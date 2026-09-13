import os
import fitz  # pymupdf
from typing import Dict
import textwrap
import urllib.request
import json
import concurrent.futures

# Suppress MuPDF low-level stderr warnings (e.g. broken xref tables in PDF templates).
# These are non-fatal format quirks — Python-level exceptions are still raised on real errors.
fitz.TOOLS.mupdf_display_errors(False)

from app.core.spells import SPELLS_BY_ID, get_spell_by_id

def fetch_spell_data(spell_id: str, name_pl: str = None, spell_level: int = 0):
    """Pobiera dane czaru w języku polskim z lokalnej bazy Spells/."""
    spell = get_spell_by_id(spell_id)
    if spell:
        return {
            "id": spell.get('id', spell_id),
            "name_pl": spell.get('name_pl') or name_pl or spell_id,
            "name_en": spell.get('name_en') if spell.get('name_en') != spell.get('name_pl') else '',
            "level": spell.get('level', spell_level),
            "school": spell.get('school', ''),
            "desc": spell.get('desc', ''),
            "casting_time": spell.get('casting_time', ''),
            "range": spell.get('range', ''),
            "components": spell.get('components', ''),
            "duration": spell.get('duration', ''),
        }
    return {
        "id": spell_id,
        "name_pl": name_pl or spell_id.replace('_', ' ').title(),
        "name_en": '',
        "level": spell_level,
        "school": 'Cantrip' if spell_level == 0 else f'Poziom {spell_level}',
        "desc": 'Opis zaklęcia w przygotowaniu.',
        "casting_time": '-',
        "range": '-',
        "components": '-',
        "duration": '-',
    }

def generate_character_pdf(char_data: dict) -> bytes:
    """
    Wypełnia kartę postaci D&D 5e (karta-postaci-interaktywna.pdf) używając pymupdf.
    Operuje całkowicie w pamięci RAM i zwraca plik PDF jako tablicę bajtów.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(base_dir, "data", "karta-postaci-interaktywna.pdf")

    if not os.path.exists(template_path):
        raise FileNotFoundError(
            f"Brakuje pliku szablonu: {template_path}. "
            "Upewnij się, że plik 'karta-postaci-interaktywna.pdf' znajduje się w katalogu app/data/."
        )

    def ms(val: int) -> str:
        return f"+{val}" if val >= 0 else str(val)

    stats = char_data['stats']
    mods  = char_data['modifiers']
    saves = char_data['saving_throws']
    skills = char_data['skill_bonuses']
    save_profs = char_data.get('saving_throw_profs', [])
    skill_profs = char_data.get('skill_profs', [])

    def has_skill_prof(skill_key: str) -> bool:
        return skill_key in skill_profs

    fields_to_fill = {
        # NAGŁÓWEK
        "Imi\u0119 postaci": char_data["name"],
        "Imi postaci":        char_data["name"],
        "kip":  f"{char_data['class_name']} {char_data['level']}",
        "rasa": char_data["race_name"],
        "poch": char_data["background_name"],
        "char": char_data["alignment"],
        "im gr": char_data.get("player", ""),
        "pd": "0",

        # GŁÓWNE STATYSTYKI — MODYFIKATORY (duże okrągłe pola na górze)
        "Pole tekstowe 29": ms(mods['str']),   # Siła modyfikator
        "Pole tekstowe 31": ms(mods['dex']),   # Zręczność modyfikator
        "Pole tekstowe 33": ms(mods['con']),   # Kondycja modyfikator
        "Pole tekstowe 35": ms(mods['int']),   # Inteligencja modyfikator
        "Pole tekstowe 37": ms(mods['wis']),   # Mądrość modyfikator
        "Pole tekstowe 39": ms(mods['cha']),   # Charyzma modyfikator

        # GŁÓWNE STATYSTYKI — WARTOŚCI BAZOWE (małe owale na dole)
        "Pole tekstowe 30": str(stats['str']),  # Siła bazowa
        "Pole tekstowe 32": str(stats['dex']),  # Zręczność bazowa
        "Pole tekstowe 34": str(stats['con']),  # Kondycja bazowa
        "Pole tekstowe 36": str(stats['int']),  # Inteligencja bazowa
        "Pole tekstowe 38": str(stats['wis']),  # Mądrość bazowa
        "Pole tekstowe 40": str(stats['cha']),  # Charyzma bazowa

        # WALKA / PODSTAWY
        "kp":   str(char_data['ac']),
        "ini":  ms(char_data['initiative']),
        "szyb": str(char_data['speed']),
        "max PW": str(char_data['hp']),
        "akt PW": str(char_data['hp']),
        "pr z b": f"+{char_data['prof_bonus']}",
        "Pasywna Madrosc": str(char_data['passive_perception']),
        "Kosc W": f"{char_data['level']}d{char_data['hit_die']}",
        "ins": "",

        # RZUTY OBRONNE (wartości liczbowe obok kółek)
        "S":   ms(saves['str']),   # Siła rzut
        "Zr":  ms(saves['dex']),   # Zręczność rzut
        "K":   ms(saves['con']),   # Kondycja rzut
        "int": ms(saves['int']),   # Inteligencja rzut
        "M":   ms(saves['wis']),   # Mądrość rzut
        "Ch":  ms(saves['cha']),   # Charyzma rzut

        # BIEGŁOŚCI W RZUTACH OBRONNYCH (checkboxy przy rzutach)
        "Pole wyboru 31": "Yes" if "str" in save_profs else "",
        "Pole wyboru 36": "Yes" if "dex" in save_profs else "",
        "Pole wyboru 37": "Yes" if "con" in save_profs else "",
        "Pole wyboru 38": "Yes" if "int" in save_profs else "",
        "Pole wyboru 39": "Yes" if "wis" in save_profs else "",
        "Pole wyboru 40": "Yes" if "cha" in save_profs else "",

        # UMIEJĘTNOŚCI — WARTOŚCI LICZBOWE (18 umiejętności alfabetycznie PL)
        "Pole tekstowe 133": ms(skills.get('akrobatyka',      mods['dex'])),  # Akrobatyka (Zrc)
        "Pole tekstowe 134": ms(skills.get('atletyka',        mods['str'])),  # Atletyka (Sił)
        "Pole tekstowe 135": ms(skills.get('historia',        mods['int'])),  # Historia (Int)
        "Pole tekstowe 136": ms(skills.get('wgląd',           mods['wis'])),  # Intuicja (Mdr)
        "Pole tekstowe 137": ms(skills.get('medycyna',        mods['wis'])),  # Medycyna (Mdr)
        "Pole tekstowe 138": ms(skills.get('zwierzęta',       mods['wis'])),  # Opieka nad zwierzętami (Mdr)
        "Pole tekstowe 139": ms(skills.get('oszustwo',        mods['cha'])),  # Oszustwo (Cha)
        "Pole tekstowe 140": ms(skills.get('postrzeganie',    mods['wis'])),  # Percepcja (Mdr)
        "Pole tekstowe 141": ms(skills.get('perswazja',       mods['cha'])),  # Perswazja (Cha)
        "Pole tekstowe 142": ms(skills.get('przyroda',        mods['int'])),  # Przyroda (Int)
        "Pole tekstowe 143": ms(skills.get('religia',         mods['int'])),  # Religia (Int)
        "Pole tekstowe 144": ms(skills.get('ukrycie',         mods['dex'])),  # Skradanie się (Zrc)
        "Pole tekstowe 145": ms(skills.get('przetrwanie',     mods['wis'])),  # Sztuka przetrwania (Mdr)
        "Pole tekstowe 146": ms(skills.get('badanie',         mods['int'])),  # Śledztwo (Int)
        "Pole tekstowe 147": ms(skills.get('arcana',          mods['int'])),  # Wiedza tajemna (Int)
        "Pole tekstowe 148": ms(skills.get('wykonanie',       mods['cha'])),  # Występy (Cha)
        "Pole tekstowe 149": ms(skills.get('zastraszanie',    mods['cha'])),  # Zastraszanie (Cha)
        "zwinne dlonie 150": ms(skills.get('sleight_of_hand', mods['dex'])),  # Zwinne dłonie (Zrc)

        # BIEGŁOŚCI W UMIEJĘTNOŚCIACH (checkboxy)
        "Pole wyboru 41": "Yes" if has_skill_prof("akrobatyka") else "",
        "Pole wyboru 42": "Yes" if has_skill_prof("atletyka") else "",
        "Pole wyboru 43": "Yes" if has_skill_prof("historia") else "",
        "Pole wyboru 44": "Yes" if has_skill_prof("wgląd") or has_skill_prof("intuicja") else "",
        "Pole wyboru 45": "Yes" if has_skill_prof("medycyna") else "",
        "Pole wyboru 46": "Yes" if has_skill_prof("zwierzęta") or has_skill_prof("obsługa zwierząt") or has_skill_prof("opieka nad zwierzętami") else "",
        "Pole wyboru 47": "Yes" if has_skill_prof("oszustwo") else "",
        "Pole wyboru 48": "Yes" if has_skill_prof("postrzeganie") or has_skill_prof("percepcja") else "",
        "Pole wyboru 49": "Yes" if has_skill_prof("perswazja") else "",
        "Pole wyboru 50": "Yes" if has_skill_prof("przyroda") else "",
        "Pole wyboru 51": "Yes" if has_skill_prof("religia") else "",
        "Pole wyboru 52": "Yes" if has_skill_prof("ukrycie") or has_skill_prof("skradanie się") or has_skill_prof("skradanie") else "",
        "Pole wyboru 53": "Yes" if has_skill_prof("przetrwanie") or has_skill_prof("sztuka przetrwania") else "",
        "Pole wyboru 54": "Yes" if has_skill_prof("badanie") or has_skill_prof("śledztwo") else "",
        "Pole wyboru 55": "Yes" if has_skill_prof("arcana") or has_skill_prof("wiedza tajemna") else "",
        "Pole wyboru 56": "Yes" if has_skill_prof("wykonanie") or has_skill_prof("występy") else "",
        "Pole wyboru 57": "Yes" if has_skill_prof("zastraszanie") else "",
        "Pole wyboru 58": "Yes" if has_skill_prof("sleight_of_hand") or has_skill_prof("zwinne dłonie") else "",

        # POZOSTAŁE SEKCJE
        "korzysci i zdolnosci": "\n".join(
            char_data.get('traits', []) + char_data.get('class_features', [])
        ),
        "pozost biegl": (
            "JĘZYKI: " + ", ".join(char_data.get('languages', [])) +
            "\nPANCERZ: " + ", ".join(char_data.get('armor_profs', ['brak'])) +
            "\nBRONIE: " + ", ".join(char_data.get('weapon_profs', ['brak']))
        ),
        "c os":    char_data.get("personality", ""),
        "idealy":  char_data.get("ideals", ""),
        "wiezi":   char_data.get("bonds", ""),
        "slabo":   char_data.get("flaws", ""),
        "wyposazenie":   char_data.get("equipment", ""),
        "ataki i magia": char_data.get("attacks", ""),
    }

    # --- CZARY (Spellcasting) ---
    # Spellcasting class header
    if char_data.get("spellcasting_stat"):
        sc_stat = char_data["spellcasting_stat"]  # e.g. "cha", "wis", "int"
        sc_mod = mods.get(sc_stat, 0)
        prof = char_data.get("prof_bonus", 2)
        spell_save_dc = 8 + prof + sc_mod
        spell_attack = prof + sc_mod
        
        stat_names_map = {"cha": "CHA", "wis": "WIS", "int": "INT"}
        fields_to_fill["CB"] = stat_names_map.get(sc_stat, sc_stat.upper())
        fields_to_fill["ST"] = str(spell_save_dc)
        fields_to_fill["PR"] = ms(spell_attack)
        fields_to_fill["czar"] = char_data.get("class_name", "")

    # Cantrips: czar 1 through czar 7
    cantrip_names = char_data.get("cantrip_names", [])
    for i, spell_name in enumerate(cantrip_names[:7]):
        fields_to_fill[f"czar {i + 1}"] = spell_name

    # Spell slots structure from PDF:
    # L1: czar 8-20 (13), max slots: "K"
    # L2: czar 21-33 (13), max slots: "K 1"
    # L3: czar 34-46 (13), max slots: "K 2"
    # L4: czar 47-59 (13), max slots: "K 3"
    # L5: czar 60-68 (9), max slots: "K 4"
    # L6: czar 69-77 (9), max slots: "K 5"
    # L7: czar 78-86 (9), max slots: "K 6"
    # L8: czar 87-93 (7), max slots: "K 7"
    # L9: czar 94-100 (7), max slots: "K 8"
    
    spell_field_info = {
        1: {"start": 8, "count": 13, "slots_field": "K"},
        2: {"start": 21, "count": 13, "slots_field": "K 1"},
        3: {"start": 34, "count": 13, "slots_field": "K 2"},
        4: {"start": 47, "count": 13, "slots_field": "K 3"},
        5: {"start": 60, "count": 9, "slots_field": "K 4"},
        6: {"start": 69, "count": 9, "slots_field": "K 5"},
        7: {"start": 78, "count": 9, "slots_field": "K 6"},
        8: {"start": 87, "count": 7, "slots_field": "K 7"},
        9: {"start": 94, "count": 7, "slots_field": "K 8"},
    }

    # Spells and Max Slots
    spell_slots = char_data.get("spell_slots", {})
    for level in range(1, 10):
        info = spell_field_info[level]
        # Fill spell names
        spell_names = char_data.get(f"spell{level}_names", [])
        for i, spell_name in enumerate(spell_names[:info["count"]]):
            fields_to_fill[f"czar {info['start'] + i}"] = spell_name
        
        # Fill max slots
        max_slots = spell_slots.get(level, 0)
        if max_slots > 0:
            fields_to_fill[info["slots_field"]] = str(max_slots)

    doc = fitz.open(template_path)

    for page in doc:
        for widget in page.widgets():
            name = widget.field_name
            if name in fields_to_fill:
                widget.field_value = fields_to_fill[name]
                widget.update()
                try:
                    doc.xref_set_key(widget.xref, "AP", "null")
                except Exception:
                    pass

    # --- NOWA STRONA: CZARY (SPELLBOOK) ---
    spell_ids = char_data.get("all_spell_ids", [])
    # Only render spell cards for spells selected on the character sheet.
    if spell_ids:
        spells_info = []
        for item in spell_ids:
            if isinstance(item, (list, tuple)) and len(item) >= 3:
                sid, name_pl, lvl = item[0], item[1], item[2]
            elif isinstance(item, str):
                sid, name_pl, lvl = item, None, 0
            else:
                continue
            res = fetch_spell_data(sid, name_pl, lvl)
            if res:
                spells_info.append(res)
    else:
        spells_info = []

    def insert_fitted_text(page, rect, text, fontname, color, sizes, align=0):
        text = str(text or "-").strip() or "-"
        for size in sizes:
            result = page.insert_textbox(
                rect, text, fontsize=size, fontname=fontname,
                color=color, align=align
            )
            if result >= 0:
                return

        low = 1
        high = len(text)
        best = "-"
        while low <= high:
            mid = (low + high) // 2
            candidate = text[:mid].rstrip() + "..."
            result = page.insert_textbox(
                rect, candidate, fontsize=sizes[-1], fontname=fontname,
                color=color, align=align
            )
            if result >= 0:
                best = candidate
                low = mid + 1
            else:
                high = mid - 1
        page.insert_textbox(
            rect, best, fontsize=sizes[-1], fontname=fontname,
            color=color, align=align
        )

    if spells_info:
        spells_info.sort(key=lambda s: (s.get('level', 0), s.get('name_pl', '')))

        CARD_WIDTH = 175
        CARD_HEIGHT = 245
        GAP_X = 15
        GAP_Y = 15
        MARGIN_X = (595 - (3 * CARD_WIDTH + 2 * GAP_X)) / 2
        MARGIN_Y = (842 - (3 * CARD_HEIGHT + 2 * GAP_Y)) / 2

        def init_page():
            p = doc.new_page()
            try:
                curr_dir = os.path.dirname(os.path.abspath(__file__))
                font_dir = os.path.join(os.path.dirname(curr_dir), "static", "fonts")
                reg_font = os.path.join(font_dir, "Roboto-Regular.ttf")
                bold_font = os.path.join(font_dir, "Roboto-Bold.ttf")
                if not os.path.exists(reg_font):
                    reg_font = "app/static/fonts/Roboto-Regular.ttf"
                    bold_font = "app/static/fonts/Roboto-Bold.ttf"
                p.insert_font(fontname="roboreg", fontfile=reg_font)
                p.insert_font(fontname="robobold", fontfile=bold_font)
            except Exception:
                pass
            return p

        page = init_page()
        cards_on_page = 0
        school_colors = {
            'Abjuration': (0.18, 0.38, 0.58),
            'Conjuration': (0.42, 0.24, 0.56),
            'Divination': (0.62, 0.42, 0.10),
            'Enchantment': (0.15, 0.44, 0.35),
            'Evocation': (0.62, 0.22, 0.22),
            'Illusion': (0.32, 0.27, 0.56),
            'Necromancy': (0.25, 0.23, 0.30),
            'Transmutation': (0.10, 0.43, 0.45),
            'default': (0.28, 0.32, 0.30),
        }

        for spell in spells_info:
            if cards_on_page >= 9:
                page = init_page()
                cards_on_page = 0

            col = cards_on_page % 3
            row = cards_on_page // 3
            x = MARGIN_X + col * (CARD_WIDTH + GAP_X)
            y = MARGIN_Y + row * (CARD_HEIGHT + GAP_Y)
            rect = fitz.Rect(x, y, x + CARD_WIDTH, y + CARD_HEIGHT)
            page.draw_rect(rect, color=(0.16, 0.20, 0.18), fill=(0.985, 0.975, 0.92), width=0.8)

            header_rect = fitz.Rect(x, y, x + CARD_WIDTH, y + 36)
            page.draw_rect(
                header_rect, color=(0, 0, 0),
                fill=school_colors.get(spell.get('school'), school_colors['default']), width=0
            )

            title = spell.get('name_pl') or spell.get('name_en') or 'Nieznane'
            title_en = spell.get('name_en') or ''
            insert_fitted_text(page, fitz.Rect(x + 5, y + 3, x + CARD_WIDTH - 5, y + 18), title, 'robobold', (0.98, 0.98, 0.94), [11, 10, 9, 8])
            if title_en and title_en != title:
                insert_fitted_text(page, fitz.Rect(x + 5, y + 19, x + CARD_WIDTH - 5, y + 32), title_en, 'roboreg', (0.80, 0.88, 0.82), [8.5, 7.5, 6.5])

            level = spell.get('level', 0)
            level_str = spell.get('school') or ('Sztuczka' if level == 0 else f'Poziom {level}')
            insert_fitted_text(page, fitz.Rect(x + 5, y + 38, x + CARD_WIDTH - 5, y + 49), level_str, 'robobold', (0.2, 0.2, 0.2), [8, 7, 6])
            page.draw_line(fitz.Point(x + 5, y + 51), fitz.Point(x + CARD_WIDTH - 5, y + 51), color=(0.62, 0.66, 0.60), width=0.7)

            meta_y = y + 55
            col1_x = x + 5
            col2_x = x + CARD_WIDTH / 2 + 2
            meta_fields = [
                (fitz.Rect(col1_x, meta_y, col2_x - 3, meta_y + 18), f"Czas: {spell.get('casting_time') or '-'}"),
                (fitz.Rect(col2_x, meta_y, x + CARD_WIDTH - 5, meta_y + 18), f"Zasięg: {spell.get('range') or '-'}"),
                (fitz.Rect(col1_x, meta_y + 18, col2_x - 3, meta_y + 36), f"Komp: {spell.get('components') or '-'}"),
                (fitz.Rect(col2_x, meta_y + 18, x + CARD_WIDTH - 5, meta_y + 36), f"Trwanie: {spell.get('duration') or '-'}"),
            ]
            for meta_rect, meta_text in meta_fields:
                insert_fitted_text(page, meta_rect, meta_text, 'roboreg', (0.14, 0.18, 0.15), [7, 6.3, 5.7])

            page.draw_line(fitz.Point(x + 5, meta_y + 40), fitz.Point(x + CARD_WIDTH - 5, meta_y + 40), color=(0.62, 0.66, 0.60), width=0.7)
            desc_rect = fitz.Rect(x + 6, meta_y + 46, x + CARD_WIDTH - 6, y + CARD_HEIGHT - 6)
            desc = " ".join(str(spell.get('desc') or 'Brak opisu.').split())
            insert_fitted_text(page, desc_rect, desc, 'roboreg', (0.12, 0.14, 0.12), [7.4, 7.0, 6.6, 6.2, 5.8])
            cards_on_page += 1

    wild_shape_forms = char_data.get("wild_shape_forms", [])
    if wild_shape_forms:
        card_width = 280
        card_height = 370
        gap_x = 15
        gap_y = 12
        margin_x = (595 - (2 * card_width + gap_x)) / 2
        top_margin = 42

        def new_wild_shape_page():
            wild_page = doc.new_page()
            try:
                curr_dir = os.path.dirname(os.path.abspath(__file__))
                font_dir = os.path.join(os.path.dirname(curr_dir), "static", "fonts")
                reg_font = os.path.join(font_dir, "Roboto-Regular.ttf")
                bold_font = os.path.join(font_dir, "Roboto-Bold.ttf")
                if not os.path.exists(reg_font):
                    reg_font = "app/static/fonts/Roboto-Regular.ttf"
                    bold_font = "app/static/fonts/Roboto-Bold.ttf"
                wild_page.insert_font(fontname="roboreg", fontfile=reg_font)
                wild_page.insert_font(fontname="robobold", fontfile=bold_font)
            except Exception:
                pass
            wild_page.insert_text(
                (margin_x, 24), "FORMY ZWIERZĘCE DRUIDA",
                fontsize=15, fontname="robobold", color=(0.12, 0.28, 0.18)
            )
            wild_page.insert_text(
                (margin_x, 36), "Dostępne formy według poziomu i subklasy postaci",
                fontsize=7.5, fontname="roboreg", color=(0.32, 0.38, 0.34)
            )
            return wild_page

        page = new_wild_shape_page()
        forms_on_page = 0
        for form in wild_shape_forms:
            if forms_on_page >= 4:
                page = new_wild_shape_page()
                forms_on_page = 0

            col = forms_on_page % 2
            row = forms_on_page // 2
            x = margin_x + col * (card_width + gap_x)
            y = top_margin + row * (card_height + gap_y)
            card_rect = fitz.Rect(x, y, x + card_width, y + card_height)
            page.draw_rect(card_rect, color=(0.16, 0.30, 0.21), fill=(0.96, 0.98, 0.95), width=0.8)

            header = fitz.Rect(x, y, x + card_width, y + 31)
            page.draw_rect(header, color=(0.10, 0.25, 0.16), fill=(0.14, 0.38, 0.23), width=0)
            title = f"{form.get('name', 'Nieznana forma')}  |  CR {form.get('cr', '-') }"
            page.insert_text((x + 8, y + 14), title, fontsize=10, fontname="robobold", color=(0.95, 0.98, 0.92))
            name_en = form.get("name_en", "")
            if name_en:
                page.insert_text((x + 8, y + 27), name_en, fontsize=7.5, fontname="roboreg", color=(0.75, 0.88, 0.78))

            stat_y = y + 37
            challenge_label = form.get("challenge", "CR " + str(form.get("cr", "-")))
            stat_labels = [
                f"{form.get('type', 'Bestia')}",
                f"KP {form.get('ac', '-')}   HP {form.get('hp', '-')}   Szybkość: {form.get('speed', '-')}",
                f"Cechy: {form.get('ability_scores', '-')}  (S, Zr, K, Int, M, Cha)",
                f"{challenge_label}  |  Języki: {form.get('languages', '-')}",
            ]
            for index, stat_line in enumerate(stat_labels):
                insert_fitted_text(page, fitz.Rect(x + 8, stat_y + index * 13, x + card_width - 8, stat_y + 12 + index * 13), stat_line, "robobold" if index == 0 else "roboreg", (0.18, 0.24, 0.19), [7.5, 6.5])

            body_y = stat_y + 56
            sections = [
                ("Zmysły", form.get("senses", "-")),
                ("Umiejętności", form.get("skills", "-")),
                ("Rzuty obronne", form.get("saving_throws", "-")),
                ("Odporności", form.get("damage_resistances", "-")),
                ("Immunitety", f"Obrażenia: {form.get('damage_immunities', '-')} | Stany: {form.get('condition_immunities', '-')}"),
                ("Języki", form.get("languages", "-")),
                ("Cechy", f"{form.get('special_abilities', '-')} {form.get('features', '')}"),
                ("Akcje", form.get("action_details", form.get("attacks", "-"))),
            ]
            section_height = 34
            for index, (label, value) in enumerate(sections):
                section_y = body_y + index * section_height
                page.draw_line(fitz.Point(x + 8, section_y), fitz.Point(x + card_width - 8, section_y), color=(0.78, 0.84, 0.78), width=0.35)
                insert_fitted_text(page, fitz.Rect(x + 8, section_y + 3, x + 96, section_y + 13), label.upper(), "robobold", (0.16, 0.38, 0.22), [6.5, 5.8])
                insert_fitted_text(page, fitz.Rect(x + 96, section_y + 3, x + card_width - 8, section_y + 30), value, "roboreg", (0.18, 0.20, 0.18), [7.0, 6.5, 6.0, 5.5])
            forms_on_page += 1

    pdf_bytes = doc.tobytes(garbage=4, deflate=True)
    doc.close()
    return pdf_bytes
