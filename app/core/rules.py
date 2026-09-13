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
            "Biegłość w broni elfów: Długi miecz, krótki miecz, krótki łuk, długi łuk",
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
            "Biegłość w broni elfów: Długi miecz, krótki miecz, krótki łuk, długi łuk",
            "Zwinność lasu: Możesz się ukryć będąc tylko lekko przysłoniętym przez naturę"
        ],
        "languages": ["Wspólny", "Elficki"],
        "darkvision": True,
        "description": "Zwinna rasa elfów żyjących w harmonii z naturą.",
        "subraces": {},
    },
    "dwarf_hill": {
        "name": "Krasnolud Wzgórz",
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
        "name": "Krasnolud Górski",
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
    "goblin": {
        "name": "Goblin",
        "name_en": "Goblin",
        "asi": {"dex": 2, "con": 1},
        "speed": 9,
        "size": "Mały",
        "traits": [
            "Mroczne widzenie (18m)",
            "Zwinna ucieczka: Możesz wykonać akcję Ukrycia lub Odskoku jako akcję dodatkową",
            "Furia Małych: Raz na długi odpoczynek zadaj dodatkowe obrażenia równe poziomowi postaci, gdy trafisz atakiem lub zaklęciem stworzenie większe od ciebie",
        ],
        "languages": ["Wspólny", "Gobliński"],
        "darkvision": True,
        "description": "Mały, zwinny goblinoid o dużej pomysłowości i instynkcie przetrwania.",
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
    "aasimar": {
        "name": "Aasimar",
        "name_en": "Aasimar",
        "asi": {"cha": 2, "wis": 1},
        "speed": 9,
        "size": "Średni",
        "traits": [
            "Mroczne widzenie (18m)",
            "Niebiańska Oporność: Odporność na obrażenia nekrotyczne i świetliste (radiant)",
            "Leczące Dłonie: Leczysz cel za liczbę PW równą twojemu poziomowi raz na długi odpoczynek",
            "Sztuczka: Światło (Light)"
        ],
        "languages": ["Wspólny", "Niebiański"],
        "darkvision": True,
        "description": "Dotknięci niebiańską mocą, Aasimarowie niosą światło w ciemności.",
        "subraces": {},
    },
    "goliath": {
        "name": "Goliat",
        "name_en": "Goliath",
        "asi": {"str": 2, "con": 1},
        "speed": 9,
        "size": "Średni",
        "traits": [
            "Naturalny Atleta: Biegłość w Atletyce",
            "Wytrzymałość Kamienia: Raz na krótki odpoczynek zredukuj otrzymane obrażenia o 1k12 + mod. Kondycji",
            "Potężna Budowa: Liczysz się jako rozmiar Duży przy udźwigu",
            "Górskie Dziecko: Odporność na zimno i aklimatyzacja na dużych wysokościach"
        ],
        "languages": ["Wspólny", "Giganci"],
        "darkvision": False,
        "description": "Potężni potomkowie gigantów górskich, ceniący siłę i niezależność.",
        "subraces": {},
    },
    "tabaxi": {
        "name": "Tabaxi",
        "name_en": "Tabaxi",
        "asi": {"dex": 2, "cha": 1},
        "speed": 9,
        "size": "Średni",
        "traits": [
            "Mroczne widzenie (18m)",
            "Kocia Zwinność: Możesz podwoić swoją prędkość do końca tury (odnawia się po bezruchu)",
            "Pazury: Twoje nieuzbrojone ataki zadają 1k4 + mod. Siły obrażeń tnących",
            "Talent Kota: Biegłość w Percepcji i Ukrywaniu się",
            "Szybka Wspinaczka: Prędkość wspinaczki 6m"
        ],
        "languages": ["Wspólny", "+ 1 do wyboru"],
        "darkvision": True,
        "description": "Kocioludzie kierowani ciekawością i pasją do zbierania niezwykłych opowieści i skarbów.",
        "subraces": {},
    },
    "firbolg": {
        "name": "Firbolg",
        "name_en": "Firbolg",
        "asi": {"wis": 2, "str": 1},
        "speed": 9,
        "size": "Średni",
        "traits": [
            "Magia Firbolgów: Rzucasz Wykrycie Magii i Przebranie (Disguise Self) raz na krótki odp.",
            "Ukryty Krok: Reakcją możesz stać się niewidzialny do początku następnej tury po ataku",
            "Potężna Budowa: Liczysz się jako rozmiar Duży przy udźwigu",
            "Mowa Zwierząt i Roślin: Potrafisz przekazać prostą myśl roślinom i bestiom"
        ],
        "languages": ["Wspólny", "Elficki", "Giganci"],
        "darkvision": False,
        "description": "Spokojni, gigantyczni strażnicy prastarych lasów.",
        "subraces": {},
    },
    "kenku": {
        "name": "Kenku",
        "name_en": "Kenku",
        "asi": {"dex": 2, "wis": 1},
        "speed": 9,
        "size": "Średni",
        "traits": [
            "Ekspercki Fałszerz: Masz przewagę na kopiowanie tekstów i rzemiosła",
            "Trening Kenku: Dwie biegłości z: Akrobatyka, Oszustwo, Ukrywanie, Zwinne Dłonie",
            "Naśladownictwo: Perfekcyjnie naśladujesz dźwięki i głosy, które słyszałeś"
        ],
        "languages": ["Wspólny", "Auran (czytanie i pisanie)"],
        "darkvision": False,
        "description": "Krukoludzie pozbawieni skrzydeł i własnego głosu, skazani na naśladownictwo.",
        "subraces": {},
    }
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
    "artificer": {
        "name": "Wynalazca",
        "name_en": "Artificer",
        "hit_die": 8,
        "primary_stats": ["int"],
        "saving_throws": ["con", "int"],
        "armor_proficiencies": ["lekka", "średnia", "tarcze"],
        "weapon_proficiencies": ["prosta", "broń palna (opcjonalnie)"],
        "num_skills": 2,
        "skill_choices": ["arcana", "historia", "badanie", "medycyna", "przyroda", "postrzeganie", "sleight_of_hand"],
        "features_1": [
            "Magiczne Majsterkowanie",
            "Rzucanie zaklęć (Int)",
        ],
        "spellcasting": True,
        "spellcasting_stat": "int",
        "description": "Mistrz inwencji, używający magii poprzez przedmioty, które tworzy.",
        "subclasses": {
            "alchemist": "Alchemik - ekspert od mikstur i leczenia",
            "artillerist": "Artylerzysta - mistrz magicznych wieżyczek",
            "battlesmith": "Kowal Bitewny - wojownik ze stalowym obrońcą",
            "armorer": "Zbrojmistrz - mistrz modyfikowanych pancerzy",
        },
        "primary_ability": "INT",
    },
    "bard": {
        "name": "Bard",
        "name_en": "Bard",
        "hit_die": 8,
        "primary_stats": ["cha"],
        "saving_throws": ["dex", "cha"],
        "armor_proficiencies": ["lekka"],
        "weapon_proficiencies": ["prosta", "ręczna kusza", "długi miecz", "rapier", "krótki miecz"],
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
        "subclasses": {
            "open_hand": "Droga Otwartej Dłoni - mistrz uderzeń bezbronnych",
            "shadow": "Droga Cienia - ninja i cisi mordercy",
            "four_elements": "Droga Czterech Żywiołów - władca żywiołów",
        },
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
        "spellcasting_level": 2,
        "spellcasting_stat": "cha",
        "description": "Święty wojownik złączony przysięgą z boską mocą.",
        "subclasses": {
            "devotion": "Przysięga Oddania - klasyczny święty rycerz",
            "ancients": "Przysięga Starożytnych - zielony rycerz natury",
            "vengeance": "Przysięga Zemsty - bezwzględny inkwizytor",
        },
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
        "spellcasting_level": 2,
        "spellcasting_stat": "wis",
        "description": "Strażnik dziczy, łowca i zwiadowca.",
        "subclasses": {
            "hunter": "Łowca - skupiony na walce z konkretnymi zagrożeniami",
            "beast_master": "Władca Bestii - towarzysze zwierzęcy",
        },
        "primary_ability": "DEX/WIS",
    },
    "rogue": {
        "name": "Łotrzyk",
        "name_en": "Rogue",
        "hit_die": 8,
        "primary_stats": ["dex"],
        "saving_throws": ["dex", "int"],
        "armor_proficiencies": ["lekka"],
        "weapon_proficiencies": ["prosta", "ręczna kusza", "długi miecz", "rapier", "krótki miecz"],
        "num_skills": 4,
        "skill_choices": ["akrobatyka", "atletyka", "oszustwo", "badanie", "wgląd", "zastraszanie", "postrzeganie", "wykonanie", "perswazja", "sleight_of_hand", "ukrycie"],
        "features_1": [
            "Wiedza Eksperta: x2 premię za biegłość w 2 umiejętnościach",
            "Atak Skrytobójczy: +1k6 obrażeń gdy masz przewagę lub sojusznik jest obok celu",
            "Złodziejski żargon: Tajny język złodziei",
        ],
        "spellcasting": False,
        "description": "Skryty i zwinny mistrz sztuczek, infiltracji i nagłych ataków.",
        "subclasses": {
            "thief": "Złodziej - szybkie ręce i perfekcyjna wspinaczka",
            "assassin": "Zabójca - ekspert od eliminacji celów",
            "arcane_trickster": "Tajemny Szachraj - magiczny oszust",
        },
        "primary_ability": "DEX",
    },
    "sorcerer": {
        "name": "Zaklinacz",
        "name_en": "Sorcerer",
        "hit_die": 6,
        "primary_stats": ["cha"],
        "saving_throws": ["con", "cha"],
        "armor_proficiencies": [],
        "weapon_proficiencies": ["sztylet", "oszczep", "proca", "kij", "lekka kusza"],
        "num_skills": 2,
        "skill_choices": ["arcana", "oszustwo", "wgląd", "zastraszanie", "perswazja", "religia"],
        "features_1": [
            "Rzucanie zaklęć (Cha)",
            "Magiczne Źródło: Wybierz źródło mocy (Smocze, Dzikie)",
        ],
        "spellcasting": True,
        "spellcasting_stat": "cha",
        "description": "Mag czerpiący moc z wrodzonego daru magicznego.",
        "subclasses": {
            "draconic": "Rodowód Smoka - smocze moce i łuski",
            "wild_magic": "Dzika Magia - chaotyczne wybuchy mocy",
        },
        "primary_ability": "CHA",
    },
    "warlock": {
        "name": "Czarownik",
        "name_en": "Warlock",
        "hit_die": 8,
        "primary_stats": ["cha"],
        "saving_throws": ["wis", "cha"],
        "armor_proficiencies": ["lekka"],
        "weapon_proficiencies": ["prosta"],
        "num_skills": 2,
        "skill_choices": ["arcana", "oszustwo", "historia", "zastraszanie", "badanie", "przyroda", "religia"],
        "features_1": [
            "Pakt Okultystyczny: Wybierz patrona (Arcywróżka, Demon, Wielki Przedwieczny)",
            "Magia Paktu: 1 miejsce zaklęcia, odnawialne po krótkim odpoczynku",
        ],
        "spellcasting": True,
        "spellcasting_stat": "cha",
        "description": "Czarownik, który zawarł pakt z nadnaturalną istotą.",
        "subclasses": {
            "archfey": "Arcywróżka - patron z Feywild",
            "fiend": "Diabelski Patron - niszczycielska magia piekieł",
            "great_old_one": "Wielki Przedwieczny - moc umysłowa z kosmosu",
        },
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

from app.core.spells import SPELLS, SPELLS_BY_ID, get_spell_by_id, get_spells

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

WILD_SHAPE_FORMS = {
    0.0: [
        {"name": "Kot", "name_en": "Cat", "cr": 0, "hp": 2, "ac": 12, "speed": "12m, wspinaczka 9m", "attacks": "Pazury (+0 do trafienia, 1 obr. tnące)", "features": "Wysokie ukrywanie i zwinność."},
        {"name": "Borsuk", "name_en": "Badger", "cr": 0, "hp": 3, "ac": 10, "speed": "6m, kopanie 1.5m", "attacks": "Ugryzienie (+2 do trafienia, 1 obr. kłute)", "features": "Węch."},
        {"name": "Sowa", "name_en": "Owl", "cr": 0, "hp": 1, "ac": 11, "speed": "1.5m, lot 18m", "attacks": "Szpony (+3 trafienie, 1 tnące)", "features": "Lot z zaskoczenia (bez ataków okazyjnych)."}
    ],
    0.125: [
        {"name": "Mastif", "name_en": "Mastiff", "cr": 0.125, "hp": 5, "ac": 12, "speed": "12m", "attacks": "Ugryzienie (+3 do trafienia, 1k6+1 kłute)", "features": "ST 11 Siła przewrócenie (Prone)."},
        {"name": "Gigantyczny Szczur", "name_en": "Giant Rat", "cr": 0.125, "hp": 7, "ac": 12, "speed": "9m", "attacks": "Ugryzienie (+4 do trafienia, 1k4+2 kłute)", "features": "Taktyka Stada."}
    ],
    0.25: [
        {"name": "Wilk", "name_en": "Wolf", "cr": 0.25, "hp": 11, "ac": 13, "speed": "12m", "attacks": "Ugryzienie (+4 do trafienia, 2k4+2 kłute)", "features": "Taktyka Stada, ST 11 Siła przewrócenie."},
        {"name": "Gigantyczny Borsuk", "name_en": "Giant Badger", "cr": 0.25, "hp": 13, "ac": 10, "speed": "9m, kopanie 3m", "attacks": "Wielokrotny atak (Ugryzienie + Pazury)", "features": "Mroczne widzenie, wyostrzony węch."},
        {"name": "Dzik", "name_en": "Boar", "cr": 0.25, "hp": 11, "ac": 11, "speed": "12m", "attacks": "Kły (+3 trafienie, 1k6+1 tnące)", "features": "Szarża (+1k6 obrażeń). Relentless (Zostaje z 1 HP)."},
        {"name": "Pantera", "name_en": "Panther", "cr": 0.25, "hp": 13, "ac": 12, "speed": "15m, wspinaczka 12m", "attacks": "Ugryzienie (+4), Pazury (+4)", "features": "Skok z zasadzki (Pounce) dający atak bonusowy."}
    ],
    0.5: [
        {"name": "Czarny Niedźwiedź", "name_en": "Black Bear", "cr": 0.5, "hp": 19, "ac": 11, "speed": "12m, wspinaczka 9m", "attacks": "Wielokrotny atak (Ugryzienie + Pazury)", "features": "Węch."},
        {"name": "Małpa", "name_en": "Ape", "cr": 0.5, "hp": 19, "ac": 12, "speed": "9m, wspinaczka 9m", "attacks": "Wielokrotny atak (2x Pięść +5 trafienie, 1k6+3)", "features": "Zdolność rzucania kamieniami."},
        {"name": "Koń Bojowy", "name_en": "Warhorse", "cr": 0.5, "hp": 19, "ac": 11, "speed": "18m", "attacks": "Kopyta (+6 trafienie, 2k6+4 obuchowe)", "features": "Tratująca Szarża (Trampling Charge)."}
    ],
    1.0: [
        {"name": "Niedźwiedź Brunatny", "name_en": "Brown Bear", "cr": 1, "hp": 34, "ac": 11, "speed": "12m, wspinaczka 9m", "attacks": "Wielokrotny atak (Ugryzienie + Pazury)", "features": "Dobre zdrowie, mocne obrażenia bazowe."},
        {"name": "Wilkor", "name_en": "Dire Wolf", "cr": 1, "hp": 37, "ac": 14, "speed": "15m", "attacks": "Ugryzienie (+5 trafienie, 2k6+3 kłute)", "features": "Taktyka Stada, ST 13 Siła przewrócenie."},
        {"name": "Gigantyczny Pająk", "name_en": "Giant Spider", "cr": 1, "hp": 26, "ac": 14, "speed": "9m, wspinaczka 9m", "attacks": "Ugryzienie (+5 trafienie, 1k8+3 kłute + 2k8 trucizna)", "features": "Wspinaczka pajęcza, Sieć (Web) do pętania wrogów."},
        {"name": "Lew", "name_en": "Lion", "cr": 1, "hp": 26, "ac": 12, "speed": "15m", "attacks": "Ugryzienie (+5), Pazury (+5)", "features": "Taktyka Stada, Skok z Zasadzki (Pounce)."}
    ],
    2.0: [
        {"name": "Gigantyczny Dusiciel", "name_en": "Giant Constrictor Snake", "cr": 2, "hp": 60, "ac": 12, "speed": "9m, pływanie 9m", "attacks": "Ugryzienie (+6 trafienie), Duszenie (+6 trafienie)", "features": "Duszenie pęta i chwyta cel na ST 16 ucieczki."},
        {"name": "Niedźwiedź Polarny", "name_en": "Polar Bear", "cr": 2, "hp": 42, "ac": 12, "speed": "12m, pływanie 9m", "attacks": "Wielokrotny atak (Ugryzienie + Pazury)", "features": "Zwiększone statystyki i pływanie."},
        {"name": "Gigantyczny Dzik", "name_en": "Giant Boar", "cr": 2, "hp": 42, "ac": 12, "speed": "12m", "attacks": "Kły (+5 trafienie, 2k6+3 tnące)", "features": "Szarża (+2k6 obr), Zaciętość (Relentless)."},
        {"name": "Alozaur", "name_en": "Allosaurus", "cr": 2, "hp": 51, "ac": 13, "speed": "18m", "attacks": "Ugryzienie (+6 trafienie, 2k10+4), Pazury (+6)", "features": "Skok z zasadzki (Pounce) pozwala uderzyć dwa razy."}
    ],
    3.0: [
        {"name": "Ankylozaur", "name_en": "Ankylosaurus", "cr": 3, "hp": 68, "ac": 15, "speed": "9m", "attacks": "Ogon (+7 trafienie, 4k6+4 obuchowe)", "features": "ST 14 Siła przewrócenie."},
        {"name": "Orka", "name_en": "Killer Whale", "cr": 3, "hp": 90, "ac": 12, "speed": "pływanie 18m", "attacks": "Ugryzienie (+6 trafienie, 5k6+4 kłute)", "features": "Echolokacja, oddychanie wstrzymywane (30 min)."}
    ],
    4.0: [
        {"name": "Słoń", "name_en": "Elephant", "cr": 4, "hp": 76, "ac": 12, "speed": "12m", "attacks": "Cios Kłem (+8, 3k8+6 kłute), Tratowanie (+8, 3k10+6)", "features": "Szarża z Tratowaniem (ST 12 Siła na przewrócenie)."},
        {"name": "Stegozaur", "name_en": "Stegosaurus", "cr": 4, "hp": 76, "ac": 13, "speed": "12m", "attacks": "Ogon (+7 trafienie, 6k6+5 kłute)", "features": "Wysokie obrażenia w walce wręcz."}
    ],
    5.0: [
        {"name": "Gigantyczny Krokodyl", "name_en": "Giant Crocodile", "cr": 5, "hp": 85, "ac": 14, "speed": "9m, pływanie 15m", "attacks": "Ugryzienie (+8), Ogon (+8)", "features": "Wielokrotny atak. Ugryzienie chwyta i pęta automatycznie."},
        {"name": "Triceratops", "name_en": "Triceratops", "cr": 5, "hp": 95, "ac": 13, "speed": "15m", "attacks": "Gore (+9 trafienie, 4k8+6 kłute)", "features": "Tratująca Szarża dająca Przewrócenie i bonus Stomp."}
    ],
    6.0: [
        {"name": "Mamut", "name_en": "Mammoth", "cr": 6, "hp": 126, "ac": 13, "speed": "12m", "attacks": "Gore (+9 trafienie, 4k8+7 kłute)", "features": "Szarża dająca Przewrócenie + Atak Stomp z bonusem 4k10+7."}
    ]
}

_WILD_SHAPE_DETAILS = {
    "Kot": ("Malutka bestia", "3, 15, 10, 3, 12, 7", "Percepcja +3, Skradanie +4", "Bierne 13; węch i słuch", "Ostry słuch i węch"),
    "Borsuk": ("Mała bestia", "13, 11, 12, 2, 12, 5", "Percepcja +3", "Mroczne widzenie 9 m; bierne 13; węch", "Ostry węch"),
    "Sowa": ("Malutka bestia", "3, 17, 8, 2, 13, 7", "Percepcja +3, Skradanie +5", "Mroczne widzenie 36 m; bierne 13; ostry słuch i wzrok", "Przelot: nie prowokuje ataków okazyjnych"),
    "Mastif": ("Średnia bestia", "13, 14, 12, 3, 12, 7", "Percepcja +3", "Bierne 13; ostry słuch i węch", "Ostry słuch i węch"),
    "Gigantyczny Szczur": ("Mała bestia", "7, 15, 11, 2, 10, 4", "Percepcja +2", "Mroczne widzenie 18 m; bierne 12; węch", "Taktyka stada"),
    "Wilk": ("Średnia bestia", "12, 15, 12, 3, 12, 6", "Percepcja +3, Skradanie +4", "Bierne 13; ostry słuch i węch", "Taktyka stada; przewrócenie celu"),
    "Gigantyczny Borsuk": ("Średnia bestia", "13, 10, 15, 2, 12, 5", "Percepcja +3", "Mroczne widzenie 18 m; bierne 13; węch", "Ostry węch; kopanie"),
    "Dzik": ("Średnia bestia", "13, 11, 12, 2, 9, 5", "", "Bierne 9; węch", "Szarża; niezłomność"),
    "Pantera": ("Średnia bestia", "14, 15, 10, 3, 14, 7", "Percepcja +4, Skradanie +6", "Mroczne widzenie 18 m; bierne 14; węch", "Skok z zasadzki"),
    "Czarny Niedźwiedź": ("Średnia bestia", "19, 10, 16, 2, 13, 7", "Percepcja +3", "Bierne 13; węch", "Ostry węch"),
    "Małpa": ("Średnia bestia", "16, 14, 14, 6, 12, 7", "Atletyka +5", "Bierne 11", "Wspinaczka; używa prostych przedmiotów"),
    "Koń Bojowy": ("Duża bestia", "18, 12, 13, 2, 12, 7", "", "Bierne 11", "Szarża z tratowaniem"),
    "Niedźwiedź Brunatny": ("Duża bestia", "19, 10, 16, 2, 13, 7", "Percepcja +3", "Bierne 13; węch", "Ostry węch"),
    "Wilkor": ("Duża bestia", "17, 15, 15, 3, 12, 7", "Percepcja +3, Skradanie +4", "Mroczne widzenie 18 m; bierne 13; słuch i węch", "Taktyka stada; przewrócenie celu"),
    "Gigantyczny Pająk": ("Duża bestia", "14, 16, 12, 2, 11, 4", "Skradanie +7", "Mroczne widzenie 18 m; ślepowidzenie 3 m", "Chodzenie po pajęczynie; wyczucie sieci; sieć"),
    "Lew": ("Duża bestia", "17, 15, 13, 3, 12, 8", "Percepcja +3, Skradanie +6", "Mroczne widzenie 18 m; bierne 13; słuch i węch", "Taktyka stada; skok z zasadzki"),
    "Gigantyczny Dusiciel": ("Ogromna bestia", "19, 14, 12, 1, 10, 3", "Percepcja +4", "Ślepowidzenie 3 m; bierne 14; węch", "Duszenie; chwyta cel"),
    "Niedźwiedź Polarny": ("Duża bestia", "20, 10, 16, 2, 13, 7", "Percepcja +3", "Bierne 13; węch", "Ostry węch; pływanie"),
    "Gigantyczny Dzik": ("Duża bestia", "17, 10, 16, 2, 13, 5", "", "Bierne 11; węch", "Szarża; niezłomność"),
    "Alozaur": ("Duża bestia", "19, 13, 13, 2, 12, 5", "Percepcja +3", "Bierne 13; węch", "Skok z zasadzki"),
    "Ankylozaur": ("Ogromna bestia", "19, 11, 15, 2, 12, 5", "", "Bierne 11", "Ogon może przewrócić cel"),
    "Orka": ("Ogromna bestia", "19, 12, 13, 3, 12, 7", "Percepcja +3", "Echolokacja 36 m; ślepowidzenie 36 m", "Wstrzymywanie oddechu"),
    "Słoń": ("Ogromna bestia", "22, 9, 17, 3, 11, 6", "Percepcja +3", "Bierne 13; węch", "Szarża z tratowaniem"),
    "Stegozaur": ("Ogromna bestia", "20, 12, 17, 2, 11, 5", "", "Bierne 10", "Ogon uderza w cel za plecami"),
    "Gigantyczny Krokodyl": ("Ogromna bestia", "21, 9, 17, 2, 10, 7", "Skradanie +5", "Bierne 10; wstrzymywanie oddechu", "Chwyta i unieruchamia; wstrzymywanie oddechu"),
    "Triceratops": ("Ogromna bestia", "22, 9, 17, 2, 11, 5", "", "Bierne 10", "Szarża z tratowaniem"),
    "Mamut": ("Ogromna bestia", "24, 9, 21, 3, 11, 6", "", "Bierne 10; węch", "Szarża z tratowaniem"),
}

_WILD_SHAPE_ACTIONS = {
    "Kot": "Pazury: +0 do trafienia, 1 obrażenie tnące.",
    "Borsuk": "Ugryzienie: +2 do trafienia, 1 obrażenie kłute.",
    "Sowa": "Szpony: +3 do trafienia, 1 obrażenie tnące.",
    "Mastif": "Ugryzienie: +3 do trafienia, 1k6+1 obrażeń kłutych; ST 11 Siła lub przewrócenie.",
    "Gigantyczny Szczur": "Ugryzienie: +4 do trafienia, 1k4+2 obrażeń kłutych.",
    "Wilk": "Ugryzienie: +4 do trafienia, 2k4+2 obrażeń kłutych; ST 11 Siła lub przewrócenie.",
    "Gigantyczny Borsuk": "Wielokrotny atak: ugryzienie +3, 1k6+1 kłutych oraz pazury +3, 1k4+1 tnących.",
    "Dzik": "Kły: +3 do trafienia, 1k6+1 obrażeń tnących.",
    "Pantera": "Ugryzienie: +4 do trafienia, 1k6+2 kłutych; pazury: +4, 1k4+2 tnących; skok może dać dodatkowe pazury.",
    "Czarny Niedźwiedź": "Wielokrotny atak: ugryzienie +5, 1k8+4 kłutych oraz pazury +5, 2k6+4 tnących.",
    "Małpa": "Pięść: +5 do trafienia, 1k6+3 obrażeń obuchowych; kamień: +5, 1k6+3 obuchowych na dystans.",
    "Koń Bojowy": "Kopyta: +6 do trafienia, 2k6+4 obrażeń obuchowych; po szarży cel wykonuje ST 14 Siła.",
    "Niedźwiedź Brunatny": "Wielokrotny atak: ugryzienie +6, 1k8+4 kłutych oraz pazury +6, 2k6+4 tnących.",
    "Wilkor": "Ugryzienie: +5 do trafienia, 2k6+3 obrażeń kłutych; ST 13 Siła lub przewrócenie.",
    "Gigantyczny Pająk": "Ugryzienie: +5 do trafienia, 1k8+3 kłutych oraz 2k8 trucizny; ST 11 Kondycja, połowa przy udanym rzucie.",
    "Lew": "Wielokrotny atak: ugryzienie +5, 1k8+3 kłutych oraz pazury +5, 1k4+3 tnących; skok z zasadzki.",
    "Gigantyczny Dusiciel": "Ugryzienie: +6 do trafienia, 2k6+4 kłutych; duszenie: +6, 2k8+4 obuchowych i chwyt.",
    "Niedźwiedź Polarny": "Wielokrotny atak: ugryzienie +7, 1k8+5 kłutych oraz pazury +7, 2k6+5 tnących.",
    "Gigantyczny Dzik": "Kły: +5 do trafienia, 2k6+5 obrażeń tnących; szarża dodaje 2k6.",
    "Alozaur": "Wielokrotny atak: ugryzienie +6, 2k10+4 kłutych oraz pazury +6, 1k8+2 tnących.",
    "Ankylozaur": "Ogon: +7 do trafienia, 4k6+4 obrażeń obuchowych; ST 14 Siła lub przewrócenie.",
    "Orka": "Ugryzienie: +6 do trafienia, 5k6+4 obrażeń kłutych.",
    "Słoń": "Wielokrotny atak: cios kłem +8, 3k8+6 kłutych oraz tratowanie +8, 3k10+6 obuchowych.",
    "Stegozaur": "Ogon: +7 do trafienia, 6k6+5 obrażeń kłutych; cel musi być za stworzeniem.",
    "Gigantyczny Krokodyl": "Wielokrotny atak: ugryzienie +8, 3k10+5 kłutych oraz ogon +8, 2k8+5 obuchowych.",
    "Triceratops": "Gore: +9 do trafienia, 4k8+6 obrażeń kłutych; kopyta: +9, 3k10+6 obuchowych po szarży.",
    "Mamut": "Wielokrotny atak: gore +9, 4k8+7 kłutych oraz tratowanie +9, 4k10+7 obuchowych.",
}

for _forms in WILD_SHAPE_FORMS.values():
    for _form in _forms:
        _details = _WILD_SHAPE_DETAILS.get(_form["name"])
        if _details:
            _form.update({
                "type": _details[0],
                "ability_scores": _details[1],
                "skills": _details[2],
                "senses": _details[3],
                "special_abilities": _details[4],
            })
            _form["action_details"] = _WILD_SHAPE_ACTIONS.get(_form["name"], _form.get("attacks", "-"))
            _form.setdefault("saving_throws", "brak")
            _form.setdefault("damage_resistances", "brak")
            _form.setdefault("damage_immunities", "brak")
            _form.setdefault("condition_immunities", "brak")
            _form.setdefault("languages", "brak")
            _form.setdefault("challenge", f"CR {_form.get('cr', '-')}; biegłość +{2 + int(float(_form.get('cr', 0)) // 4)}")

    ELEMENTAL_FORMS = [
        {
            "name": "Żywiołak Powietrza", "name_en": "Air Elemental", "cr": 5,
            "hp": 90, "ac": 15, "speed": "lot 27m (zawis)", "type": "Duży żywiołak",
            "ability_scores": "14, 20, 14, 6, 10, 6", "skills": "", "senses": "Mroczne widzenie 18 m; ślepowidzenie 18 m",
            "special_abilities": "Forma powietrzna; może przechodzić przez przestrzeń stworzeń i małych otworów.",
            "attacks": "Wielokrotny atak: 2 uderzenia.",
            "action_details": "Uderzenie: +8 do trafienia, 2k8+5 obrażeń obuchowych. Wir: stworzenia w przestrzeni wykonują ST 13 Siła.",
            "features": "Wir może przewracać i przenosić stworzenia; odporność na niemagiczne obrażenia obuchowe, kłute i tnące."
        },
        {
            "name": "Żywiołak Ziemi", "name_en": "Earth Elemental", "cr": 5,
            "hp": 126, "ac": 17, "speed": "9m, kopanie 9m", "type": "Duży żywiołak",
            "ability_scores": "20, 8, 20, 5, 10, 5", "skills": "", "senses": "Mroczne widzenie 18 m; tremorsense 18 m",
            "special_abilities": "Przebijanie przez ziemię; może przechodzić przez kamień i ziemię bez naruszania konstrukcji.",
            "attacks": "Wielokrotny atak: 2 uderzenia.",
            "action_details": "Uderzenie: +8 do trafienia, 2k8+5 obrażeń obuchowych.",
            "features": "Odporność na niemagiczne obrażenia obuchowe, kłute i tnące."
        },
        {
            "name": "Żywiołak Ognia", "name_en": "Fire Elemental", "cr": 5,
            "hp": 102, "ac": 13, "speed": "15m", "type": "Duży żywiołak",
            "ability_scores": "10, 17, 16, 6, 10, 7", "skills": "", "senses": "Mroczne widzenie 18 m",
            "special_abilities": "Forma ognia; podpala obiekty i przechodzi przez szczeliny; odporność na ogień.",
            "attacks": "Wielokrotny atak: 2 dotknięcia.",
            "action_details": "Dotknięcie: +6 do trafienia, 2k6+3 obrażeń od ognia; cel może zapłonąć.",
            "features": "Odporność na obrażenia obuchowe, kłute i tnące; niewrażliwość na ogień i truciznę."
        },
        {
            "name": "Żywiołak Wody", "name_en": "Water Elemental", "cr": 5,
            "hp": 114, "ac": 14, "speed": "9m, pływanie 27m", "type": "Duży żywiołak",
            "ability_scores": "18, 14, 18, 5, 10, 8", "skills": "", "senses": "Ślepowidzenie 18 m",
            "special_abilities": "Forma wodna; może wejść w przestrzeń stworzenia i przeciskać się przez szczeliny.",
            "attacks": "Wielokrotny atak: 2 uderzenia.",
            "action_details": "Uderzenie: +7 do trafienia, 2k8+4 obrażeń obuchowych. Wir: ST 15 Siła, 2k8 obrażeń i pochwycenie.",
            "features": "Odporność na niemagiczne obrażenia obuchowe, kłute i tnące; oddycha pod wodą."
        },
    ]

    for _elemental in ELEMENTAL_FORMS:
        _elemental.update({
            "saving_throws": "brak",
            "damage_resistances": "kwas, zimno, ogień, pioruny, grzmoty",
            "damage_immunities": "trucizna",
            "condition_immunities": "wyczerpanie, skrępowanie, paraliż, skamienienie, zatrucie, przewrócenie",
            "languages": "Auran / Terran / Ignan / Aquan (zależnie od formy)",
            "challenge": "CR 5; biegłość +3",
        })
