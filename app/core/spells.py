"""
Spells Database Loader for D&D 5e (Polish Edition).
Loads and parses all spells from the Spells/ CSV files.
"""

import os
import glob
import csv
import re
from typing import Dict, List, Optional, Any

# Map of old English IDs to their official Polish names for backward compatibility
OLD_EN_ID_TO_PL_NAME = {
    'acid_splash': 'KWASOWY ROZPRYSK',
    'chill_touch': 'DOTYK ŚMIERCI',
    'dancing_lights': 'TAŃCZĄCE ŚWIATŁA',
    'eldritch_blast': 'MISTYCZNE UDERZENIE',
    'fire_bolt': 'OGNISTY POCISK',
    'guidance': 'PRZEWODNICTWO',
    'light': 'ŚWIATŁO',
    'mage_hand': 'MAGICZNA DŁOŃ',
    'minor_illusion': 'POMNIEJSZA ILUZJA',
    'prestidigitation': 'KUGLARSTWO',
    'ray_of_frost': 'PROMIEŃ MROZU',
    'shocking_grasp': 'PORAŻAJĄCY UŚCISK',
    'sacred_flame': 'ŚWIĘTY PŁOMIEŃ',
    'thaumaturgy': 'TAUMATURGIA',
    'toll_the_dead': 'BIJĄCE DZWONY',
    'druidcraft': 'DRUIDYZM',
    'poison_spray': 'TRUJĄCY ROZPRYSK',
    'produce_flame': 'WYWOŁANIE PŁOMIENIA',
    'resistance': 'OPÓR',
    'shillelagh': 'KOSTUR',
    'thorn_whip': 'CIERNIOWY BICZ',
    'vicious_mockery': 'ZJADLIWE SZYDERSTWO',
    'mending': 'NAPRAWA',
    'message': 'WIADOMOŚĆ',
    'true_strike': 'PRAWDZIWE UDERZENIE',
    'blade_ward': 'OSŁONA PRZED ORĘŻEM',
    'friends': 'PRZYJAŹŃ',
    'spare_the_dying': 'OSZCZĘDZENIE KONAJĄCEGO',
    'absorb_elements': 'WCHŁONIĘCIE ŻYWIOŁÓW',
    'alarm': 'ALARM',
    'animal_friendship': 'PRZYJAŹŃ ZE ZWIERZĘTAMI',
    'bane': 'ZGUBNE SŁOWO',
    'bless': 'BŁOGOSŁAWIEŃSTWO',
    'burning_hands': 'PŁONĄCE DŁONIE',
    'charm_person': 'UROCZENIE OSOBY',
    'color_spray': 'BARWNY ROZPRYSK',
    'command': 'ROZKAZ',
    'comprehend_languages': 'ROZUMIENIE JĘZYKÓW',
    'cure_wounds': 'LECZENIE RAN',
    'detect_magic': 'WYKRYCIE MAGII',
    'disguise_self': 'PRZEBRANIE',
    'dissonant_whispers': 'FAŁSZYWE PODSZEPTY',
    'faerie_fire': 'BLASK FAERIE',
    'feather_fall': 'PIÓRKOWE OPADANIE',
    'fog_cloud': 'CHMURA MGŁY',
    'guiding_bolt': 'POWADZĄCY POCISK',
    'healing_word': 'SŁOWO LECZENIA',
    'hellish_rebuke': 'PIEKIELNA REPRYMANDA',
    'hex': 'UROK',
    'hunter_mark': 'ZNAMIĘ ŁOWCY',
    'identify': 'IDENTYFIKACJA',
    'inflict_wounds': 'ZADANIE RAN',
    'jump': 'SKOK',
    'longstrider': 'DŁUGI KROK',
    'mage_armor': 'ZBROJA MAGA',
    'magic_missile': 'MAGICZNY POCISK',
    'protection_from_evil_and_good': 'OCHRONA PRZED ZŁEM I DOBREM',
    'purify_food_and_drink': 'OCZYSZCZENIE JEDZENIA I NAPOJÓW',
    'sanctuary': 'AZYL',
    'shield': 'TARCZA',
    'shield_of_faith': 'TARCZA WIARY',
    'silent_image': 'CICHY OBRAZ',
    'sleep': 'UŚPIENIE',
    'speak_with_animals': 'ROZMOWA ZE ZWIERZĘTAMI',
    'thunderwave': 'FALA GROMU',
    'witch_bolt': 'CZAROWNY POCISK',
    'blindness_deafness': 'ŚLEPOTA LUB GŁUCHOTA',
    'blur': 'ROZMYCIE',
    'darkness': 'CIEMNOŚĆ',
    'darkvision': 'WIDZENIE W CIEMNOŚCI',
    'hold_person': 'UNIERUCHOMIENIE OSOBY',
    'invisibility': 'NIEWIDZIALNOŚĆ',
    'knock': 'KOŁATANIE',
    'lesser_restoration': 'MNIEJSZE PRZYWRÓCENIE',
    'levitate': 'LEWITACJA',
    'mirror_image': 'LUSTRZANE ODBICIE',
    'misty_step': 'KROK PRZEZ MGŁĘ',
    'pass_without_trace': 'BEZŚLADOWE PRZEJŚCIE',
    'scorching_ray': 'PIEKĄCY PROMIEŃ',
    'see_invisibility': 'WIDZENIE NIEWIDZIALNEGO',
    'shatter': 'ROZTRZASKANIE',
    'spider_climb': 'PAJĘCZY CHÓD',
    'spiritual_weapon': 'DUCHOWY ORĘŻ',
    'suggestion': 'SUGESTIA',
    'web': 'PAJĘCZYNA',
    'moonbeam': 'PROMIEŃ KSIĘŻYCA',
    'flaming_sphere': 'PŁONĄCA SFERA',
    'barkskin': 'KORA DRZEWNA',
    'enhance_ability': 'WZMOCNIENIE CECHY',
    'spike_growth': 'KOLCZASTY WZROST',
    'counterspell': 'KONTRCZAR',
    'dispel_magic': 'ROZPROSZENIE MAGII',
    'fireball': 'KULA OGNIA',
    'fly': 'LATANIE',
    'haste': 'PRZYSPIESZENIE',
    'lightning_bolt': 'BŁYSKAWICA',
    'revivify': 'OŻYWIENIE',
    'spirit_guardians': 'DUCHOWI STRAŻNICY',
    'call_lightning': 'WEZWANIE BŁYSKAWICY',
    'plant_growth': 'ROZROST ROŚLIN',
    'sleet_storm': 'BURZA ŚNIEŻNA',
    'slow': 'SPOWOLNIENIE',
    'tongues': 'JĘZYKI',
    'vampiric_touch': 'WAMPIRYCZNY DOTYK',
    'hypnotic_pattern': 'HIPNOTYCZNY WZÓR',
    'banishment': 'WYGNANIE',
    'dimension_door': 'DRZWI PRZEZ WYMIARY',
    'greater_invisibility': 'WIĘKSZA NIEWIDZIALNOŚĆ',
    'polymorph': 'POLIMORFIA',
    'wall_of_fire': 'ŚCIANA OGNIA',
    'blight': 'ZWIĘDNIEĆ',
    'death_ward': 'ZABEZPIECZENIE PRZED ŚMIERCIĄ',
    'divination': 'WIESZCZENIE',
    'cloudkill': 'ZABÓJCZA CHMURA',
    'cone_of_cold': 'STOŻEK ZIMNA',
    'greater_restoration': 'WIĘKSZE PRZYWRÓCENIE',
    'hold_monster': 'UNIERUCHOMIENIE POTWORA',
    'mass_cure_wounds': 'MASOWE LECZENIE RAN',
    'teleportation_circle': 'KRĄG TELEPORTACJI',
    'wall_of_force': 'ŚCIANA MOCY',
    'chain_lightning': 'ŁAŃCUCH BŁYSKAWIC',
    'disintegrate': 'DEZINTEGRACJA',
    'globe_of_invulnerability': 'KULA NIEWRAŻLIWOŚCI',
    'heal': 'UZDROWIENIE',
    'mass_suggestion': 'MASOWA SUGESTIA',
    'true_seeing': 'PRAWDZIWE WIDZENIE',
    'finger_of_death': 'PALEC ŚMIERCI',
    'fire_storm': 'BURZA OGNIA',
    'plane_shift': 'PODRÓŻ PRZEZ SFERY',
    'teleport': 'TELEPORTACJA',
    'forcecage': 'KLATKA MOCY',
    'antimagic_field': 'POLE ANTYMAGICZNE',
    'dominate_monster': 'ZDOMINOWANIE POTWORA',
    'earthquake': 'TRZĘSIENIE ZIEMI',
    'feeblemind': 'ZAGŁADA UMYSŁU',
    'sunburst': 'WYBUCH SŁOŃCA',
    'incendiary_cloud': 'ZAPALAJĄCA CHMURA',
    'gate': 'BRAMA',
    'meteor_swarm': 'RÓJ METEORÓW',
    'power_word_kill': 'SŁOWO MOCY: GIŃ',
    'time_stop': 'ZATRZYMANIE CZASU',
    'true_polymorph': 'PRAWDZIWA POLIMORFIA',
    'wish': 'ŻYCZENIE'
}

# Standard Artificer spells
ARTIFICER_SPELL_SLUGS = [
    'kwasowy_rozpysk', 'ognisty_pocisk', 'przewodnictwo', 'swiatlo',
    'magiczna_dlon', 'kuglarstwo', 'promien_mrozu', 'porazajacy_ucisk',
    'trujacy_rozpysk', 'opor', 'naprawa', 'alarm', 'leczenie_ran',
    'wykrycie_magii', 'przebranie', 'piorkowe_opadanie', 'identyfikacja',
    'azyl', 'skok', 'dlugi_krok', 'oczyszczenie_jedzenia_i_napojow'
]

def make_slug(name: str) -> str:
    """Converts a Polish spell name to a snake_case slug."""
    repl = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
        'Ą': 'a', 'Ć': 'c', 'Ę': 'e', 'Ł': 'l', 'Ń': 'n',
        'Ó': 'o', 'Ś': 's', 'Ź': 'z', 'Ż': 'z'
    }
    s = name.strip()
    for k, v in repl.items():
        s = s.replace(k, v)
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '_', s)
    return s.strip('_')

def format_title(name: str) -> str:
    """Formats a Polish spell name with proper title casing."""
    lower_words = {
        'w', 'we', 'z', 'ze', 'i', 'na', 'do', 'o', 'od',
        'po', 'pod', 'nad', 'przed', 'za', 'ku', 'dla', 'lub'
    }
    words = name.strip().split()
    res = []
    for idx, w in enumerate(words):
        wl = w.lower()
        if idx > 0 and wl in lower_words:
            res.append(wl)
        else:
            # Handle words with punctuation like "Mocy:" or "(Wariant)"
            res.append(w.capitalize())
    return ' '.join(res)

def clean_desc_plain(desc_html: str) -> str:
    """Cleans HTML tags from description, converting breaks to newlines."""
    text = desc_html.replace('<br>', '\n').replace('<br/>', '\n').replace('<br />', '\n')
    text = re.sub(r'<[^>]+>', '', text)
    # Normalize multiple consecutive empty lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def _find_spells_dir() -> str:
    """Locates the Spells directory in the project."""
    base_core = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(base_core, '..', '..', 'Spells'),
        os.path.join(base_core, '..', 'Spells'),
        os.path.join(os.getcwd(), 'dnd', 'Spells'),
        os.path.join(os.path.abspath(os.path.join(os.getcwd(), '..')), 'Spells'),
    ]
    for c in candidates:
        if os.path.isdir(c):
            return os.path.abspath(c)
    raise FileNotFoundError("Nie znaleziono katalogu 'Spells' z plikami CSV czarów!")

def load_spells_database():
    """Parses all CSV files in the Spells folder and builds spell catalogs."""
    spells_dir = _find_spells_dir()
    csv_files = glob.glob(os.path.join(spells_dir, '*.csv'))
    
    class_name_map = {
        'bard': 'bard',
        'cleric': 'cleric',
        'druid': 'druid',
        'paladin': 'paladin',
        'ranger': 'ranger',
        'sorcerer': 'sorcerer',
        'warlock': 'warlock',
        'wizard': 'wizard'
    }

    all_spells_by_id = {}
    by_level = {f'level_{i}': [] for i in range(1, 10)}
    by_level['cantrip'] = []
    
    for fpath in csv_files:
        base_name = os.path.basename(fpath).replace('_pl.csv', '').replace('.csv', '').lower()
        default_class = class_name_map.get(base_name, base_name)
        
        with open(fpath, encoding='utf-8', errors='replace') as fp:
            reader = csv.reader(fp, delimiter=';')
            for row in reader:
                if not row or len(row) < 8:
                    continue
                level_raw = row[0].strip()
                if not level_raw.isdigit():
                    continue
                    
                lvl = int(level_raw)
                name_raw = row[1].strip()
                school = row[2].strip()
                casting_time = row[3].strip()
                spell_range = row[4].strip()
                components = row[5].strip()
                duration = row[6].strip()
                desc_raw = row[7].strip()
                
                slug = make_slug(name_raw)
                title_pl = format_title(name_raw)
                
                if slug not in all_spells_by_id:
                    spell_obj = {
                        'id': slug,
                        'name_pl': title_pl,
                        'name_en': title_pl,  # Default to title_pl
                        'raw_name': name_raw,
                        'level': lvl,
                        'school': school,
                        'casting_time': casting_time,
                        'range': spell_range,
                        'components': components,
                        'duration': duration,
                        'desc': clean_desc_plain(desc_raw),
                        'desc_html': desc_raw,
                        'classes': [default_class]
                    }
                    all_spells_by_id[slug] = spell_obj
                    
                    cat_key = 'cantrip' if lvl == 0 else f'level_{lvl}'
                    by_level[cat_key].append(spell_obj)
                else:
                    if default_class not in all_spells_by_id[slug]['classes']:
                        all_spells_by_id[slug]['classes'].append(default_class)

    # Assign artificer spells
    for art_slug in ARTIFICER_SPELL_SLUGS:
        if art_slug in all_spells_by_id:
            if 'artificer' not in all_spells_by_id[art_slug]['classes']:
                all_spells_by_id[art_slug]['classes'].append('artificer')

    # Sort each level list alphabetically by Polish name
    for cat_key in by_level:
        by_level[cat_key].sort(key=lambda s: s['name_pl'])

    # Build backward-compatibility aliases
    # Map old English IDs to their corresponding spell object
    raw_name_to_obj = {s['raw_name'].upper(): s for s in all_spells_by_id.values()}
    slug_lookup = dict(all_spells_by_id)
    
    for en_id, pl_name in OLD_EN_ID_TO_PL_NAME.items():
        matched_obj = raw_name_to_obj.get(pl_name.upper())
        if not matched_obj:
            # Try by slug
            pl_slug = make_slug(pl_name)
            matched_obj = all_spells_by_id.get(pl_slug)
            
        if matched_obj:
            # Register alias in lookup
            slug_lookup[en_id] = matched_obj
            # Set English title if not already set
            matched_obj['name_en'] = en_id.replace('_', ' ').title()

    return by_level, slug_lookup

# Module-level singletons initialized on load
SPELLS, SPELLS_BY_ID = load_spells_database()

def get_spell_by_id(spell_id: str) -> Optional[Dict[str, Any]]:
    """Lookup spell by its ID or old English alias."""
    if not spell_id:
        return None
    slug = spell_id.strip()
    # Direct match in lookup (handles both slugs and old English IDs)
    if slug in SPELLS_BY_ID:
        return SPELLS_BY_ID[slug]
    # Try normalized slug
    norm_slug = make_slug(slug)
    if norm_slug in SPELLS_BY_ID:
        return SPELLS_BY_ID[norm_slug]
    return None

def get_spells(class_name: Optional[str] = None, level: Optional[Any] = None, search: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Filters and returns spells matching the given criteria.
    - class_name: e.g. 'bard', 'cleric', 'wizard', 'all' or None.
    - level: 0 to 9, 'all', or None.
    - search: substring search in name_pl, school, or desc.
    """
    class_alias = {
        'mag': 'wizard',
        'czarodziej': 'wizard',
        'kleryk': 'cleric',
        'lowca': 'ranger',
        'łowca': 'ranger',
        'zaklinacz': 'sorcerer',
        'czarnoksieznik': 'warlock',
        'czarnoksiężnik': 'warlock',
        'paladyn': 'paladin'
    }
    
    filter_class = None
    if class_name and class_name.lower() not in ('all', '', 'none'):
        raw_c = class_name.lower().strip()
        filter_class = class_alias.get(raw_c, raw_c)

    filter_level = None
    if level is not None and str(level).lower() not in ('all', '', 'none'):
        try:
            filter_level = int(level)
        except (ValueError, TypeError):
            pass

    search_term = search.lower().strip() if search else None

    # Collect matching spells
    results = []
    # Loop across levels
    target_levels = [filter_level] if filter_level is not None else list(range(10))
    
    for lvl in target_levels:
        cat_key = 'cantrip' if lvl == 0 else f'level_{lvl}'
        for spell in SPELLS.get(cat_key, []):
            # Class filter
            if filter_class:
                if filter_class not in spell['classes']:
                    continue
            
            # Search filter
            if search_term:
                match = (
                    search_term in spell['name_pl'].lower() or
                    search_term in spell.get('name_en', '').lower() or
                    search_term in spell['school'].lower() or
                    search_term in spell['desc'].lower()
                )
                if not match:
                    continue
                    
            results.append(spell)

    return results
