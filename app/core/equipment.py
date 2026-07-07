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
