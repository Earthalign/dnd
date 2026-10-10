"""
D&D 5e Starting Equipment Data
Based on Player's Handbook - class starting equipment choices.
"""

# Equipment options per class: each entry = one "package" option
# Format: { id, name_pl, category, damage, damage_type, weight, props, notes }

WEAPONS = {
    # Simple Melee
    "club":         {"name": "Pałka", "damage": "1k4", "type": "obuchowe", "weight": "Lekka", "range": "wręcz", "profs": ["prosta"]},
    "dagger":       {"name": "Sztylet", "damage": "1k4", "type": "kłute", "weight": "Lekka", "range": "wręcz/dystans", "profs": ["prosta"], "props": "Finezja, Rzut (3/9m)"},
    "greatclub":    {"name": "Kij bojowy", "damage": "1k8", "type": "obuchowe", "weight": "Dwuręczna", "range": "wręcz", "profs": ["prosta"]},
    "handaxe":      {"name": "Ręczny topór", "damage": "1k6", "type": "sieczne", "weight": "Lekka", "range": "wręcz/dystans", "profs": ["prosta"], "props": "Lekka, Rzut (6/18m)"},
    "javelin":      {"name": "Oszczep", "damage": "1k6", "type": "kłute", "weight": "—", "range": "wręcz/dystans", "profs": ["prosta"], "props": "Rzut (9/36m)"},
    "light_hammer": {"name": "Lekki młot", "damage": "1k4", "type": "obuchowe", "weight": "Lekka", "range": "wręcz/dystans", "profs": ["prosta"], "props": "Lekka, Rzut (6/18m)"},
    "mace":         {"name": "Buława", "damage": "1k6", "type": "obuchowe", "weight": "—", "range": "wręcz", "profs": ["prosta"]},
    "quarterstaff": {"name": "Kij", "damage": "1k6/1k8", "type": "obuchowe", "weight": "Wszechstronna", "range": "wręcz", "profs": ["prosta"], "props": "Wszechstronna (1k8)"},
    "spear":        {"name": "Włócznia", "damage": "1k6/1k8", "type": "kłute", "weight": "—", "range": "wręcz/dystans", "profs": ["prosta"], "props": "Rzut (6/18m), Wszechstronna (1k8)"},
    "scimitar":     {"name": "Scimitar", "damage": "1k6", "type": "sieczne", "weight": "Lekka", "range": "wręcz", "profs": ["prosta", "bojowa"], "props": "Finezja, Lekka"},
    "sickle":       {"name": "Sierp", "damage": "1k4", "type": "sieczne", "weight": "Lekka", "range": "wręcz", "profs": ["prosta"], "props": "Lekka"},
    # Simple Ranged
    "light_crossbow": {"name": "Lekka kusza", "damage": "1k8", "type": "kłute", "weight": "Dwuręczna", "range": "dystans", "profs": ["prosta"], "props": "Zasięg (24/96m), Ładowanie, Dwuręczna"},
    "shortbow":     {"name": "Krótki łuk", "damage": "1k6", "type": "kłute", "weight": "Dwuręczna", "range": "dystans", "profs": ["prosta"], "props": "Zasięg (24/96m), Dwuręczna"},
    # Martial Melee
    "battleaxe":    {"name": "Topór bojowy", "damage": "1k8/1k10", "type": "sieczne", "weight": "Wszechstronna", "range": "wręcz", "profs": ["bojowa"], "props": "Wszechstronna (1k10)"},
    "flail":        {"name": "Cep", "damage": "1k8", "type": "obuchowe", "weight": "—", "range": "wręcz", "profs": ["bojowa"]},
    "glaive":       {"name": "Glewia", "damage": "1k10", "type": "sieczne", "weight": "Ciężka, Zasięg", "range": "wręcz", "profs": ["bojowa"], "props": "Ciężka, Zasięg, Dwuręczna"},
    "greataxe":     {"name": "Wielki topór", "damage": "1k12", "type": "sieczne", "weight": "Ciężka, Dwuręczna", "range": "wręcz", "profs": ["bojowa"]},
    "greatsword":   {"name": "Wielki miecz", "damage": "2k6", "type": "sieczne", "weight": "Ciężka, Dwuręczna", "range": "wręcz", "profs": ["bojowa"]},
    "longsword":    {"name": "Długi miecz", "damage": "1k8/1k10", "type": "sieczne", "weight": "Wszechstronna", "range": "wręcz", "profs": ["bojowa"], "props": "Wszechstronna (1k10)"},
    "maul":         {"name": "Maul", "damage": "2k6", "type": "obuchowe", "weight": "Ciężka, Dwuręczna", "range": "wręcz", "profs": ["bojowa"]},
    "rapier":       {"name": "Rapier", "damage": "1k8", "type": "kłute", "weight": "—", "range": "wręcz", "profs": ["bojowa"], "props": "Finezja"},
    "shortsword":   {"name": "Krótki miecz", "damage": "1k6", "type": "kłute", "weight": "Lekka", "range": "wręcz", "profs": ["bojowa"], "props": "Finezja, Lekka"},
    "trident":      {"name": "Trójząb", "damage": "1k6/1k8", "type": "kłute", "weight": "Wszechstronna", "range": "wręcz/dystans", "profs": ["bojowa"], "props": "Rzut (6/18m), Wszechstronna (1k8)"},
    "warhammer":    {"name": "Młot bojowy", "damage": "1k8/1k10", "type": "obuchowe", "weight": "Wszechstronna", "range": "wręcz", "profs": ["bojowa"], "props": "Wszechstronna (1k10)"},
    # Martial Ranged
    "hand_crossbow": {"name": "Ręczna kusza", "damage": "1k6", "type": "kłute", "weight": "Lekka", "range": "dystans", "profs": ["bojowa"], "props": "Zasięg (9/36m), Ładowanie, Lekka"},
    "heavy_crossbow": {"name": "Ciężka kusza", "damage": "1k10", "type": "kłute", "weight": "Ciężka, Dwuręczna", "range": "dystans", "profs": ["bojowa"], "props": "Zasięg (30/120m), Ciężka, Ładowanie, Dwuręczna"},
    "longbow":      {"name": "Długi łuk", "damage": "1k8", "type": "kłute", "weight": "Ciężka, Dwuręczna", "range": "dystans", "profs": ["bojowa"], "props": "Zasięg (45/180m), Ciężka, Dwuręczna"},
}

ARMORS = {
    "none":           {"name": "Brak zbroi", "ac": "10 + DEX", "type": "brak", "stealth": "—"},
    "padded":         {"name": "Watowana", "ac": 11, "type": "lekka", "stealth": "Utrudnienie", "notes": "AC 11 + DEX"},
    "leather":        {"name": "Skórzana", "ac": 11, "type": "lekka", "notes": "AC 11 + DEX"},
    "studded_leather":{"name": "Ćwiekowana skóra", "ac": 12, "type": "lekka", "notes": "AC 12 + DEX"},
    "hide":           {"name": "Skóra gruba", "ac": 12, "type": "średnia", "notes": "AC 12 + DEX (max 2)"},
    "chain_shirt":    {"name": "Koszulka kolcza", "ac": 13, "type": "średnia", "notes": "AC 13 + DEX (max 2)"},
    "scale_mail":     {"name": "Łuskowa", "ac": 14, "type": "średnia", "stealth": "Utrudnienie", "notes": "AC 14 + DEX (max 2)"},
    "breastplate":    {"name": "Napierśnik", "ac": 14, "type": "średnia", "notes": "AC 14 + DEX (max 2)"},
    "half_plate":     {"name": "Półpłytowa", "ac": 15, "type": "średnia", "stealth": "Utrudnienie", "notes": "AC 15 + DEX (max 2)"},
    "ring_mail":      {"name": "Pierścieniowa", "ac": 14, "type": "ciężka", "stealth": "Utrudnienie", "notes": "AC 14 (bez DEX)"},
    "chain_mail":     {"name": "Kolcza", "ac": 16, "type": "ciężka", "stealth": "Utrudnienie", "notes": "AC 16 (bez DEX), wymaga STR 13"},
    "splint":         {"name": "Szynowa", "ac": 17, "type": "ciężka", "stealth": "Utrudnienie", "notes": "AC 17 (bez DEX), wymaga STR 15"},
    "plate":          {"name": "Płytowa", "ac": 18, "type": "ciężka", "stealth": "Utrudnienie", "notes": "AC 18 (bez DEX), wymaga STR 15"},
    "shield":         {"name": "Tarcza", "ac": "+2", "type": "tarcza", "notes": "+2 do KP, nie można używać z dwuręczną bronią"},
}

# Starting equipment packages per class
CLASS_EQUIPMENT = {
    "artificer": {
        "options": [
            {
                "id": "artificer_a",
                "label": "Pakiet A: Łuskowa (Scale Mail) + 2x Prosta Broń (Sztylety) + Kusza + Narzędzia",
                "weapons": ["dagger", "dagger", "light_crossbow"],
                "armor": "scale_mail",
                "shield": False,
                "notes": "Wynalazca noszący średni pancerz. Posiada narzędzia złodziejskie i rzemieślnicze.",
            },
            {
                "id": "artificer_b",
                "label": "Pakiet B: Ćwiekowana skóra + Prosta Broń + Kusza + Narzędzia",
                "weapons": ["mace", "light_crossbow"],
                "armor": "studded_leather",
                "shield": False,
                "notes": "Lżejszy zestaw dla większej mobilności (stealth).",
            },
        ]
    },
    "barbarian": {
        "options": [
            {
                "id": "barb_a",
                "label": "Pakiet A: Wielki topór + 2x Oszczepy + Ekwipunek odkrywcy",
                "weapons": ["greataxe", "javelin", "javelin"],
                "armor": "none",
                "shield": False,
                "notes": "Barbarzyńcy nie mogą nosić zbroi podczas szału (AC = 10 + DEX + CON).",
            },
            {
                "id": "barb_b",
                "label": "Pakiet B: Broń bojowa 1H + Tarcza + 2x Oszczepy + Ekwipunek odkrywcy",
                "weapons": ["longsword", "javelin", "javelin"],
                "armor": "none",
                "shield": True,
                "notes": "Styl walki z tarczą daje +2 KP (AC = 10 + DEX + CON + 2).",
            },
        ]
    },
    "bard": {
        "options": [
            {
                "id": "bard_a",
                "label": "Pakiet A: Rapier + Dyplomata (Zbroja skórzana) + Instrument muzyczny",
                "weapons": ["rapier"],
                "armor": "leather",
                "shield": False,
                "notes": "Rapier + finezja pozwala używać DEX zamiast STR do ataku i obrażeń.",
            },
            {
                "id": "bard_b",
                "label": "Pakiet B: Długi miecz + Zbroja skórzana + Instrument muzyczny",
                "weapons": ["longsword"],
                "armor": "leather",
                "shield": False,
                "notes": "Styl wojownika-barda. Długi miecz (1k8) to solidna broń wszechstronna.",
            },
            {
                "id": "bard_c",
                "label": "Pakiet C: Sztylet x2 + Zbroja skórzana + Instrument muzyczny",
                "weapons": ["dagger", "dagger"],
                "armor": "leather",
                "shield": False,
                "notes": "Szybki styl Bardów skrytobójców. Finezja i lekkie sztyletki.",
            },
        ]
    },
    "cleric": {
        "options": [
            {
                "id": "cleric_a",
                "label": "Pakiet A: Buława + Łuskowa zbroja + Tarcza + Święty symbol",
                "weapons": ["mace"],
                "armor": "scale_mail",
                "shield": True,
                "notes": "Klasyczny kleryk obrońca. Wysoka KP (16+) dzięki średniej zbroi i tarczy.",
            },
            {
                "id": "cleric_b",
                "label": "Pakiet B: Topór bojowy + Kolcza + Tarcza + Święty symbol",
                "weapons": ["battleaxe"],
                "armor": "chain_mail",
                "shield": True,
                "notes": "Wojenny kleryk – uwaga: kolcza wymaga STR 13. Wysoka KP 18.",
            },
            {
                "id": "cleric_c",
                "label": "Pakiet C: Kij + Skórzana + Sztylet + Święty symbol",
                "weapons": ["quarterstaff", "dagger"],
                "armor": "leather",
                "shield": False,
                "notes": "Kleryk mistyk bez ciężkiej zbroi. Kij może działać jako wtórna ogniskowa.",
            },
        ]
    },
    "druid": {
        "options": [
            {
                "id": "druid_a",
                "label": "Pakiet A: Kij (Druidic focus) + Skóra gruba + Tarcza + Torba podróżna",
                "weapons": ["quarterstaff"],
                "armor": "hide",
                "shield": True,
                "notes": "Druidzi nie mogą nosić metalowej zbroi ani tarcz. Kij służy jako ogniskowa druida.",
            },
            {
                "id": "druid_b",
                "label": "Pakiet B: Scimitar + Skóra gruba + Torba podróżna",
                "weapons": ["scimitar"],
                "armor": "hide",
                "shield": False,
                "notes": "Scimitar (sierp bojowy) to finezja + lekka – idealne do Druidów Księżyca walczących wręcz.",
            },
        ]
    },
    "fighter": {
        "options": [
            {
                "id": "fighter_a",
                "label": "Pakiet A: Kolcza + Długi miecz + Tarcza + Lekka kusza + 20 bełtów",
                "weapons": ["longsword", "light_crossbow"],
                "armor": "chain_mail",
                "shield": True,
                "notes": "Klasyczny wojownik tarczowy. KP 18 (kolcza+tarcza). Kusza jako dystansowa opcja.",
            },
            {
                "id": "fighter_b",
                "label": "Pakiet B: Skóra ćwiekowana + Wielki miecz + Lekka kusza + 20 bełtów",
                "weapons": ["greatsword", "light_crossbow"],
                "armor": "studded_leather",
                "shield": False,
                "notes": "Wojownik dwuręczny. Wielki miecz 2k6 to duże obrażenia. Styl: Great Weapon Fighting.",
            },
            {
                "id": "fighter_c",
                "label": "Pakiet C: Kolcza + Topór bojowy + Tarcza + Ręczna kusza",
                "weapons": ["battleaxe", "hand_crossbow"],
                "armor": "chain_mail",
                "shield": True,
                "notes": "Pancerny wojownik z toporem. Ręczna kusza pozwala na szybki strzał w Akcji Bonusowej.",
            },
        ]
    },
    "monk": {
        "options": [
            {
                "id": "monk_a",
                "label": "Pakiet A: Krótki miecz + 10x Dart + Zestaw klasztorny",
                "weapons": ["shortsword", "dagger"],
                "armor": "none",
                "shield": False,
                "notes": "Mnich nie korzysta ze zbroi (AC = 10 + DEX + WIS). Krótki miecz to standardowa broń mnicha.",
            },
            {
                "id": "monk_b",
                "label": "Pakiet B: Prosta broń (Kij) + 10x Dart + Zestaw odkrywcy",
                "weapons": ["quarterstaff", "dagger"],
                "armor": "none",
                "shield": False,
                "notes": "Kij dwuręczny (1k8) lub jednoręczny (1k6) – idealne dla Drogi Otwartej Dłoni.",
            },
        ]
    },
    "paladin": {
        "options": [
            {
                "id": "paladin_a",
                "label": "Pakiet A: Kolcza + Długi miecz + Tarcza + 5x Oszczepy + Święty symbol",
                "weapons": ["longsword", "javelin"],
                "armor": "chain_mail",
                "shield": True,
                "notes": "Kolcza wymaga STR 13. Zapewnia wysoką obronę (KP 16 + 2 z tarczy).",
            },
            {
                "id": "paladin_b",
                "label": "Pakiet B: Kolcza + Wielki miecz + 5x Oszczepy + Święty symbol",
                "weapons": ["greatsword", "javelin"],
                "armor": "chain_mail",
                "shield": False,
                "notes": "Paladyn dwuręczny. Wielki miecz + Boskie Uderzenie = ogromne obrażenia.",
            },
        ]
    },
    "ranger": {
        "options": [
            {
                "id": "ranger_a",
                "label": "Pakiet A: Łuskowa + Krótki miecz x2 + Długi łuk + 20 strzał",
                "weapons": ["shortsword", "shortsword", "longbow"],
                "armor": "scale_mail",
                "shield": False,
                "notes": "Styl Dwóch Broni. Dwa krótkie miecze (1k6 + 1k6) i łuk długodystansowy.",
            },
            {
                "id": "ranger_b",
                "label": "Pakiet B: Łuskowa + Długi miecz + Długi łuk + 20 strzał",
                "weapons": ["longsword", "longbow"],
                "armor": "scale_mail",
                "shield": False,
                "notes": "Zbalansowany łucznik. Długi miecz do walki wręcz, łuk do dystansowej.",
            },
        ]
    },
    "rogue": {
        "options": [
            {
                "id": "rogue_a",
                "label": "Pakiet A: Ćwiekowana skóra + Rapier + Krótki łuk + 20 strzał + Sztylet",
                "weapons": ["rapier", "shortbow", "dagger"],
                "armor": "studded_leather",
                "shield": False,
                "notes": "Rapier finezją + DEX do ataku. Krótki łuk do ataków z dystansu. Sztylet do kryjobójcy.",
            },
            {
                "id": "rogue_b",
                "label": "Pakiet B: Ćwiekowana skóra + Krótki miecz x2 + Sztylet x2",
                "weapons": ["shortsword", "shortsword", "dagger", "dagger"],
                "armor": "studded_leather",
                "shield": False,
                "notes": "Styl Dwóch Broni. Dwa Krótkie Miecze (1k6) z finezją – idealne do Łotrzyka Arcane Trickster.",
            },
        ]
    },
    "sorcerer": {
        "options": [
            {
                "id": "sorc_a",
                "label": "Pakiet A: Lekka kusza + 20 bełtów + Sztylet + Różdżka czarodziejska (ogniskowa)",
                "weapons": ["light_crossbow", "dagger"],
                "armor": "none",
                "shield": False,
                "notes": "Czarodnicy nie mają biegłości ze zbrojami. Kusza daje opcję dystansową zanim nabierzesz poziomów.",
            },
            {
                "id": "sorc_b",
                "label": "Pakiet B: 2x Sztylet + Laska czarodziejska (ogniskowa)",
                "weapons": ["dagger", "dagger", "quarterstaff"],
                "armor": "none",
                "shield": False,
                "notes": "Laska jako ogniskowa i broń defensywna. Sztylet do sytuacji awaryjnych.",
            },
        ]
    },
    "warlock": {
        "options": [
            {
                "id": "warlock_a",
                "label": "Pakiet A: Lekka kusza + 20 bełtów + Skórzana + Sztylet + Ogniskowa paktowa",
                "weapons": ["light_crossbow", "dagger"],
                "armor": "leather",
                "shield": False,
                "notes": "Warlock ma biegłość z lekką zbroją. Kusza do ataku zanim użyjesz Niesamowitego Uderzenia.",
            },
            {
                "id": "warlock_b",
                "label": "Pakiet B: Prosta broń (Kij) x2 + Skórzana + Ogniskowa paktowa",
                "weapons": ["quarterstaff", "dagger"],
                "armor": "leather",
                "shield": False,
                "notes": "Kij jako mistyczna laska + Pakt Ostrza pozwala walczyć wręcz z magią.",
            },
        ]
    },
    "wizard": {
        "options": [
            {
                "id": "wizard_a",
                "label": "Pakiet A: Kij + Sztylet + Zestaw ucznia + Spellbook + Ogniskowa (Kryształowa kula)",
                "weapons": ["quarterstaff", "dagger"],
                "armor": "none",
                "shield": False,
                "notes": "Czarodziejska klasyka. Kij jako ogniskowa i broń. Żadnej zbroi – polegasz na magii.",
            },
            {
                "id": "wizard_b",
                "label": "Pakiet B: Lekka kusza + 20 bełtów + Sztylet + Spellbook + Różdżka (ogniskowa)",
                "weapons": ["light_crossbow", "dagger"],
                "armor": "none",
                "shield": False,
                "notes": "Czarodziej z kuszą jako backup. Lekka kusza przy biegłości daje 1k8 obrażeń.",
            },
        ]
    },
}

# PHB 2014 starting wealth: number of d4s multiplied by gp per die.
STARTING_GOLD_RULES = {
    "barbarian": {"dice": 2, "multiplier": 10, "phb": True},
    "bard": {"dice": 5, "multiplier": 10, "phb": True},
    "cleric": {"dice": 5, "multiplier": 10, "phb": True},
    "druid": {"dice": 2, "multiplier": 10, "phb": True},
    "fighter": {"dice": 5, "multiplier": 10, "phb": True},
    "monk": {"dice": 5, "multiplier": 1, "phb": True},
    "paladin": {"dice": 5, "multiplier": 10, "phb": True},
    "ranger": {"dice": 5, "multiplier": 10, "phb": True},
    "rogue": {"dice": 4, "multiplier": 10, "phb": True},
    "sorcerer": {"dice": 3, "multiplier": 10, "phb": True},
    "warlock": {"dice": 4, "multiplier": 10, "phb": True},
    "wizard": {"dice": 4, "multiplier": 10, "phb": True},
    # Artificer is not a PHB 2014 class; use the common 5d4 x 10 gp option.
    "artificer": {"dice": 5, "multiplier": 10, "phb": False},
}

_WEAPON_PRICES_CP = {
    "club": 10, "dagger": 200, "greatclub": 20, "handaxe": 500,
    "javelin": 50, "light_hammer": 200, "mace": 500,
    "quarterstaff": 20, "spear": 100, "scimitar": 2500,
    "sickle": 100, "light_crossbow": 2500, "shortbow": 2500,
    "battleaxe": 1000, "flail": 1000, "glaive": 2000,
    "greataxe": 3000, "greatsword": 5000, "longsword": 1500,
    "maul": 1000, "rapier": 2500, "shortsword": 1000,
    "trident": 500, "warhammer": 1500, "hand_crossbow": 7500,
    "heavy_crossbow": 5000, "longbow": 5000,
}

_ARMOR_PRICES_CP = {
    "padded": 500, "leather": 1000, "studded_leather": 4500,
    "hide": 1000, "chain_shirt": 5000, "scale_mail": 5000,
    "breastplate": 40000, "half_plate": 75000, "ring_mail": 3000,
    "chain_mail": 7500, "splint": 20000, "plate": 150000,
}

SHOP_ITEMS = {
    **{
        item_id: {
            "name": item["name"],
            "category": "Broń wojenna" if "bojowa" in item.get("profs", []) else "Broń prosta",
            "kind": "weapon",
            "price_cp": _WEAPON_PRICES_CP[item_id],
        }
        for item_id, item in WEAPONS.items()
    },
    **{
        item_id: {"name": item["name"], "category": "Zbroje", "kind": "armor", "price_cp": _ARMOR_PRICES_CP[item_id]}
        for item_id, item in ARMORS.items()
        if item_id in _ARMOR_PRICES_CP
    },
    "shield": {"name": ARMORS["shield"]["name"], "category": "Zbroje", "kind": "shield", "price_cp": 1000},
}

SHOP_ITEMS.update({
    item_id: {"name": name, "category": category, "kind": "ammo" if category == "Amunicja" else "weapon", "price_cp": price_cp}
    for item_id, name, category, price_cp in [
        ("dart", "Strzałka", "Broń prosta", 5),
        ("sling", "Proca", "Broń prosta", 10),
        ("blowgun", "Dmuchawka", "Broń wojenna", 1000),
        ("lance", "Lanca", "Broń wojenna", 1000),
        ("morningstar", "Korbacz", "Broń wojenna", 1500),
        ("pike", "Pika", "Broń wojenna", 500),
        ("war_pick", "Kilof bojowy", "Broń wojenna", 500),
        ("whip", "Bicz", "Broń wojenna", 200),
        ("net", "Sieć", "Broń wojenna", 100),
        ("arrows", "Strzały (20 szt.)", "Amunicja", 100),
        ("crossbow_bolts", "Bełty (20 szt.)", "Amunicja", 100),
        ("sling_bullets", "Pociski do procy (20 szt.)", "Amunicja", 4),
        ("blowgun_needles", "Igły do dmuchawki (50 szt.)", "Amunicja", 100),
    ]
})

_ADVENTURING_GEAR = {
    "backpack": ("Plecak", 200),
    "ball_bearings": ("Kulki metalowe (woreczek)", 100),
    "bedroll": ("Rolka posłania", 100),
    "bell": ("Dzwonek", 100),
    "block_and_tackle": ("Blok i talia", 100),
    "blanket": ("Koc", 50),
    "book": ("Książka", 2500),
    "bottle_glass": ("Szklana butelka", 2),
    "bucket": ("Wiadro", 5),
    "caltrops": ("Kolce, woreczek", 100),
    "candle": ("Świeca", 1),
    "case_crossbow_bolts": ("Pojemnik na bełty", 100),
    "case_map": ("Pojemnik na mapę lub zwój", 100),
    "chain_10ft": ("Łańcuch (3 m)", 500),
    "chalk": ("Kreda", 1),
    "chest": ("Skrzynia", 500),
    "climbers_kit": ("Zestaw wspinaczkowy", 2500),
    "clothes_common": ("Ubranie zwykłe", 50),
    "clothes_costume": ("Kostium", 500),
    "clothes_fine": ("Ubranie wytworne", 1500),
    "clothes_travelers": ("Ubranie podróżne", 200),
    "component_pouch": ("Sakiewka na komponenty", 2500),
    "crowbar": ("Łom", 200),
    "disguise_kit": ("Zestaw do charakteryzacji", 2500),
    "fishing_tackle": ("Sprzęt wędkarski", 100),
    "flask": ("Piersiówka", 2),
    "forgery_kit": ("Zestaw fałszerski", 1500),
    "grappling_hook": ("Kotwiczka", 200),
    "healers_kit": ("Zestaw uzdrowiciela", 500),
    "holy_symbol": ("Święty symbol", 500),
    "hunting_trap": ("Pułapka myśliwska", 500),
    "ink": ("Tusz (butelka 30 ml)", 1000),
    "ink_pen": ("Pióro", 2),
    "ladder": ("Drabina (3 m)", 10),
    "lantern": ("Latarnia z osłoną", 500),
    "lock": ("Zamek", 1000),
    "manacles": ("Kajdanki", 200),
    "map": ("Mapa", 5000),
    "map_case": ("Pojemnik na mapę", 100),
    "magnifying_glass": ("Szkło powiększające", 10000),
    "mess_kit": ("Menażka", 20),
    "mirror": ("Lusterko stalowe", 500),
    "oil_flask": ("Oliwa (bukłak)", 10),
    "paper": ("Papier (arkusz)", 20),
    "parchment": ("Pergamin (arkusz)", 10),
    "perfume": ("Perfumy (fiolka)", 500),
    "piton": ("Hak", 5),
    "playing_card_set": ("Talia kart", 50),
    "pole": ("Żerdź (3 m)", 5),
    "pouch": ("Sakiewka", 50),
    "quiver": ("Kołczan", 100),
    "rations": ("Racje żywnościowe (1 dzień)", 50),
    "ram_portable": ("Taranujący drąg", 400),
    "rope_hempen": ("Lina konopna (15 m)", 100),
    "rope_silk": ("Lina jedwabna (15 m)", 1000),
    "sack": ("Worek", 1),
    "scale_merchants": ("Waga kupiecka", 100),
    "seal_wax": ("Lak", 50),
    "shovel": ("Łopata", 200),
    "signal_whistle": ("Gwizdek sygnałowy", 5),
    "signet_ring": ("Pierścień sygnetowy", 500),
    "soap": ("Mydło", 2),
    "spellbook": ("Księga czarów", 5000),
    "spyglass": ("Luneta", 100000),
    "tent_four_person": ("Namiot czteroosobowy", 200),
    "tent": ("Namiot dwuosobowy", 200),
    "tinderbox": ("Krzesiwo", 50),
    "torch": ("Pochodnia", 1),
    "waterskin": ("Bukłak", 20),
    "whetstone": ("Osełka", 1),
    "thieves_tools": ("Narzędzia złodziejskie", 2500),
    "herbalism_kit": ("Zestaw zielarski", 500),
    "smith_tools": ("Narzędzia kowalskie", 2000),
    "alchemist_supplies": ("Narzędzia alchemika", 5000),
    "brewer_supplies": ("Narzędzia piwowara", 2000),
    "calligrapher_supplies": ("Narzędzia kaligrafa", 1000),
    "carpenter_tools": ("Narzędzia cieśli", 800),
    "cartographer_tools": ("Narzędzia kartografa", 1500),
    "cobbler_tools": ("Narzędzia szewca", 500),
    "cook_utensils": ("Przybory kuchenne", 100),
    "glassblower_tools": ("Narzędzia szklarza", 3000),
    "jeweler_tools": ("Narzędzia jubilera", 2500),
    "leatherworker_tools": ("Narzędzia kaletnika", 500),
    "mason_tools": ("Narzędzia murarza", 1000),
    "painter_tools": ("Narzędzia malarza", 1000),
    "potter_tools": ("Narzędzia garncarza", 1000),
    "tinker_tools": ("Narzędzia majsterkowicza", 500),
    "weaver_tools": ("Narzędzia tkacza", 100),
    "woodcarver_tools": ("Narzędzia rzeźbiarza w drewnie", 100),
    "poisoners_kit": ("Zestaw truciciela", 5000),
    "navigators_tools": ("Narzędzia nawigatora", 2500),
    "arcane_focus_crystal": ("Kryształ (ogniskowa)", 1000),
    "arcane_focus_wand": ("Różdżka (ogniskowa)", 1000),
    "arcane_focus_staff": ("Laska (ogniskowa)", 500),
    "arcane_focus_orb": ("Kula (ogniskowa)", 2000),
    "druidic_focus": ("Ogniskowa druida", 500),
    "musical_instrument": ("Instrument muzyczny", 1000),
    "bagpipes": ("Dudy", 3000),
    "drum": ("Bęben", 600),
    "dulcimer": ("Cymbały", 2500),
    "flute": ("Flet", 200),
    "lute": ("Lutnia", 3500),
    "lyre": ("Lira", 3000),
    "horn": ("Róg", 300),
    "pan_flute": ("Fletnia Pana", 1200),
    "shawm": ("Szałamaja", 200),
    "viol": ("Wiola", 3000),
    "explorers_pack": ("Zestaw odkrywcy", 1000),
    "dungeoneers_pack": ("Zestaw podziemny", 1200),
    "priests_pack": ("Zestaw kapłański", 1900),
    "scholars_pack": ("Zestaw uczonego", 4000),
    "burglars_pack": ("Zestaw włamywacza", 1600),
}

SHOP_ITEMS.update({
    item_id: {"name": name, "category": "Wyposażenie i narzędzia", "kind": "gear", "price_cp": price_cp}
    for item_id, (name, price_cp) in _ADVENTURING_GEAR.items()
})

_GEAR_DESCRIPTIONS = {
    "backpack": "Przenosi i porządkuje wyposażenie podczas podróży.",
    "ball_bearings": "Rozsyp je na podłodze, by utrudnić poruszanie się po obszarze.",
    "bedroll": "Pozwala wygodnie przespać się w terenie.",
    "bell": "Dzwoni po poruszeniu; może służyć jako prosty alarm.",
    "block_and_tackle": "Zestaw bloczków ułatwiający podnoszenie ciężkich ładunków.",
    "blanket": "Chroni przed zimnem podczas odpoczynku.",
    "book": "Zapisuj w niej notatki, wiedzę lub informacje z przygód.",
    "bottle_glass": "Szklane naczynie do przechowywania płynów.",
    "bucket": "Naczynie do przenoszenia wody i innych materiałów.",
    "caltrops": "Rozsypane na ziemi ranią i spowalniają przechodzące istoty.",
    "candle": "Daje niewielkie światło przez krótki czas.",
    "case_crossbow_bolts": "Chroni i przenosi bełty do kuszy.",
    "case_map": "Chroni mapy i zwoje przed zniszczeniem.",
    "chain_10ft": "Solidny łańcuch do mocowania, zamykania lub krępowania.",
    "chalk": "Służy do oznaczania ścian, drogi i przedmiotów.",
    "chest": "Pojemnik do przechowywania większych przedmiotów.",
    "climbers_kit": "Sprzęt do asekuracji i wspinania się po trudnym terenie.",
    "clothes_common": "Zwykłe ubranie odpowiednie do codziennego noszenia.",
    "clothes_costume": "Przebranie przydatne podczas występów i kamuflażu.",
    "clothes_fine": "Elegancki strój na uroczystości i spotkania towarzyskie.",
    "clothes_travelers": "Wytrzymałe ubranie przeznaczone do podróży.",
    "component_pouch": "Przechowuje niemagiczne komponenty do rzucania zaklęć.",
    "crowbar": "Ułatwia podważanie zamkniętych drzwi i ciężkich przedmiotów.",
    "disguise_kit": "Pozwala zmienić wygląd postaci za pomocą makijażu i rekwizytów.",
    "fishing_tackle": "Zestaw przyborów do łowienia ryb.",
    "flask": "Małe naczynie do przenoszenia napoju.",
    "forgery_kit": "Służy do kopiowania dokumentów i tworzenia fałszywek.",
    "grappling_hook": "Można zaczepić go o krawędź i użyć do wspinaczki linowej.",
    "healers_kit": "Zawiera bandaże i środki do opatrywania ran bez testu Medycyny.",
    "holy_symbol": "Kapłan może użyć go jako ogniska rzucania zaklęć.",
    "hunting_trap": "Unieruchamia stworzenie, które uruchomi mechanizm pułapki.",
    "ink": "Atrament do pisania i sporządzania dokumentów.",
    "ink_pen": "Pióro do pisania przy użyciu atramentu.",
    "ladder": "Pomaga dostać się na wyższe powierzchnie.",
    "lantern": "Oświetla otoczenie; osłona pozwala ograniczyć lub skierować światło.",
    "lock": "Zabezpiecza drzwi, skrzynię lub inny przedmiot przed otwarciem.",
    "manacles": "Krępują ręce lub nogi schwytanej istoty.",
    "map": "Pomaga nawigować i odnaleźć miejsca w odwiedzanym regionie.",
    "map_case": "Chroni mapę lub zwój podczas podróży.",
    "magnifying_glass": "Powiększa drobne szczegóły podczas oględzin.",
    "mess_kit": "Podstawowe naczynia do przygotowania i spożycia posiłku.",
    "mirror": "Pozwala obserwować zza rogu i sprawdzać trudno dostępne miejsca.",
    "oil_flask": "Paliwo do lampy; rozlana oliwa może też podtrzymać ogień.",
    "paper": "Arkusz do sporządzania notatek i dokumentów.",
    "parchment": "Trwalszy arkusz do zapisywania wiadomości lub map.",
    "perfume": "Zapach używany do pielęgnacji lub jako element przebrania.",
    "piton": "Metalowy hak do mocowania liny podczas wspinaczki.",
    "playing_card_set": "Talia do gier i hazardu.",
    "pole": "Długi drąg do sprawdzania podłoża i dosięgania odległych miejsc.",
    "pouch": "Mały woreczek na monety lub drobne przedmioty.",
    "quiver": "Przenosi strzały i ułatwia sięganie po amunicję.",
    "rations": "Porcja trwałej żywności na jeden dzień podróży.",
    "ram_portable": "Pozwala kilku osobom wyważać zamknięte drzwi.",
    "rope_hempen": "Lina do wspinaczki, wiązania i mocowania ładunków.",
    "rope_silk": "Lekka, wytrzymała lina do wspinaczki i mocowania.",
    "sack": "Prosty worek do przenoszenia przedmiotów.",
    "scale_merchants": "Pozwala ważyć towary i szacować ich ilość.",
    "seal_wax": "Lak do zabezpieczania listów pieczęcią.",
    "shovel": "Umożliwia kopanie ziemi i przenoszenie urobku.",
    "signal_whistle": "Głośny gwizdek do alarmowania i sygnalizowania.",
    "signet_ring": "Pierścień z herbem lub znakiem, używany do identyfikacji i pieczętowania.",
    "soap": "Do mycia ciała i przedmiotów.",
    "spellbook": "Księga czarodzieja do zapisywania znanych zaklęć.",
    "spyglass": "Pozwala obserwować odległe obiekty z bliska.",
    "tent_four_person": "Schronienie dla grupy podczas noclegu w terenie.",
    "tent": "Schronienie dla dwóch osób podczas noclegu w terenie.",
    "tinderbox": "Zestaw do rozpalania ognia.",
    "torch": "Przenośne źródło światła, które można trzymać w dłoni.",
    "waterskin": "Przenosi wodę pitną podczas podróży.",
    "whetstone": "Służy do ostrzenia broni i narzędzi.",
    "thieves_tools": "Przybory do otwierania zamków i rozbrajania pułapek.",
    "herbalism_kit": "Narzędzia do rozpoznawania i przygotowywania ziół.",
    "smith_tools": "Narzędzia do obróbki i naprawy metalowych przedmiotów.",
    "alchemist_supplies": "Naczynia i składniki do eksperymentów alchemicznych.",
    "poisoners_kit": "Przybory do przygotowywania i rozpoznawania trucizn.",
    "navigators_tools": "Przyrządy do wyznaczania kursu i nawigacji.",
    "arcane_focus_crystal": "Kryształ służący za ognisko rzucania zaklęć.",
    "arcane_focus_wand": "Różdżka służąca za ognisko rzucania zaklęć.",
    "arcane_focus_staff": "Laska służąca za ognisko rzucania zaklęć.",
    "arcane_focus_orb": "Kula służąca za ognisko rzucania zaklęć.",
    "druidic_focus": "Ognisko druida, na przykład gałązka jemioły lub drewniany totem.",
    "musical_instrument": "Instrument do wykonywania muzyki i występów.",
    "explorers_pack": "Zestaw podróżny z podstawowym wyposażeniem eksploracyjnym.",
    "dungeoneers_pack": "Zestaw do eksploracji podziemi, z liną, światłem i narzędziami.",
    "priests_pack": "Zestaw podróżny z wyposażeniem przydatnym kapłanowi.",
    "scholars_pack": "Zestaw do prowadzenia notatek i pracy badawczej.",
    "burglars_pack": "Zestaw do skradania się, wspinaczki i forsowania przeszkód.",
    "arrows": "Amunicja do łuku; zestaw zawiera 20 strzał.",
    "crossbow_bolts": "Amunicja do kuszy; zestaw zawiera 20 bełtów.",
    "sling_bullets": "Amunicja do procy; zestaw zawiera 20 pocisków.",
    "blowgun_needles": "Amunicja do dmuchawki; zestaw zawiera 50 igieł.",
    "dart": "Broń dystansowa: 1k4 obrażeń kłutych, zasięg 6/18 m.",
    "sling": "Broń dystansowa: 1k4 obrażeń obuchowych, zasięg 9/36 m; wymaga pocisków.",
    "blowgun": "Broń dystansowa: 1 obrażenie kłute, zasięg 7,5/30 m; wymaga igieł.",
    "lance": "Broń: 1k12 obrażeń kłutych, zasięg; ma utrudnienie przy ataku na cel w odległości 1,5 m.",
    "morningstar": "Broń: 1k8 obrażeń kłutych w walce wręcz.",
    "pike": "Broń dwuręczna z zasięgiem: 1k10 obrażeń kłutych.",
    "war_pick": "Broń: 1k8 obrażeń kłutych w walce wręcz.",
    "whip": "Broń z finezją i zasięgiem: 1k4 obrażeń siecznych.",
    "net": "Trafiona istota zostaje unieruchomiona do czasu oswobodzenia lub przecięcia sieci.",
    "bagpipes": "Instrument dęty do wykonywania muzyki i występów.",
    "drum": "Instrument perkusyjny do wykonywania muzyki i występów.",
    "dulcimer": "Instrument strunowy do wykonywania muzyki i występów.",
    "flute": "Instrument dęty do wykonywania muzyki i występów.",
    "lute": "Instrument strunowy do wykonywania muzyki i występów.",
    "lyre": "Instrument strunowy do wykonywania muzyki i występów.",
    "horn": "Instrument dęty do wykonywania muzyki i sygnalizowania.",
    "pan_flute": "Instrument dęty do wykonywania muzyki i występów.",
    "shawm": "Instrument dęty do wykonywania muzyki i występów.",
    "viol": "Instrument smyczkowy do wykonywania muzyki i występów.",
    "brewer_supplies": "Narzędzia do warzenia i oceny jakości napojów.",
    "calligrapher_supplies": "Przybory do kaligrafowania i ozdobnego pisma.",
    "carpenter_tools": "Narzędzia do cięcia i obróbki drewna.",
    "cartographer_tools": "Przybory do tworzenia i odczytywania map.",
    "cobbler_tools": "Narzędzia do naprawy i wytwarzania obuwia.",
    "cook_utensils": "Przybory do przygotowywania i gotowania posiłków.",
    "glassblower_tools": "Narzędzia do kształtowania i naprawy szkła.",
    "jeweler_tools": "Narzędzia do oceny i obróbki klejnotów oraz biżuterii.",
    "leatherworker_tools": "Narzędzia do obróbki skóry i wytwarzania skórzanych przedmiotów.",
    "mason_tools": "Narzędzia do obróbki kamienia i prac murarskich.",
    "painter_tools": "Przybory do malowania i tworzenia obrazów.",
    "potter_tools": "Narzędzia do formowania i wypalania naczyń z gliny.",
    "tinker_tools": "Przybory do konstruowania i naprawiania drobnych mechanizmów.",
    "weaver_tools": "Narzędzia do tkania materiałów.",
    "woodcarver_tools": "Narzędzia do rzeźbienia i obróbki drewna.",
}

for item_id, item in SHOP_ITEMS.items():
    if item["kind"] == "weapon" and item_id in WEAPONS:
        weapon = WEAPONS[item_id]
        item["description"] = f"{weapon['damage']} obrażeń {weapon['type']}; {weapon.get('props', weapon.get('range', 'broń do walki'))}."
    elif item["kind"] == "armor" and item_id in ARMORS:
        armor = ARMORS[item_id]
        item["description"] = armor.get("notes") or f"Zbroja {armor['type']}; bazowa KP {armor['ac']}."
    elif item["kind"] == "shield":
        item["description"] = "Daje +2 do KP, gdy jest trzymana w jednej ręce."
    else:
        item["description"] = _GEAR_DESCRIPTIONS.get(item_id, "Amunicja lub wyposażenie użytkowe przeznaczone do użycia z odpowiednią bronią.")
