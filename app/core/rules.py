"""
D&D 5e Core Data - Rules compliant character creation data.
Based on D&D 5th Edition Player's Handbook.
"""

RACES = {
    "human": {
        "name": "Człowiek",
        "name_en": "Human",
        "speed": 9,
        "size": "Średni",
        "traits": ["Dodatkowy język"],
        "asi": {"str": 1, "dex": 1, "con": 1, "int": 1, "wis": 1, "cha": 1},
        "description": "Ludzie są innowatorami i pionierami w świecie D&D.",
        "subraces": {},
        "darkvision": False,
        "languages": ["Wspólny", "+ 1 do wyboru"],
    },
    "human_variant": {
        "name": "Człowiek (Wariant)",
        "name_en": "Human (Variant)",
        "speed": 9,
        "size": "Średni",
        "traits": ["Dodatkowy język", "Wybierz 1 dodatkową biegłość"],
        "asi": {},
        "description": "Wariant człowieka pozwala wziąć od razu 1 atut oraz dodać 1 punkt do dwóch dowolnych statystyk (punkty ASI).",
        "subraces": {},
        "darkvision": False,
        "languages": ["Wspólny", "+ 1 do wyboru"],
    },
    "elf_high": {
        "name": "Elf Wysoki",
        "name_en": "High Elf",
        "asi": {"dex": 2, "int": 1},
        "speed": 9,
        "size": "Średni",
        "traits": [
            "Mroczne widzenie (18m)",
            "Rodowód fey: Przewaga vs zauroczeniom, odporność na magiczny sen",
            "Trans (4 godziny odpoczynku)",
            "Biegłość w broni palnej (elfy): Długi miecz, krótki miecz, krótki łuk, długi łuk",
            "Dodatkowa sztuczka (oparta na Inteligencji)",
            "Dodatkowy język"
        ],
        "languages": ["Wspólny", "Elficki", "+ 1 do wyboru"],
        "darkvision": True,
        "description": "Elegancka i długowieczna rasa z powinowactwem do magii.",
        "subraces": {},
    },
    "elf_wood": {
        "name": "Elf Leśny",
        "name_en": "Wood Elf",
        "asi": {"dex": 2, "wis": 1},
        "speed": 10.5,
        "size": "Średni",
        "traits": [
            "Mroczne widzenie (18m)",
            "Rodowód fey: Przewaga vs zauroczeniom, odporność na magiczny sen",
            "Trans (4 godziny odpoczynku)",
            "Biegłość w broni palnej (elfy): Długi miecz, krótki miecz, krótki łuk, długi łuk",
            "Zwinność lasu: Możesz się ukryć będąc tylko lekko przysłoniętym przez naturę"
        ],
        "languages": ["Wspólny", "Elficki"],
        "darkvision": True,
        "description": "Zwinna rasa elfów żyjących w harmonii z naturą.",
        "subraces": {},
    },
    "dwarf_hill": {
        "name": "Krasnolud Górski",
        "name_en": "Hill Dwarf",
        "asi": {"con": 2, "wis": 1},
        "speed": 7.5,
        "size": "Średni",
        "traits": [
            "Mroczne widzenie (18m)",
            "Odporność krasnoludów: Przewaga vs trucizny, odporność na trucizny",
            "Wyczucie kamienia: Biegłość w historii dot. kamienia, x2 premię za biegłość",
            "Waleczność: Biegłość w bojowym toporze, ręcznym toporze, lekkim młocie, młocie bojowym",
            "Narzędzia: Biegłość w wybranych narzędziach rzemieślniczych",
            "Wytrwałość krasnoludów (nie spowalnia ich zbroja)",
            "Wytrzymałość wzgórza: +1 max PW za poziom"
        ],
        "languages": ["Wspólny", "Krasnoludzki"],
        "darkvision": True,
        "description": "Odporne krasnoludy wzgórz, słynne z wytrzymałości i mądrości.",
        "subraces": {},
    },
    "dwarf_mountain": {
        "name": "Krasnolud Górski (Góry)",
        "name_en": "Mountain Dwarf",
        "asi": {"con": 2, "str": 2},
        "speed": 7.5,
        "size": "Średni",
        "traits": [
            "Mroczne widzenie (18m)",
            "Odporność krasnoludów",
            "Wyczucie kamienia",
            "Waleczność krasnoludów",
            "Narzędzia krasnoludzkie",
            "Wytrwałość krasnoludów",
            "Górska zbroja: Biegłość w lekkiej i średniej zbroi",
        ],
        "languages": ["Wspólny", "Krasnoludzki"],
        "darkvision": True,
        "description": "Potężne krasnoludy górskie, waleczne i silne.",
        "subraces": {},
    },
    "halfling_lightfoot": {
        "name": "Niziołek Zwinniec",
        "name_en": "Lightfoot Halfling",
        "asi": {"dex": 2, "cha": 1},
        "speed": 7.5,
        "size": "Mały",
        "traits": [
            "Szczęście: Ponów k20 jeśli wypadnie 1",
            "Nieustraszony: Przewaga vs strachu",
            "Zwinność niziołków: Możesz przejść przez pole stworzenia większego od ciebie",
            "Naturalna skrytość: Ukryj się za stworzeniem większym od ciebie",
        ],
        "languages": ["Wspólny", "Niziołkowy"],
        "darkvision": False,
        "description": "Mali i zwinni, niziołki zwinńcy są mistrzami dyskrecji.",
        "subraces": {},
    },
    "halforc": {
        "name": "Pół-Ork",
        "name_en": "Half-Orc",
        "asi": {"str": 2, "con": 1},
        "speed": 9,
        "size": "Średni",
        "traits": [
            "Mroczne widzenie (18m)",
            "Groźny: Biegłość w zastraszaniu",
            "Brutalne ataki: +1k8 do trafień krytycznych bronią",
            "Nieustępliwość: 1x/długi odpoczynek, gdy spadniesz do 0 PW, możesz pozostać przy 1 PW",
        ],
        "languages": ["Wspólny", "Orczański"],
        "darkvision": True,
        "description": "Silny i wytrzymały potomek człowieka i orka.",
        "subraces": {},
    },
    "tiefling": {
        "name": "Tiefling",
        "name_en": "Tiefling",
        "asi": {"int": 1, "cha": 2},
        "speed": 9,
        "size": "Średni",
        "traits": [
            "Mroczne widzenie (18m)",
            "Piekielne dziedzictwo: Odporność na ogień",
            "Zaklęcia (Cha): Thaumaturgy (1 lvl), Hellish Rebuke (3 lvl), Darkness (5 lvl)"
        ],
        "languages": ["Wspólny", "Piekielny"],
        "darkvision": True,
        "description": "Istoty piekielnego pochodzenia o mrocznym uroku i magii.",
        "subraces": {},
    },
    "dragonborn": {
        "name": "Smoczorodny",
        "name_en": "Dragonborn",
        "asi": {"str": 2, "cha": 1},
        "speed": 9,
        "size": "Średni",
        "traits": [
            "Oddech smoka: Wybierz typ obrażeń, użyj jako ataku obszarowego (Con rzut obronny)",
            "Odporność na obrażenia: Typ zależny od rodowodu",
        ],
        "languages": ["Wspólny", "Smoczy"],
        "darkvision": False,
        "description": "Dumna rasa ze smoczą krwią, zdolna do ziania oddechem żywiołu.",
        "subraces": {},
    },
    "gnome_forest": {
        "name": "Gnom Leśny",
        "name_en": "Forest Gnome",
        "asi": {"int": 2, "dex": 1},
        "speed": 7.5,
        "size": "Mały",
        "traits": [
            "Mroczne widzenie (18m)",
            "Spryt gnoma: Przewaga na rzuty Int, Mdr, Cha vs magia",
            "Iluzja natury: Sztuczka Drobnych Złudzeń",
            "Rozmowa ze zwierzętami: Prosty komunikat z małymi naturalnymi zwierzętami",
        ],
        "languages": ["Wspólny", "Gnomi"],
        "darkvision": True,
        "description": "Żywiołowe i ciekawskie gnomy, zaprzyjaźnione z naturą.",
        "subraces": {},
    },
}

CLASSES = {
    "barbarian": {
        "name": "Barbarzyńca",
        "name_en": "Barbarian",
        "hit_die": 12,
        "primary_stats": ["str", "con"],
        "saving_throws": ["str", "con"],
        "armor_proficiencies": ["lekka", "średnia", "tarcze"],
        "weapon_proficiencies": ["prosta", "bojowa"],
        "num_skills": 2,
        "skill_choices": ["atletyka", "postrzeganie", "zastraszanie", "przetrwanie", "przyroda", "zwierzęta"],
        "features_1": [
            "Szał (Rage): Bonus do ataków i obrażeń od siły, odporność na obrażenia fizyczne. Użycia: 2",
            "Obrona bez pancerza: KP = 10 + modyfikator Zręczności + modyfikator Kondycji",
        ],
        "spellcasting": False,
        "description": "Dziki wojownik korzystający z prymitywnej siły i szału bojowego.",
        "subclasses": {
            "berserker": "Berserker - skupia się na szale i dodatkowych atakach",
            "totem_warrior": "Wojownik Totemu - mistyczna więź ze zwierzęciem totemicznym",
        },
        "primary_ability": "STR",
        "secondary_ability": "CON",
    },
    "bard": {
        "name": "Bard",
        "name_en": "Bard",
        "hit_die": 8,
        "primary_stats": ["cha"],
        "saving_throws": ["dex", "cha"],
        "armor_proficiencies": ["lekka"],
        "weapon_proficiencies": ["prosta", "rapier", "szpada", "krótki miecz"],
        "num_skills": 3,
        "skill_choices": "all",
        "features_1": [
            "Rzucanie zaklęć (Cha)",
            "Bardowska Inspiracja: Kostka inspiracji dla sojusznika (k6), użycia = mod Cha",
        ],
        "spellcasting": True,
        "spellcasting_stat": "cha",
        "description": "Magiczny pieśniarz czerpiący moc z muzyki i słów.",
        "subclasses": {
            "lore": "Kolegium Wiedzy - skupia się na magii i wiedzy",
            "valor": "Kolegium Waleczności - łączy magię z walką",
        },
        "primary_ability": "CHA",
    },
    "cleric": {
        "name": "Kleryk",
        "name_en": "Cleric",
        "hit_die": 8,
        "primary_stats": ["wis"],
        "saving_throws": ["wis", "cha"],
        "armor_proficiencies": ["lekka", "średnia", "tarcze"],
        "weapon_proficiencies": ["prosta"],
        "num_skills": 2,
        "skill_choices": ["historia", "medycyna", "perswazja", "religia", "wgląd"],
        "features_1": [
            "Rzucanie zaklęć (Mdr)",
            "Boska Domena: Wybierz domenę (Życia, Wiedzy, Światła, etc.)",
        ],
        "spellcasting": True,
        "spellcasting_stat": "wis",
        "description": "Kapłan boga, dysponujący boską magią i uzdrawianiem.",
        "subclasses": {
            "life": "Domena Życia - uzdrawianie i wsparcie",
            "light": "Domena Światła - ofensywna magia ognia",
        },
        "primary_ability": "WIS",
    },
    "druid": {
        "name": "Druid",
        "name_en": "Druid",
        "hit_die": 8,
        "primary_stats": ["wis"],
        "saving_throws": ["int", "wis"],
        "armor_proficiencies": ["lekka (niemagiczna)", "średnia (niemagiczna)", "tarcze (nie metalowe)"],
        "weapon_proficiencies": ["pałka", "sztylet", "dzida", "oszczep", "buława", "kij", "sierp", "proca"],
        "num_skills": 2,
        "skill_choices": ["arcana", "zwierzęta", "wgląd", "medycyna", "przyroda", "postrzeganie", "religia", "przetrwanie"],
        "features_1": [
            "Rzucanie zaklęć (Mdr)",
            "Druidzki język (druidic) - tajny język",
        ],
        "spellcasting": True,
        "spellcasting_stat": "wis",
        "description": "Strażnik natury władający magią przyrody i zdolny do przemiany.",
        "subclasses": {
            "land": "Krąg Ziemi - magia oparta na środowisku",
            "moon": "Krąg Księżyca - potężniejsza przemiana w zwierzę",
        },
        "primary_ability": "WIS",
    },
    "fighter": {
        "name": "Wojownik",
        "name_en": "Fighter",
        "hit_die": 10,
        "primary_stats": ["str", "dex"],
        "saving_throws": ["str", "con"],
        "armor_proficiencies": ["lekka", "średnia", "ciężka", "tarcze"],
        "weapon_proficiencies": ["prosta", "bojowa"],
        "num_skills": 2,
        "skill_choices": ["akrobatyka", "atletyka", "historia", "wgląd", "zastraszanie", "postrzeganie", "przetrwanie"],
        "features_1": [
            "Styl Walki: Wybierz specjalizację bojową",
            "Drugi Oddech: Ulecz 1k10 + poziom wojownika raz na krótki/długi odpoczynek",
        ],
        "spellcasting": False,
        "description": "Wszechstronny mistrz broni i technik walki.",
        "subclasses": {
            "champion": "Czempion - doskonałość fizyczna, krytyki na 19",
            "battlemaster": "Mistrz Bitewny - manewry taktyczne",
            "eldritch_knight": "Eldryczny Rycerz - wojownik z magią",
        },
        "primary_ability": "STR/DEX",
    },
    "monk": {
        "name": "Mnich",
        "name_en": "Monk",
        "hit_die": 8,
        "primary_stats": ["dex", "wis"],
        "saving_throws": ["str", "dex"],
        "armor_proficiencies": [],
        "weapon_proficiencies": ["prosta", "krótki miecz"],
        "num_skills": 2,
        "skill_choices": ["akrobatyka", "atletyka", "historia", "wgląd", "religia", "ukrycie"],
        "features_1": [
            "Nieuzbrojony: Obrona bez pancerza (10 + Zrc + Mdr)",
            "Ki: Pula punktów Ki = poziom",
            "Nieuzbrojony Atak: Bonus atak bez broni lub ki",
        ],
        "spellcasting": False,
        "description": "Ascetyczny wojownik doskonalący ciało i ducha poprzez medytację.",
        "primary_ability": "DEX/WIS",
    },
    "paladin": {
        "name": "Paladyn",
        "name_en": "Paladin",
        "hit_die": 10,
        "primary_stats": ["str", "cha"],
        "saving_throws": ["wis", "cha"],
        "armor_proficiencies": ["lekka", "średnia", "ciężka", "tarcze"],
        "weapon_proficiencies": ["prosta", "bojowa"],
        "num_skills": 2,
        "skill_choices": ["atletyka", "wgląd", "zastraszanie", "medycyna", "perswazja", "religia"],
        "features_1": [
            "Boskie Poczucie: Wykryj zło/dobro w promieniu 18m (Cha+1 razy/długi odpoczynek)",
            "Nałożenie Rąk: Lecz PW = poziom × 5 na długi odpoczynek",
        ],
        "spellcasting": True,
        "spellcasting_stat": "cha",
        "description": "Święty wojownik złączony przysięgą z boską mocą.",
        "primary_ability": "STR/CHA",
    },
    "ranger": {
        "name": "Łowca",
        "name_en": "Ranger",
        "hit_die": 10,
        "primary_stats": ["dex", "wis"],
        "saving_throws": ["str", "dex"],
        "armor_proficiencies": ["lekka", "średnia", "tarcze"],
        "weapon_proficiencies": ["prosta", "bojowa"],
        "num_skills": 3,
        "skill_choices": ["zwierzęta", "atletyka", "wgląd", "badanie", "przyroda", "postrzeganie", "ukrycie", "przetrwanie"],
        "features_1": [
            "Ulubiony Wróg: Wybierz typ wrogów, przewaga na śledzenie i wiedzę",
            "Naturalne Badanie: Wybierz typ terenu, ignorujesz trudny teren",
        ],
        "spellcasting": True,
        "spellcasting_stat": "wis",
        "description": "Strażnik dziczy, łowca i zwiadowca.",
        "primary_ability": "DEX/WIS",
    },
    "rogue": {
        "name": "Łotrzyk",
        "name_en": "Rogue",
        "hit_die": 8,
        "primary_stats": ["dex"],
        "saving_throws": ["dex", "int"],
        "armor_proficiencies": ["lekka"],
        "weapon_proficiencies": ["prosta", "ręczna kusza", "długi łuk", "rapier", "szpada", "krótki miecz"],
        "num_skills": 4,
        "skill_choices": ["akrobatyka", "atletyka", "oszustwo", "badanie", "wgląd", "zastraszanie", "postrzeganie", "wykonanie", "perswazja", "sleight_of_hand", "ukrycie"],
        "features_1": [
            "Wiedza Eksperta: x2 premię za biegłość w 2 umiejętnościach",
            "Atak Skrytobójczy: +1k6 obrażeń gdy masz przewagę lub sojusznik jest obok celu",
            "Złodziejski żargon: Tajny język złodziei",
        ],
        "spellcasting": False,
        "description": "Skryty i zwinny mistrz sztuczek, infiltracji i nagłych ataków.",
        "primary_ability": "DEX",
    },
    "sorcerer": {
        "name": "Czarnoksiężnik",
        "name_en": "Sorcerer",
        "hit_die": 6,
        "primary_stats": ["cha"],
        "saving_throws": ["con", "cha"],
        "armor_proficiencies": [],
        "weapon_proficiencies": ["sztylet", "oszczep", "proca", "kij"],
        "num_skills": 2,
        "skill_choices": ["arcana", "oszustwo", "wgląd", "zastraszanie", "perswazja", "religia"],
        "features_1": [
            "Rzucanie zaklęć (Cha)",
            "Magiczne Źródło: Wybierz źródło mocy (Smocze, Dzikie)",
        ],
        "spellcasting": True,
        "spellcasting_stat": "cha",
        "description": "Mag czerpiący moc z wrodzonego daru magicznego.",
        "primary_ability": "CHA",
    },
    "warlock": {
        "name": "Mroczny Czarnoksiężnik",
        "name_en": "Warlock",
        "hit_die": 8,
        "primary_stats": ["cha"],
        "saving_throws": ["wis", "cha"],
        "armor_proficiencies": ["lekka"],
        "weapon_proficiencies": ["prosta"],
        "num_skills": 2,
        "skill_choices": ["arcana", "oszustwo", "historia", "zastraszanie", "badanie", "przyroda", "religia"],
        "features_1": [
            "Pakt Okultystyczny: Wybierz patrona (Archfey, Fiend, Great Old One)",
            "Magia Paktu: 1 miejsce zaklęcia, odnawialne po krótkim odpoczynku",
        ],
        "spellcasting": True,
        "spellcasting_stat": "cha",
        "description": "Czarnoksiężnik, który zawarł pakt z nadnaturalną istotą.",
        "primary_ability": "CHA",
    },
    "wizard": {
        "name": "Mag",
        "name_en": "Wizard",
        "hit_die": 6,
        "primary_stats": ["int"],
        "saving_throws": ["int", "wis"],
        "armor_proficiencies": [],
        "weapon_proficiencies": ["sztylet", "rzutka", "proca", "kij", "lekka kusza"],
        "num_skills": 2,
        "skill_choices": ["arcana", "historia", "wgląd", "badanie", "medycyna", "religia"],
        "features_1": [
            "Rzucanie zaklęć (Int)",
            "Księga zaklęć: Zawiera 6 zaklęć 1 poziomu",
            "Odzysk Arcanum: Odzyskaj miejsca zaklęć po krótkim odpoczynku",
        ],
        "spellcasting": True,
        "spellcasting_stat": "int",
        "description": "Uczony mag opanowujący arkana poprzez naukę i praktykę.",
        "primary_ability": "INT",
    },
}

BACKGROUNDS = {
    "acolyte": {
        "name": "Akolita",
        "skills": ["wgląd", "religia"],
        "tools": [],
        "languages": 2,
        "equipment": ["symbol święty", "modlitewnik", "5 kadzidełek", "szaty", "15 sz złota"],
        "feature": "Schronienie wiernych: Możesz liczyć na wsparcie świątyni",
        "description": "Spędziłeś życie w służbie świątynnej.",
    },
    "criminal": {
        "name": "Przestępca",
        "skills": ["oszustwo", "ukrycie"],
        "tools": ["narzędzia do gier", "narzędzia złodzieja"],
        "languages": 0,
        "equipment": ["łom", "ciemne ubranie z kapturem", "15 sz złota"],
        "feature": "Kontakt w podziemiu: Masz kontakt, który może pomóc w kryminalnych sprawach",
        "description": "Prowadziłeś życie na skraju prawa.",
    },
    "folk_hero": {
        "name": "Bohater Ludu",
        "skills": ["obsługa zwierząt", "przetrwanie"],
        "tools": ["narzędzia rzemieślnicze", "pojazdy lądowe"],
        "languages": 0,
        "equipment": ["narzędzia rzemieślnicze", "łopata", "żelazny garnek", "ubranie wieśniaka", "10 sz złota"],
        "feature": "Schronienie ludu: Zwykli ludzie cię wspierają i ukryją",
        "description": "Wywodzisz się ze zwykłego ludu i bronisz ich spraw.",
    },
    "noble": {
        "name": "Szlachcic",
        "skills": ["historia", "perswazja"],
        "tools": ["narzędzia do gier"],
        "languages": 1,
        "equipment": ["dobre ubrania", "pierścień z sygnetu", "dokument szlachectwa", "25 sz złota"],
        "feature": "Przywilej pozycji: Twoja pozycja otwiera wiele drzwi",
        "description": "Urodzony w zamożnej i wpływowej rodzinie.",
    },
    "sage": {
        "name": "Uczony",
        "skills": ["arcana", "historia"],
        "tools": [],
        "languages": 2,
        "equipment": ["butelka atramentu", "pióro", "nóż do listów", "10 arkuszy pergaminu", "10 sz złota"],
        "feature": "Badacz: Wiesz gdzie szukać informacji, gdy ich nie znasz",
        "description": "Poświęciłeś życie zdobywaniu wiedzy.",
    },
    "soldier": {
        "name": "Żołnierz",
        "skills": ["atletyka", "zastraszanie"],
        "tools": ["narzędzia do gier", "pojazdy lądowe"],
        "languages": 0,
        "equipment": ["insygnia rangi", "trofea z bitew", "kości do gry", "zwykłe ubrania", "10 sz złota"],
        "feature": "Stopień wojskowy: Żołnierze rozpoznają twój autorytet",
        "description": "Służyłeś w armii i przeżyłeś bitwy.",
    },
    "outlander": {
        "name": "Wędrowiec",
        "skills": ["atletyka", "przetrwanie"],
        "tools": ["instrument muzyczny"],
        "languages": 1,
        "equipment": ["kij", "pułapka myśliwska", "trofea z polowania", "ubrania podróżne", "10 sz złota"],
        "feature": "Wędrownik: Doskonale znasz dzikie tereny i potrafisz znaleźć żywność",
        "description": "Wychowałeś się poza cywilizacją, w dzikich terenach.",
    },
    "entertainer": {
        "name": "Artysta",
        "skills": ["akrobatyka", "wykonanie"],
        "tools": ["instrument muzyczny", "zestaw przebrań"],
        "languages": 0,
        "equipment": ["instrument muzyczny", "przychylność fana", "kostium", "15 sz złota"],
        "feature": "Przez noc sławny: Możesz zawsze liczyć na nocleg w miejscu, gdzie grałeś",
        "description": "Rozkwitałeś na scenie i żyłeś dla oklasków.",
    },
    "hermit": {
        "name": "Pustelnik",
        "skills": ["medycyna", "religia"],
        "tools": ["zestaw ziołowy"],
        "languages": 1,
        "equipment": ["etui do pergaminu", "koc zimowy", "zestaw ziołowy", "5 sz złota"],
        "feature": "Odkrycie: Odosobnienie dało ci unikalną wiedzę lub sekret",
        "description": "Żyłeś w odosobnieniu przez długi czas.",
    },
    "guild_artisan": {
        "name": "Rzemieślnik",
        "skills": ["wgląd", "perswazja"],
        "tools": ["narzędzia rzemieślnicze"],
        "languages": 1,
        "equipment": ["narzędzia rzemieślnicze", "list polecający od gildii", "ubrania podróżne", "15 sz złota"],
        "feature": "Przynależność do gildii: Gildia zapewni ci nocleg i pomoc",
        "description": "Jesteś mistrzem rzemiosła i członkiem gildii.",
    },
}

SKILLS = {
    "akrobatyka": {"stat": "dex", "name": "Akrobatyka"},
    "zwierzęta": {"stat": "wis", "name": "Opieka nad zwierzętami"},
    "arcana": {"stat": "int", "name": "Wiedza tajemna"},
    "atletyka": {"stat": "str", "name": "Atletyka"},
    "oszustwo": {"stat": "cha", "name": "Oszustwo"},
    "historia": {"stat": "int", "name": "Historia"},
    "wgląd": {"stat": "wis", "name": "Intuicja"},
    "zastraszanie": {"stat": "cha", "name": "Zastraszanie"},
    "badanie": {"stat": "int", "name": "Badanie"},
    "medycyna": {"stat": "wis", "name": "Medycyna"},
    "przyroda": {"stat": "int", "name": "Przyroda"},
    "postrzeganie": {"stat": "wis", "name": "Percepcja"},
    "wykonanie": {"stat": "cha", "name": "Występy"},
    "perswazja": {"stat": "cha", "name": "Perswazja"},
    "religia": {"stat": "int", "name": "Religia"},
    "sleight_of_hand": {"name": "Zwinne dłonie", "name_en": "Sleight of Hand", "stat": "dex", "desc": "Sztuczki manualne, kradzież kieszonkowa."},
    "stealth": {"name": "Ukrycie", "name_en": "Stealth", "stat": "dex", "desc": "Bezszelestne poruszanie się, chowanie w cieniu."},
    "survival": {"name": "Sztuka przetrwania", "name_en": "Survival", "stat": "wis", "desc": "Tropienie, orientacja w terenie, polowanie."}
}

SPELLS = {
    "cantrip": [
        {
            "id": "acid_splash",
            "name_pl": "Rozprysk Kwasu",
            "name_en": "Acid Splash",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "chill_touch",
            "name_pl": "Trupi Dotyk",
            "name_en": "Chill Touch",
            "classes": [
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "dancing_lights",
            "name_pl": "Tańczące Światła",
            "name_en": "Dancing Lights",
            "classes": [
                "bard",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "eldritch_blast",
            "name_pl": "Niesamowite Uderzenie",
            "name_en": "Eldritch Blast",
            "classes": [
                "warlock"
            ]
        },
        {
            "id": "fire_bolt",
            "name_pl": "Ognisty Pocisk",
            "name_en": "Fire Bolt",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "guidance",
            "name_pl": "Przewodnictwo",
            "name_en": "Guidance",
            "classes": [
                "cleric",
                "druid"
            ]
        },
        {
            "id": "light",
            "name_pl": "Światło",
            "name_en": "Light",
            "classes": [
                "bard",
                "cleric",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "mage_hand",
            "name_pl": "Magiczna Dłoń",
            "name_en": "Mage Hand",
            "classes": [
                "bard",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "minor_illusion",
            "name_pl": "Drobna Iluzja",
            "name_en": "Minor Illusion",
            "classes": [
                "bard",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "prestidigitation",
            "name_pl": "Sztuczka",
            "name_en": "Prestidigitation",
            "classes": [
                "bard",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "ray_of_frost",
            "name_pl": "Promień Mrozu",
            "name_en": "Ray of Frost",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "sacred_flame",
            "name_pl": "Święty Płomień",
            "name_en": "Sacred Flame",
            "classes": [
                "cleric"
            ]
        },
        {
            "id": "shillelagh",
            "name_pl": "Kij",
            "name_en": "Shillelagh",
            "classes": [
                "druid"
            ]
        },
        {
            "id": "shocking_grasp",
            "name_pl": "Porażający Uścisk",
            "name_en": "Shocking Grasp",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "thaumaturgy",
            "name_pl": "Taumaturgia",
            "name_en": "Thaumaturgy",
            "classes": [
                "cleric"
            ]
        },
        {
            "id": "vicious_mockery",
            "name_pl": "Okrutna Drwina",
            "name_en": "Vicious Mockery",
            "classes": [
                "bard"
            ]
        },
        {
            "id": "druidcraft",
            "name_pl": "Sztuczka Druida",
            "name_en": "Druidcraft",
            "classes": [
                "druid"
            ]
        },
        {
            "id": "poison_spray",
            "name_pl": "Trujący Rozprysk",
            "name_en": "Poison Spray",
            "classes": [
                "druid",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "produce_flame",
            "name_pl": "Wywołanie Płomienia",
            "name_en": "Produce Flame",
            "classes": [
                "druid"
            ]
        },
        {
            "id": "resistance",
            "name_pl": "Opór",
            "name_en": "Resistance",
            "classes": [
                "cleric",
                "druid"
            ]
        },
        {
            "id": "thorn_whip",
            "name_pl": "Bicz z Cierni",
            "name_en": "Thorn Whip",
            "classes": [
                "druid"
            ]
        },
        {
            "id": "mending",
            "name_pl": "Naprawa",
            "name_en": "Mending",
            "classes": [
                "bard",
                "cleric",
                "druid",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "word_of_radiance",
            "name_pl": "Słowo Blasku",
            "name_en": "Word of Radiance",
            "classes": [
                "cleric"
            ]
        },
        {
            "id": "toll_the_dead",
            "name_pl": "Bicie w Dzwony",
            "name_en": "Toll the Dead",
            "classes": [
                "cleric",
                "warlock",
                "wizard"
            ]
        }
    ],
    "level_1": [
        {
            "id": "alarm",
            "name_pl": "Alarm",
            "name_en": "Alarm",
            "classes": [
                "ranger",
                "wizard"
            ]
        },
        {
            "id": "animal_friendship",
            "name_pl": "Przyjaźń Zwierząt",
            "name_en": "Animal Friendship",
            "classes": [
                "bard",
                "druid",
                "ranger"
            ]
        },
        {
            "id": "bane",
            "name_pl": "Zguba",
            "name_en": "Bane",
            "classes": [
                "bard",
                "cleric"
            ]
        },
        {
            "id": "bless",
            "name_pl": "Błogosławieństwo",
            "name_en": "Bless",
            "classes": [
                "cleric",
                "paladin"
            ]
        },
        {
            "id": "burning_hands",
            "name_pl": "Płonące Dłonie",
            "name_en": "Burning Hands",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "charm_person",
            "name_pl": "Zauroczenie Osoby",
            "name_en": "Charm Person",
            "classes": [
                "bard",
                "druid",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "color_spray",
            "name_pl": "Barwne Kaskady",
            "name_en": "Color Spray",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "command",
            "name_pl": "Rozkaz",
            "name_en": "Command",
            "classes": [
                "cleric",
                "paladin"
            ]
        },
        {
            "id": "comprehend_languages",
            "name_pl": "Zrozumienie Języków",
            "name_en": "Comprehend Languages",
            "classes": [
                "bard",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "cure_wounds",
            "name_pl": "Leczenie Ran",
            "name_en": "Cure Wounds",
            "classes": [
                "bard",
                "cleric",
                "druid",
                "paladin",
                "ranger"
            ]
        },
        {
            "id": "detect_magic",
            "name_pl": "Wykrycie Magii",
            "name_en": "Detect Magic",
            "classes": [
                "bard",
                "cleric",
                "druid",
                "paladin",
                "ranger",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "disguise_self",
            "name_pl": "Zmiana Wyglądu",
            "name_en": "Disguise Self",
            "classes": [
                "bard",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "entangle",
            "name_pl": "Oplątanie",
            "name_en": "Entangle",
            "classes": [
                "druid"
            ]
        },
        {
            "id": "faerie_fire",
            "name_pl": "Ogień Faerie",
            "name_en": "Faerie Fire",
            "classes": [
                "bard",
                "druid"
            ]
        },
        {
            "id": "feather_fall",
            "name_pl": "Piórkowe Opadanie",
            "name_en": "Feather Fall",
            "classes": [
                "bard",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "find_familiar",
            "name_pl": "Znalezienie Chowańca",
            "name_en": "Find Familiar",
            "classes": [
                "wizard"
            ]
        },
        {
            "id": "guiding_bolt",
            "name_pl": "Naprowadzający Pocisk",
            "name_en": "Guiding Bolt",
            "classes": [
                "cleric"
            ]
        },
        {
            "id": "healing_word",
            "name_pl": "Lecznicze Słowo",
            "name_en": "Healing Word",
            "classes": [
                "bard",
                "cleric",
                "druid"
            ]
        },
        {
            "id": "hellish_rebuke",
            "name_pl": "Piekielna Reprymenda",
            "name_en": "Hellish Rebuke",
            "classes": [
                "warlock"
            ]
        },
        {
            "id": "heroism",
            "name_pl": "Heroizm",
            "name_en": "Heroism",
            "classes": [
                "bard",
                "paladin"
            ]
        },
        {
            "id": "hex",
            "name_pl": "Klątwa",
            "name_en": "Hex",
            "classes": [
                "warlock"
            ]
        },
        {
            "id": "identify",
            "name_pl": "Identyfikacja",
            "name_en": "Identify",
            "classes": [
                "bard",
                "wizard"
            ]
        },
        {
            "id": "inflict_wounds",
            "name_pl": "Zadawanie Ran",
            "name_en": "Inflict Wounds",
            "classes": [
                "cleric"
            ]
        },
        {
            "id": "mage_armor",
            "name_pl": "Zbroja Maga",
            "name_en": "Mage Armor",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "magic_missile",
            "name_pl": "Magiczny Pocisk",
            "name_en": "Magic Missile",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "sanctuary",
            "name_pl": "Sanktuarium",
            "name_en": "Sanctuary",
            "classes": [
                "cleric"
            ]
        },
        {
            "id": "shield",
            "name_pl": "Tarcza",
            "name_en": "Shield",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "sleep",
            "name_pl": "Uśpienie",
            "name_en": "Sleep",
            "classes": [
                "bard",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "thunderwave",
            "name_pl": "Fala Gromu",
            "name_en": "Thunderwave",
            "classes": [
                "bard",
                "druid",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "absorb_elements",
            "name_pl": "Absorpcja Żywiołów",
            "name_en": "Absorb Elements",
            "classes": [
                "druid",
                "ranger",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "ice_knife",
            "name_pl": "Lodowy Nóż",
            "name_en": "Ice Knife",
            "classes": [
                "druid",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "goodberry",
            "name_pl": "Dobre Jagody",
            "name_en": "Goodberry",
            "classes": [
                "druid",
                "ranger"
            ]
        },
        {
            "id": "speak_with_animals",
            "name_pl": "Rozmowa ze Zwierzętami",
            "name_en": "Speak with Animals",
            "classes": [
                "bard",
                "druid",
                "ranger"
            ]
        },
        {
            "id": "fog_cloud",
            "name_pl": "Mglista Chmura",
            "name_en": "Fog Cloud",
            "classes": [
                "druid",
                "ranger",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "jump",
            "name_pl": "Skok",
            "name_en": "Jump",
            "classes": [
                "druid",
                "ranger",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "longstrider",
            "name_pl": "Cwał",
            "name_en": "Longstrider",
            "classes": [
                "bard",
                "druid",
                "ranger",
                "wizard"
            ]
        },
        {
            "id": "purify_food_and_drink",
            "name_pl": "Oczyszczenie Jedzenia i Picia",
            "name_en": "Purify Food and Drink",
            "classes": [
                "cleric",
                "druid",
                "paladin"
            ]
        }
    ],
    "level_2": [
        {
            "id": "blindness_deafness",
            "name_pl": "Ślepota/Głuchota",
            "name_en": "Blindness/Deafness",
            "classes": [
                "bard",
                "cleric",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "blur",
            "name_pl": "Rozmycie",
            "name_en": "Blur",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "darkness",
            "name_pl": "Ciemność",
            "name_en": "Darkness",
            "classes": [
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "hold_person",
            "name_pl": "Unieruchomienie Osoby",
            "name_en": "Hold Person",
            "classes": [
                "bard",
                "cleric",
                "druid",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "invisibility",
            "name_pl": "Niewidzialność",
            "name_en": "Invisibility",
            "classes": [
                "bard",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "misty_step",
            "name_pl": "Krok Mgły",
            "name_en": "Misty Step",
            "classes": [
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "scorching_ray",
            "name_pl": "Piekący Promień",
            "name_en": "Scorching Ray",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "shatter",
            "name_pl": "Roztrzaskanie",
            "name_en": "Shatter",
            "classes": [
                "bard",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "spiritual_weapon",
            "name_pl": "Duchowa Broń",
            "name_en": "Spiritual Weapon",
            "classes": [
                "cleric"
            ]
        },
        {
            "id": "pass_without_trace",
            "name_pl": "Przejście bez Śladu",
            "name_en": "Pass without Trace",
            "classes": [
                "druid",
                "ranger"
            ]
        },
        {
            "id": "spike_growth",
            "name_pl": "Wzrost Kolców",
            "name_en": "Spike Growth",
            "classes": [
                "druid",
                "ranger"
            ]
        },
        {
            "id": "moonbeam",
            "name_pl": "Promień Księżyca",
            "name_en": "Moonbeam",
            "classes": [
                "druid"
            ]
        },
        {
            "id": "flaming_sphere",
            "name_pl": "Płonąca Kula",
            "name_en": "Flaming Sphere",
            "classes": [
                "druid",
                "wizard"
            ]
        },
        {
            "id": "barkskin",
            "name_pl": "Kora",
            "name_en": "Barkskin",
            "classes": [
                "druid",
                "ranger"
            ]
        },
        {
            "id": "heat_metal",
            "name_pl": "Rozgrzanie Metalu",
            "name_en": "Heat Metal",
            "classes": [
                "bard",
                "druid"
            ]
        },
        {
            "id": "enhance_ability",
            "name_pl": "Wzmocnienie Cecha",
            "name_en": "Enhance Ability",
            "classes": [
                "bard",
                "cleric",
                "druid",
                "sorcerer"
            ]
        }
    ],
    "level_3": [
        {
            "id": "counterspell",
            "name_pl": "Kontrzaklęcie",
            "name_en": "Counterspell",
            "classes": [
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "dispel_magic",
            "name_pl": "Rozproszenie Magii",
            "name_en": "Dispel Magic",
            "classes": [
                "bard",
                "cleric",
                "druid",
                "paladin",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "fireball",
            "name_pl": "Kula Ognia",
            "name_en": "Fireball",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "fly",
            "name_pl": "Lot",
            "name_en": "Fly",
            "classes": [
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "haste",
            "name_pl": "Przyspieszenie",
            "name_en": "Haste",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "lightning_bolt",
            "name_pl": "Piorun",
            "name_en": "Lightning Bolt",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "revivify",
            "name_pl": "Ożywienie",
            "name_en": "Revivify",
            "classes": [
                "cleric",
                "paladin"
            ]
        },
        {
            "id": "call_lightning",
            "name_pl": "Wezwanie Błyskawic",
            "name_en": "Call Lightning",
            "classes": [
                "druid"
            ]
        },
        {
            "id": "plant_growth",
            "name_pl": "Wzrost Roślin",
            "name_en": "Plant Growth",
            "classes": [
                "bard",
                "druid",
                "ranger"
            ]
        },
        {
            "id": "sleet_storm",
            "name_pl": "Burza Śnieżna",
            "name_en": "Sleet Storm",
            "classes": [
                "druid",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "water_breathing",
            "name_pl": "Oddychanie pod Wodą",
            "name_en": "Water Breathing",
            "classes": [
                "druid",
                "ranger",
                "sorcerer",
                "wizard"
            ]
        }
    ],
    "level_4": [
        {
            "id": "banishment",
            "name_pl": "Wygnanie",
            "name_en": "Banishment",
            "classes": [
                "cleric",
                "paladin",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "blight",
            "name_pl": "Zaraza",
            "name_en": "Blight",
            "classes": [
                "druid",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "dimension_door",
            "name_pl": "Drzwi przez Wymiary",
            "name_en": "Dimension Door",
            "classes": [
                "bard",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "greater_invisibility",
            "name_pl": "Większa Niewidzialność",
            "name_en": "Greater Invisibility",
            "classes": [
                "bard",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "polymorph",
            "name_pl": "Polimorfia",
            "name_en": "Polymorph",
            "classes": [
                "bard",
                "druid",
                "sorcerer",
                "wizard"
            ]
        }
    ],
    "level_5": [
        {
            "id": "cloudkill",
            "name_pl": "Zabójcza Chmura",
            "name_en": "Cloudkill",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "cone_of_cold",
            "name_pl": "Stożek Zimna",
            "name_en": "Cone of Cold",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "greater_restoration",
            "name_pl": "Większe Uzdrowienie",
            "name_en": "Greater Restoration",
            "classes": [
                "bard",
                "cleric",
                "druid"
            ]
        },
        {
            "id": "hold_monster",
            "name_pl": "Unieruchomienie Potwora",
            "name_en": "Hold Monster",
            "classes": [
                "bard",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "mass_cure_wounds",
            "name_pl": "Masowe Leczenie Ran",
            "name_en": "Mass Cure Wounds",
            "classes": [
                "bard",
                "cleric",
                "druid"
            ]
        }
    ],
    "level_6": [
        {
            "id": "chain_lightning",
            "name_pl": "Łańcuch Piorunów",
            "name_en": "Chain Lightning",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "disintegrate",
            "name_pl": "Dezintegracja",
            "name_en": "Disintegrate",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "heal",
            "name_pl": "Uzdrawianie",
            "name_en": "Heal",
            "classes": [
                "cleric",
                "druid"
            ]
        },
        {
            "id": "sunbeam",
            "name_pl": "Promień Słońca",
            "name_en": "Sunbeam",
            "classes": [
                "druid",
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "true_seeing",
            "name_pl": "Prawdziwe Widzenie",
            "name_en": "True Seeing",
            "classes": [
                "bard",
                "cleric",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        }
    ],
    "level_7": [
        {
            "id": "delayed_blast_fireball",
            "name_pl": "Opóźniona Kula Ognia",
            "name_en": "Delayed Blast Fireball",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "finger_of_death",
            "name_pl": "Palec Śmierci",
            "name_en": "Finger of Death",
            "classes": [
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "forcecage",
            "name_pl": "Klatka Mocy",
            "name_en": "Forcecage",
            "classes": [
                "bard",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "plane_shift",
            "name_pl": "Przesunięcie Planów",
            "name_en": "Plane Shift",
            "classes": [
                "cleric",
                "druid",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "resurrection",
            "name_pl": "Zmartwychwstanie",
            "name_en": "Resurrection",
            "classes": [
                "bard",
                "cleric"
            ]
        }
    ],
    "level_8": [
        {
            "id": "antimagic_field",
            "name_pl": "Pole Antymagiczne",
            "name_en": "Antimagic Field",
            "classes": [
                "cleric",
                "wizard"
            ]
        },
        {
            "id": "dominate_monster",
            "name_pl": "Zdominowanie Potwora",
            "name_en": "Dominate Monster",
            "classes": [
                "bard",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "feeblemind",
            "name_pl": "Słaboumysłowość",
            "name_en": "Feeblemind",
            "classes": [
                "bard",
                "druid",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "incendiary_cloud",
            "name_pl": "Zapalająca Chmura",
            "name_en": "Incendiary Cloud",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "sunburst",
            "name_pl": "Eksplozja Słońca",
            "name_en": "Sunburst",
            "classes": [
                "druid",
                "sorcerer",
                "wizard"
            ]
        }
    ],
    "level_9": [
        {
            "id": "meteor_swarm",
            "name_pl": "Rój Meteorów",
            "name_en": "Meteor Swarm",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "power_word_kill",
            "name_pl": "Słowo Mocy: Giń",
            "name_en": "Power Word Kill",
            "classes": [
                "bard",
                "sorcerer",
                "warlock",
                "wizard"
            ]
        },
        {
            "id": "time_stop",
            "name_pl": "Zatrzymanie Czasu",
            "name_en": "Time Stop",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        },
        {
            "id": "true_resurrection",
            "name_pl": "Prawdziwe Zmartwychwstanie",
            "name_en": "True Resurrection",
            "classes": [
                "cleric",
                "druid"
            ]
        },
        {
            "id": "wish",
            "name_pl": "Życzenie",
            "name_en": "Wish",
            "classes": [
                "sorcerer",
                "wizard"
            ]
        }
    ]
}

STAT_NAMES = {
    "str": "Siła",
    "dex": "Zręczność",
    "con": "Kondycja",
    "int": "Inteligencja",
    "wis": "Mądrość",
    "cha": "Charyzma",
}

STANDARD_ARRAY = [15, 14, 13, 12, 10, 8]

POINT_BUY_COSTS = {8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9}
POINT_BUY_TOTAL = 27
POINT_BUY_MIN = 8
POINT_BUY_MAX = 15

PROFICIENCY_BY_LEVEL = {
    1: 2, 2: 2, 3: 2, 4: 2,
    5: 3, 6: 3, 7: 3, 8: 3,
    9: 4, 10: 4, 11: 4, 12: 4,
    13: 5, 14: 5, 15: 5, 16: 5,
    17: 6, 18: 6, 19: 6, 20: 6,
}

CLASS_STAT_PRIORITY = {
    "barbarian": ["str", "con", "dex", "wis", "int", "cha"],
    "bard": ["cha", "dex", "con", "int", "wis", "str"],
    "cleric": ["wis", "con", "str", "cha", "dex", "int"],
    "druid": ["wis", "con", "int", "dex", "str", "cha"],
    "fighter": ["str", "con", "dex", "wis", "cha", "int"],
    "monk": ["dex", "wis", "con", "str", "int", "cha"],
    "paladin": ["str", "cha", "con", "wis", "dex", "int"],
    "ranger": ["dex", "wis", "con", "str", "int", "cha"],
    "rogue": ["dex", "int", "con", "cha", "wis", "str"],
    "sorcerer": ["cha", "con", "dex", "int", "wis", "str"],
    "warlock": ["cha", "con", "dex", "wis", "int", "str"],
    "wizard": ["int", "con", "dex", "wis", "cha", "str"],
}


FEATS = {
    "alert": {
        "name": "Czujny",
        "name_en": "Alert",
        "desc": "+5 do inicjatywy, nie można cię zaskoczyć dopóki jesteś przytomny."
    },
    "tough": {
        "name": "Twardziel",
        "name_en": "Tough",
        "desc": "Twoje maksimum Punktów Wytrzymałości rośnie o 2 za każdy twój poziom."
    },
    "lucky": {
        "name": "Szczęściarz",
        "name_en": "Lucky",
        "desc": "Masz 3 punkty szczęścia. Możesz ich użyć, by przerzucić k20 lub zmusić wroga do przerzutu."
    },
    "mobile": {
        "name": "Mobilny",
        "name_en": "Mobile",
        "desc": "Twoja prędkość rośnie o 3 metry. Ataki z ukrycia (Dash) trudnym terenem cię nie spowalniają."
    },
    "sharpshooter": {
        "name": "Strzelec Wyborowy",
        "name_en": "Sharpshooter",
        "desc": "Ignorujesz częściową osłonę. Możesz przyjąć -5 do ataku za +10 do obrażeń przy ataku dystansowym."
    },
    "great_weapon_master": {
        "name": "Mistrz Broni Dwuręcznej",
        "name_en": "Great Weapon Master",
        "desc": "Gdy trafisz krytycznie lub zabijesz, możesz wykonać atak bonusowy. Przyjęcie -5 do ataku daje +10 obrażeń ciężką bronią."
    },
    "war_caster": {
        "name": "Mag Bitewny",
        "name_en": "War Caster",
        "desc": "Przewaga na rzuty obronne na Koncentrację. Możesz rzucać czary mając broń/tarczę w dłoniach. Zaklęcie na atak okazyjny."
    },
    "sentinel": {
        "name": "Strażnik",
        "name_en": "Sentinel",
        "desc": "Trafienie okazyjne redukuje prędkość celu do 0. Istoty uciekające od ciebie prowokują atak, nawet przy Odskoku."
    },
    "resilient": {
        "name": "Odporny",
        "name_en": "Resilient",
        "desc": "+1 do wybranej cechy oraz biegłość w Rzutach Obronnych z niej."
    },
    "actor": {
        "name": "Aktor",
        "name_en": "Actor",
        "desc": "+1 do Charyzmy. Przewaga na oszustwo i występy w przebraniu."
    },
    "observant": {
        "name": "Spostrzegawczy",
        "name_en": "Observant",
        "desc": "+1 do Inteligencji lub Mądrości. Czytasz z ruchu warg, +5 do pasywnej percepcji i pasywnego śledztwa."
    },
    "polearm_master": {
        "name": "Mistrz Broni Drzewcowej",
        "name_en": "Polearm Master",
        "desc": "Atakujesz z akcji bonusowej tępym końcem broni. Wróg prowokuje atak okazyjny gdy wchodzi w twój zasięg."
    },
    "spell_sniper": {
        "name": "Snajper Zaklęć",
        "name_en": "Spell Sniper",
        "desc": "Zasięg zaklęć ataku x2. Ignorują one pół osłony. 1 dodatkowa sztuczka wymagająca ataku."
    }
}
