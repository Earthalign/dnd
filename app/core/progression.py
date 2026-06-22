"""
D&D 5e Level Progression Tables (PHB).
All spell slot tables, subclass definitions, class features by level,
and core progression mechanics for levels 1-20.
"""

# Proficiency bonus by character level
PROFICIENCY_BY_LEVEL = {
    1: 2, 2: 2, 3: 2, 4: 2, 5: 3, 6: 3, 7: 3, 8: 3,
    9: 4, 10: 4, 11: 4, 12: 4, 13: 5, 14: 5, 15: 5, 16: 5,
    17: 6, 18: 6, 19: 6, 20: 6,
}

# XP thresholds per level
XP_BY_LEVEL = {
    1: 0, 2: 300, 3: 900, 4: 2700, 5: 6500, 6: 14000, 7: 23000, 8: 34000,
    9: 48000, 10: 64000, 11: 85000, 12: 100000, 13: 120000, 14: 140000,
    15: 165000, 16: 195000, 17: 225000, 18: 265000, 19: 305000, 20: 355000,
}

# ─── Full Caster Spell Slots (Bard, Cleric, Druid, Sorcerer, Wizard) ───
# Format: level -> [slot_1, slot_2, slot_3, slot_4, slot_5, slot_6, slot_7, slot_8, slot_9]
FULL_CASTER_SLOTS = {
    1:  [2,0,0,0,0,0,0,0,0],
    2:  [3,0,0,0,0,0,0,0,0],
    3:  [4,2,0,0,0,0,0,0,0],
    4:  [4,3,0,0,0,0,0,0,0],
    5:  [4,3,2,0,0,0,0,0,0],
    6:  [4,3,3,0,0,0,0,0,0],
    7:  [4,3,3,1,0,0,0,0,0],
    8:  [4,3,3,2,0,0,0,0,0],
    9:  [4,3,3,3,1,0,0,0,0],
    10: [4,3,3,3,2,0,0,0,0],
    11: [4,3,3,3,2,1,0,0,0],
    12: [4,3,3,3,2,1,0,0,0],
    13: [4,3,3,3,2,1,1,0,0],
    14: [4,3,3,3,2,1,1,0,0],
    15: [4,3,3,3,2,1,1,1,0],
    16: [4,3,3,3,2,1,1,1,0],
    17: [4,3,3,3,2,1,1,1,1],
    18: [4,3,3,3,3,1,1,1,1],
    19: [4,3,3,3,3,2,1,1,1],
    20: [4,3,3,3,3,2,2,1,1],
}

# ─── Half Caster Spell Slots (Paladin, Ranger) ───
HALF_CASTER_SLOTS = {
    1:  [0,0,0,0,0], 2: [2,0,0,0,0], 3: [3,0,0,0,0], 4: [3,0,0,0,0],
    5:  [4,2,0,0,0], 6: [4,2,0,0,0], 7: [4,3,0,0,0], 8: [4,3,0,0,0],
    9:  [4,3,2,0,0], 10:[4,3,2,0,0], 11:[4,3,3,0,0], 12:[4,3,3,0,0],
    13: [4,3,3,1,0], 14:[4,3,3,1,0], 15:[4,3,3,2,0], 16:[4,3,3,2,0],
    17: [4,3,3,3,1], 18:[4,3,3,3,1], 19:[4,3,3,3,2], 20:[4,3,3,3,2],
}

# ─── Warlock Pact Magic ───
# Format: level -> {slots: count, slot_level: level}
WARLOCK_SLOTS = {
    1:  {"slots": 1, "slot_level": 1},
    2:  {"slots": 2, "slot_level": 1},
    3:  {"slots": 2, "slot_level": 2},
    4:  {"slots": 2, "slot_level": 2},
    5:  {"slots": 2, "slot_level": 3},
    6:  {"slots": 2, "slot_level": 3},
    7:  {"slots": 2, "slot_level": 4},
    8:  {"slots": 2, "slot_level": 4},
    9:  {"slots": 2, "slot_level": 5},
    10: {"slots": 2, "slot_level": 5},
    11: {"slots": 3, "slot_level": 5},
    12: {"slots": 3, "slot_level": 5},
    13: {"slots": 3, "slot_level": 5},
    14: {"slots": 3, "slot_level": 5},
    15: {"slots": 3, "slot_level": 5},
    16: {"slots": 3, "slot_level": 5},
    17: {"slots": 4, "slot_level": 5},
    18: {"slots": 4, "slot_level": 5},
    19: {"slots": 4, "slot_level": 5},
    20: {"slots": 4, "slot_level": 5},
}

# ─── Cantrips Known by Level ───
CANTRIPS_KNOWN = {
    "bard":     {1:2, 4:3, 10:4},
    "cleric":   {1:3, 4:4, 10:5},
    "druid":    {1:2, 4:3, 10:4},
    "sorcerer": {1:4, 4:5, 10:6},
    "warlock":  {1:2, 4:3, 10:4},
    "wizard":   {1:3, 4:4, 10:5},
}

# ─── Spells Known (for known-casters: Bard, Ranger, Sorcerer, Warlock) ───
SPELLS_KNOWN = {
    "bard":     {1:4,2:5,3:6,4:7,5:8,6:9,7:10,8:11,9:12,10:14,11:15,12:15,13:16,14:18,15:19,16:19,17:20,18:22,19:22,20:22},
    "ranger":   {1:0,2:2,3:3,4:3,5:4,6:4,7:5,8:5,9:6,10:6,11:7,12:7,13:8,14:8,15:9,16:9,17:10,18:10,19:11,20:11},
    "sorcerer": {1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11,11:12,12:12,13:13,14:13,15:14,16:14,17:15,18:15,19:15,20:15},
    "warlock":  {1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:10,11:11,12:11,13:12,14:12,15:13,16:13,17:14,18:14,19:15,20:15},
}

# ─── Max Spell Level Accessible ───
FULL_CASTER_MAX_SPELL_LEVEL = {
    1:1, 2:1, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4, 9:5, 10:5,
    11:6, 12:6, 13:7, 14:7, 15:8, 16:8, 17:9, 18:9, 19:9, 20:9,
}
HALF_CASTER_MAX_SPELL_LEVEL = {
    1:0, 2:1, 3:1, 4:1, 5:2, 6:2, 7:2, 8:2, 9:3, 10:3,
    11:3, 12:3, 13:4, 14:4, 15:4, 16:4, 17:5, 18:5, 19:5, 20:5,
}

# ─── Subclass Selection Level per Class ───
SUBCLASS_LEVEL = {
    "barbarian": 3, "bard": 3, "cleric": 1, "druid": 2,
    "fighter": 3, "monk": 3, "paladin": 3, "ranger": 3,
    "rogue": 3, "sorcerer": 1, "warlock": 1, "wizard": 2,
}

# ─── Subclass Definitions ───
SUBCLASSES = {
    "barbarian": {
        "berserker": {
            "name": "Ścieżka Berserkera", "name_en": "Path of the Berserker",
            "description": "Dla niektórych szał to nie tylko furia, to trans. Berserker ignoruje ból i walczy z furią, której inni nie potrafią pojąć.",
            "description_en": "For some, their rage is more than a display of fury, it is a trance. A berserker ignores pain and fights with unimaginable fury.",
            "features": {
                3: ["Szał (Frenzy): Możesz wejść w Furię podczas szału, wykonując dodatkowy atak wręcz w akcji bonusowej, ale zyskujesz 1 poziom wyczerpania po zakończeniu szału."],
                6: ["Bezmyślny Szał (Mindless Rage): Odporność na zauroczenie i przerażenie podczas szału."],
                10: ["Zastraszająca Obecność (Intimidating Presence): Możesz użyć akcji do przerażenia wroga w promieniu 9m."],
                14: ["Odwet (Retaliation): Gdy otrzymujesz obrażenia od sąsiadującego wroga, możesz w reakcji wykonać atak wręcz."]
            }
        },
        "totem_warrior": {
            "name": "Ścieżka Wojownika Totemu", "name_en": "Path of the Totem Warrior",
            "description": "Akceptujesz ducha zwierzęcia by przewodził Ci, chronił i inspirował. Łączysz w sobie brutalność z mistycyzmem.",
            "description_en": "You accept a spirit animal as guide, protector, and inspiration. You blend ferocity with mysticism.",
            "features": {
                3: ["Poszukiwacz Dusz (Spirit Seeker): Możesz rzucać Rozmowę ze zwierzętami i Zmysł bestii jako rytuały.", "Duch Totemu (Totem Spirit): Wybierasz zwierzę (np. Niedźwiedź daje odporność na wszystkie obrażenia poza psychicznymi w szale)."],
                6: ["Aspekt Bestii (Aspect of the Beast): Zyskujesz magiczne korzyści ze swojego wybranego zwierzęcia, m.in. zmysły, siłę udźwigu, lub zwinność."],
                10: ["Duch Wędrowiec (Spirit Walker): Możesz rzucać Wspólnotę z Naturą jako rytuał."],
                14: ["Zestrojenie Totemiczne (Totemic Attunement): Twoje zwierzę nadaje Ci kolejne potężne zdolności do wsparcia i ataku."]
            }
        },
    },
    "bard": {
        "lore": {
            "name": "Kolegium Wiedzy", "name_en": "College of Lore",
            "description": "Gromadzisz sekrety i opowieści ze wszystkich zakątków świata. Używasz magii słowa by zmylić wrogów.",
            "description_en": "You gather secrets from everywhere. You use the magic of words to confuse your foes.",
            "features": {
                3: ["Dodatkowe Biegłości: Wybierz 3 dodatkowe umiejętności.", "Cięte Słowa (Cutting Words): Możesz zużyć Bardowską Inspirację by obniżyć rzut na atak, obrażenia lub test cechy przeciwnika."],
                6: ["Dodatkowe Magiczne Sekrety: Poznaj 2 zaklęcia z dowolnej klasy."],
                14: ["Niezrównane Umiejętności (Peerless Skill): Możesz dodać rzut Bardowską Inspiracją do własnego testu umiejętności."]
            }
        },
        "valor": {
            "name": "Kolegium Waleczności", "name_en": "College of Valor",
            "description": "Błędy to bardowie bitewni, którzy z pieśnią na ustach prowadzą wojowników do boju i dokumentują ich chwałę.",
            "description_en": "Bards who sing songs of heroes while fighting in the front lines alongside them.",
            "features": {
                3: ["Biegłość w Walce: Biegłość w średnim pancerzu, tarczach i broniach wojskowych.", "Inspiracja Bitewna (Combat Inspiration): Sojusznicy mogą doliczyć kość inspiracji do zadanych obrażeń lub swojej KP."],
                6: ["Dodatkowy Atak: Wykonujesz dwa ataki zamiast jednego akcją Ataku."],
                14: ["Magia i Broń (Battle Magic): Gdy rzucasz zaklęcie jako akcję, możesz wykonać atak bronią jako akcję bonusową."]
            }
        },
    },
    "cleric": {
        "knowledge": {
            "name": "Domena Wiedzy", "name_en": "Knowledge Domain",
            "description": "Skupiasz się na odnajdywaniu prawdy, badaniu historii i odkrywaniu tajemnic, które inni woleliby zapomnieć.",
            "description_en": "You focus on the pursuit of truth, history and secrets.",
            "features": {
                1: ["Błogosławieństwo Wiedzy: Biegłość i podwójna premia w 2 z: Arkana, Historia, Przyroda, Religia.", "Zaklęcia Domeny."],
                2: ["Użycie Boskości: Zyskaj wiedzę. Przez 10 min masz biegłość w wybranym narzędziu/umiejętności."],
                6: ["Użycie Boskości: Czytanie w Myślach."],
                8: ["Potężne Rzucanie Zaklęć: Dodaj modyfikator Mądrości do obrażeń ze sztuczek."],
                17: ["Wizje z Przeszłości: Widzisz przebłyski wydarzeń z przeszłości przedmiotów lub obszarów."]
            }
        },
        "life": {
            "name": "Domena Życia", "name_en": "Life Domain",
            "description": "Mistrzowie magii leczącej. Zabezpieczają zdrowie i podnoszą poległych by dalej służyli dobru.",
            "description_en": "Masters of healing magic, they restore health and bring back the fallen.",
            "features": {
                1: ["Ciężki Pancerz: Biegłość w ciężkim pancerzu.", "Uczeń Życia: Czary leczące leczą dodatkowo 2 + poziom czaru PW."],
                2: ["Użycie Boskości: Zachowanie Życia. Pula leczenia do rozdzielenia."],
                6: ["Błogosławiony Uzdrowiciel: Lecząc innych zaklęciem sam odzyskujesz 2 + poziom zaklęcia PW."],
                8: ["Boskie Uderzenie: Dodaj 1k8 obrażeń radiacyjnych raz na turę do ataku bronią."],
                17: ["Najwyższe Leczenie: Rzuty kośćmi podczas leczenia używają zawsze najwyższej możliwej wartości."]
            }
        },
        "light": {
            "name": "Domena Światła", "name_en": "Light Domain",
            "description": "Wyznawcy ideałów ognia, odrodzenia i prawdy, którzy spopielają nieumarłych mocom słońca.",
            "description_en": "Followers of fire, rebirth, and truth, they burn the undead with solar power.",
            "features": {
                1: ["Dodatkowa Sztuczka (Światło).", "Rozbłysk Ochronny (Warding Flare): Narzucasz niekorzyść na atak skierowany przeciwko tobie za pomocą błysku światła."],
                2: ["Użycie Boskości: Blask Świtu. Tworzysz wokół wybuch magicznego światła."],
                6: ["Wspólny Rozbłysk: Możesz chronić też sojusznika oddalonego do 9m."],
                8: ["Potężne Rzucanie Zaklęć: Dodaj mod Wis do sztuczek."],
                17: ["Korona Światła: Uwalniasz aurę światła (18m). Przeciwnicy mają niekorzyść na rzuty na ogień/światłość."]
            }
        },
        "nature": {
            "name": "Domena Natury", "name_en": "Nature Domain",
            "description": "Bogowie natury udzielają Ci mocy panowania nad florą i fauną.",
            "description_en": "Gods of nature grant you power over flora and fauna.",
            "features": {
                1: ["Akolita Natury: Jedna sztuczka Druida oraz Biegłość (Zwierzęta, Przyroda lub Przetrwanie). Biegłość w Ciężkich zbrojach."],
                2: ["Użycie Boskości: Zauroczenie zwierząt/roślin na 1 minutę."],
                6: ["Tłumienie Żywiołów: Reakcją zmniejszasz obrażenia od żywiołów o połowę dla wybranej postaci."],
                8: ["Boskie Uderzenie: +1k8 obrażeń żywiołów raz na turę do broni."],
                17: ["Mistrz Natury: Przejmujesz całkowitą kontrolę nad wezwanymi roślinami i zwierzętami."]
            }
        },
        "tempest": {
            "name": "Domena Burzy", "name_en": "Tempest Domain",
            "description": "Uosobienie niszczycielskiej furii natury – trzęsień ziemi, huraganów i błyskawic.",
            "description_en": "The embodiment of nature's destructive fury – earthquakes, hurricanes, and lightning.",
            "features": {
                1: ["Gniew Burzy: Kiedy zostaniesz uderzony, odbijasz piorun zadający 2k8 obrażeń.", "Biegłość w broniach żołnierskich i Ciężkim pancerzu."],
                2: ["Użycie Boskości: Maksymalizujesz obrażenia zadawane czarami od gromu lub błyskawicy."],
                6: ["Twardy jak Sztorm: Gdy uderzysz wroga piorunem, możesz pchnąć go o 3m."],
                8: ["Boskie Uderzenie: Dodajesz +1k8 do ataku wręcz (Błyskawice)."],
                17: ["Dziecko Burzy: Lot na zewnątrz, podczas burzy/wiatru."]
            }
        },
        "trickery": {
            "name": "Domena Podstępu", "name_en": "Trickery Domain",
            "description": "Bogowie podstępu i złodziejstwa czynią cię mistrzem iluzji, manipulacji i kamuflażu.",
            "description_en": "Gods of trickery and theft make you a master of illusion and manipulation.",
            "features": {
                1: ["Błogosławieństwo Podstępu: Dajesz celowi przewagę w Skradaniu się na godzinę."],
                2: ["Użycie Boskości: Bliźniak. Tworzysz swoją iluzję by rozproszyć przeciwników."],
                6: ["Peleryna Cieni: Możesz zniknąć z oczu do końca tury używając akcji."],
                8: ["Boskie Uderzenie: Dodajesz +1k8 obrażeń trucizną."],
                17: ["Poprawiony Bliźniak: Aż 4 kopie ciebie!"]
            }
        },
        "war": {
            "name": "Domena Wojny", "name_en": "War Domain",
            "description": "Klerycy wojny to mistrzowie walki, łączący moc boga z niezrównaną sprawnością fizyczną na polu bitwy.",
            "description_en": "War clerics are masters of combat, blending god's power with physical prowess.",
            "features": {
                1: ["Zbrojny Wojownik: Biegłość w broniach bojowych i ciężkim pancerzu.", "Kapłan Wojenny: Możesz uderzyć dodatkowo w akcji bonusowej po użyciu Akcji Atak."],
                2: ["Użycie Boskości: +10 do chybionego Rzutu Ataku."],
                6: ["Płaszcz Wojenny: Dajesz bonus +10 do uderzenia wroga koledze z drużyny."],
                8: ["Boskie Uderzenie: +1k8 fizycznych obrażeń w ataku na turę."],
                17: ["Awatara Bitwy: Masz wrodzoną oporność na obrażenia zadawane bronią nienamagnetyzowaną (kłute, obuchowe, rąbane)."]
            }
        }
    },
    "druid": {
        "land": {
            "name": "Krąg Ziemi", "name_en": "Circle of the Land",
            "description": "Druid skupiony na rzucaniu czarów. Posiadasz sekrety ze specjalnie połączonego krajobrazu.",
            "description_en": "A druid focused on casting spells, tied to a specific landscape.",
            "features": {
                2: ["Bonusowa sztuczka z listy Druida.", "Naturalne Odzyskanie: Podróżuj, regeneruj zaklęcia równe połowie lvl podczas odpoczynku."],
                6: ["Ziemia w sercu: Poruszasz się poprzez trudny teren bez strat, jesteś obroniony przed zatruciami / czarami ziemi."],
                10: ["Sanktuarium Natury: Twoje istnienie odsuwa magiczne stwory. Mają problem Cię atakować."],
                14: ["Ochrona Natury: Brak obrażeń od trucizn, odporność na charkterystyczne debuffy z magii natury / zarazy."]
            }
        },
        "moon": {
            "name": "Krąg Księżyca", "name_en": "Circle of the Moon",
            "description": "Przemieniasz się potężne, dzikie bestie, by w zwarciu niszczyć swych wrogów.",
            "description_en": "You transform into powerful beasts to tear enemies apart in melee combat.",
            "features": {
                2: ["Dzika Postać w Akcji Bonusowej.", "Przemiana bojowa: Możesz przemienić się w potężniejsze bestie o skali do 1 ST (np. Niedźwiedź)."],
                6: ["Pierwotne Uderzenia: Ataki bestii ignorują pancerz fizyczny (traktowane jak magiczne). Możesz zmienić się w Bestię do skali CR=lvl/3."],
                10: ["Przemiana Żywiołaka: Zyskujesz potężne formy Żywiołaków (Ognia, Ziemi, etc) za 2 ładunki przemiany."],
                14: ["Tysiące Twarzy Księżyca: Możesz dowolnie modyfikować swój wygląd."]
            }
        },
    },
    "fighter": {
        "champion": {
            "name": "Czempion", "name_en": "Champion",
            "description": "Skupiasz się na surowej sile fizycznej, doprowadzając ją do morderczej perfekcji.",
            "description_en": "You focus on raw physical perfection, landing deadly blows.",
            "features": {
                3: ["Krytyk na 19-20 z każdej broni."],
                7: ["Niezrównany Lekkoatleta: Biegłość lub podwójna wartość do umiejętności Atleyki. Szybkie skoki."],
                10: ["Nowy styl walki: Otrzymujesz 2. styl Walki z podstawowego zestawu."],
                15: ["Krytyk potężny na 18-20 na kostce d20."],
                18: ["Samoleczenie: Regenerujesz co turę HP podczas gdy masz mniej niż 50% max HP."]
            }
        },
        "battlemaster": {
            "name": "Mistrz Bitewny", "name_en": "Battle Master",
            "description": "Używasz specjalnych manewrów bojowych, by zyskać taktyczną przewagę na polu walki.",
            "description_en": "You use special maneuvers to gain tactical advantages.",
            "features": {
                3: ["Kości Wyższości: Dostajesz 4 kości (k8). Używasz ich by wzmacniać ataki lub wspierać rzuty."],
                7: ["Studium Przeciwnika: Przez godzinę poznajesz atrybuty oponenta na podstawie obserwacji."],
                10: ["Mocniejsze kości: Kości wyższości awansują na (k10)."],
                15: ["Podratowanie: Kiedy wchodzisz w starcie nie mając manewrów, odzyskujesz jeden z automatu."],
                18: ["Najmocniejsze kości: Twoje kości wyższości używają wskaźnika (k12)."]
            }
        },
        "eldritch_knight": {
            "name": "Eldryczny Rycerz", "name_en": "Eldritch Knight",
            "description": "Wykorzystujesz magię Czarodzieja, by wzmocnić swoje uderzenia mieczem i przetrwać bitwy.",
            "description_en": "You use wizard magic to boost your sword strikes.",
            "features": {
                3: ["Rzucanie Zaklęć (Zaklęcia Czarodzieja).", "Związana Broń: Możesz wezwać broń z każdego miejsca w rękę w Turze."],
                7: ["Magia Wojny: Rzucając sztuczkę, używasz akcji bonusowej na zwykły atak w zwarciu."],
                10: ["Rozdarcie magiczne: Przeciwnik trafiony bronią ma niekorzyść do rzutów obronnych na Twój następny czar."],
                15: ["Zaklęte odbicie: Używając Action Surge, teleportujesz się o 9m."],
                18: ["Rozszerzona Magia Wojny: Rzucając zaklęcie używasz akcji bonusowej na zwykły atak."]
            }
        },
    },
    "monk": {
        "open_hand": {
            "name": "Droga Otwartej Dłoni", "name_en": "Way of the Open Hand",
            "description": "Tradycyjny mnich, mistrz uderzeń bezbronnych, który wykorzystuje Ki by obalać lub powstrzymywać wrogów.",
            "description_en": "Master of unarmed strikes, utilizing Ki to topple foes.",
            "features": {
                3: ["Otwarte Dłonie: Flurry of Blows mogą teraz: odepchnąć przeciwnika, podciąć go, lub zablokować mu używanie Reakcji."],
                6: ["Integralność: Magicznie potrafisz samo-uleczyć się."],
                11: ["Zastój Umysłu: Trwały buff chroni Cię przed atakami po obudzeniu każdego dnia."],
                17: ["Drżąca Dłoń: Dotykając rywala dajesz wrogowi wibracje zabijające go po czasie."]
            }
        },
        "shadow": {
            "name": "Droga Cienia", "name_en": "Way of Shadow",
            "description": "Ninja i cisi mordercy opierający swoje zdolności na ciemności.",
            "description_en": "Ninja and silent assassins who rely on darkness.",
            "features": {
                3: ["Magia Cieni: Rzucasz pomniejsze czary Cienia (Ciemność, Krok Mgły, Milczenie) przez KI. Sztuczka Iluzja Cienia."],
                6: ["Krok Cienia: W warunkach niskiego światła skaczesz między cieniem a cieniem (18m) akcją bonusową i uzyskujesz Przewagę!"],
                11: ["Niewidzialność Cienia: W słabym świetle stajesz się magicznie niewidzialny do ataku."],
                17: ["Odbicie Złodzieja: Uderzasz z Reakcji gdy sojusznik zaatakował."]
            }
        },
        "four_elements": {
            "name": "Droga Czterech Żywiołów", "name_en": "Way of the Four Elements",
            "description": "Mnich naginający wodę, ogień, wiatr i ziemię jak Avatar.",
            "description_en": "A monk that bends water, fire, wind, and earth.",
            "features": {
                3: ["Adept Żywiołów: Używasz punktów Ki do wywołania czarów żywiołowych."],
                6: ["Rozszerzenie Elementów: Kolejna dyscyplina, wyższy limit punktów Ki na atak."],
                11: ["Mistrz Elementów: Trzecia dyscyplina."],
                17: ["Avatar Żywiołów: Czwarta dyscyplina i bardzo potężne zaklecia odblokowane."]
            }
        },
    },
    "paladin": {
        "devotion": {
            "name": "Przysięga Oddania", "name_en": "Oath of Devotion",
            "description": "Klasyczny święty rycerz w lśniącej zbroi, stawiający na prawość i honor.",
            "description_en": "Classic holy knight in shining armor, acting with honor.",
            "features": {
                3: ["Święta Broń: Użycie Boskości do nakładania modyfikatora Charyzmy do Ataków broni."],
                7: ["Aura Oddania: Promień 3m - Ty i towarzysze nie dacie się Zauroczyć magią."],
                15: ["Czystość Ducha: Zawsze aktywna Ochrona przed Dobrem i Złem."],
                20: ["Aureola: Promień 9m wrogowie otrzymują obrażenia, a Ty masz przewagę nad magią ciemności."]
            }
        },
        "ancients": {
            "name": "Przysięga Starożytnych", "name_en": "Oath of the Ancients",
            "description": "Przysięga chroniąca światło, piękno i naturę na Ziemi. Zielony Rycerz.",
            "description_en": "Green Knight swearing to protect light, beauty and nature.",
            "features": {
                3: ["Użycie Boskości: Pnącza atakujące i zakorzeniające przeciwnika."],
                7: ["Aura Ochrony: Masz i rozdajesz obniżenie Obrażeń Magicznych o połowę!"],
                15: ["Nieśmiertelny Odpoczynek: Odmładzasz się, gdy zejdziesz do 0 HP, cofasz do 1 HP."],
                20: ["Strażnik Natury: Pasywne szybkie zaklęcia z przewagą, samouleczanie się, korzenie do kontroli przeciwników."]
            }
        },
        "vengeance": {
            "name": "Przysięga Zemsty", "name_en": "Oath of Vengeance",
            "description": "Inkwizytorzy i ślepi łowcy, nie zważający na własną moralność - cel uświęca środki.",
            "description_en": "Inquisitors focused purely on eliminating the greater evil.",
            "features": {
                3: ["Użycie Boskości: Przysięga Wrogości - ciągła Przewaga na ataki wymierzone w wybranego wroga."],
                7: ["Nieubłagany Ścigający: Kiedy atakujesz okazyjnie z reakcji, możesz przenieść się z prędkością równą połowie swej bazy w ślad za nim."],
                15: ["Dusza Mściciela: Używając Przysięgi Wrogości, atakującego cię wroga uderzasz w odpowiedzi reakcją."],
                20: ["Anioł Zniszczenia: Otrzymujesz na godzinę skrzydła Latające i Przerażającą aurę."]
            }
        },
    },
    "ranger": {
        "hunter": {
            "name": "Łowca", "name_en": "Hunter",
            "description": "Skupiony na walce i zabijaniu konkretnych typów wrogów. Łowcy to żołnierze z lasu wyspecjalizowani w niszczeniu zagrożeń.",
            "description_en": "Focused on tracking and killing specific threats.",
            "features": {
                3: ["Zdobycz Łowcy: Do wyboru, np. Zabójca Kolosów (+1k8 obrażeń)."],
                7: ["Taktyka Defensywna: Obrona przed atakami z rzędu lub ucieczka z hordy."],
                11: ["Wielorakie Ataki: Atakowanie obszarowe wieloma ciosami broni."],
                15: ["Wyższa Obronność Łowcy: Uniki, Tarcza z reakcji zmniejszająca obrażenia."]
            }
        },
        "beast_master": {
            "name": "Władca Bestii", "name_en": "Beast Master",
            "description": "Posiada na stałe wierne i niebezpieczne zwierzę u swego boku walczące i patrolujące z łowcą.",
            "description_en": "Commands a loyal beast companion.",
            "features": {
                3: ["Towarzysz Bojowy: Zyskujesz Bestię, która dostaje prof bonus do statów. Kierujesz nią jako Twoja akcja."],
                7: ["Wyjątkowe Szkolenie: Zwierzę może używać akcji bonusowej np do Uniku, Odskoku na Twoje polecenie."],
                11: ["Zwierzęca Furia: Bestia atakuje 2 razy podczas wydania rozkazu ataku."],
                15: ["Współdzielenie Zaklęć: Kiedy rzucasz na siebie zaklęcie, rzucasz je również na zwierzę przebywające w obrębie 9m."]
            }
        },
    },
    "rogue": {
        "thief": {
            "name": "Złodziej", "name_en": "Thief",
            "description": "Klasyczny przestępca, szybkie ręce i perfekcyjna wspinaczka oraz łamanie zamków w locie.",
            "description_en": "Classic thief with fast hands and perfect climbing.",
            "features": {
                3: ["Szybkie Ręce: Akcja Użyj Przedmiotu staje się Akcją Bonusową.", "Wspinaczka bez straty prędkości."],
                9: ["Skrytość W Najwyższym Wydaniu: Poruszając się wolno zyskujesz przewagę na Skradanie."],
                13: ["Sztuczki Magiczne Złodzieja: Ignorujesz wymagania z klas dla Magicznych Przedmiotów."],
                17: ["Szybki Odruch: Kiedy zaczyna się Walka w pierwszym starciu otrzymujesz dwie tury z rzędu."]
            }
        },
        "assassin": {
            "name": "Zabójca", "name_en": "Assassin",
            "description": "Ekspert od zabójstwa pojedynczych celów, przebierania się oraz wykorzystywania trucizn.",
            "description_en": "Master of single-target elimination, disguise and poisons.",
            "features": {
                3: ["Biegłość: Narzędzia Truciciela, Przebranie.", "Skrytobójca: Masz przewagę na ataki wobec wrogów, którzy jeszcze nie mieli tury. Trafienie zaskoczonego to Krytyk."],
                9: ["Doskonałe Tożsamości: Perfekcyjnie fabrykujesz tło uchodźcy/żołnierza z historią i fałszywymi danymi."],
                13: ["Oszust - Słowa: Perfekcyjnie powtarzasz akcent i mowę innej osoby."],
                17: ["Zabójcze Uderzenie Śmierci: Zaskoczony wróg otrzymuje podwójne obrażenia, jeśli nie zda rzutu na Kondycję."]
            }
        },
        "arcane_trickster": {
            "name": "Tajemny Szachraj", "name_en": "Arcane Trickster",
            "description": "Magiczny oszust używający zaklęć iluzji oraz niewidzialnej ręki do kradzieży.",
            "description_en": "Magical scoundrel using illusions and mage hand.",
            "features": {
                3: ["Rzucanie Zaklęć (Iluzje/Zaczarowania).", "Magiczna Dłoń: Twoja dłoń jest Niewidzialna. Kradnie i rozbraja zamki z daleka Akcją Bonusową!"],
                9: ["Magiczna Zasadzka: Kiedy rzucasz z ukrycia z zaskoczenia, cel ma niekorzyść w obronie przed twoim czarem."],
                13: ["Magiczny Szachraj: Twoja Magiczna Dłoń rozprasza wroga dając Ci Przewagę (Advantage) na ataki."],
                17: ["Kradzież Zaklęcia: Kradniesz magiczne zaklęcie rzucane przez przeciwnika, zabraniając mu go używać."]
            }
        },
    },
    "sorcerer": {
        "draconic": {
            "name": "Rodowód Smoka", "name_en": "Draconic Bloodline",
            "description": "Twoja magia pochodzi od smoczego przodka. Posiadasz twarde łuski i odporności żywiołowe.",
            "description_en": "Magic born of a dragon ancestor. You possess hard scales and elemental affinity.",
            "features": {
                1: ["Potężne Zdrowie: +1 HP za poziom. Bazowe AC bez pancerza = 13 + Zr.", "Wybierz Smoka (żywioł)."],
                6: ["Zgodność Elementarna: Dodaj modyfikator Cha do obrażeń twojego elementu smoczego i dostań oporność na niego na 1 godzinę za punkt magii."],
                14: ["Smocze Skrzydła: Wyrastają ci smocze skrzydła dające szybkość latania równą twojej prędkości chodu."],
                18: ["Aura Strachu: Emanujesz aurą przerażenia wokół siebie wydając punkt magii."]
            }
        },
        "wild_magic": {
            "name": "Dzika Magia", "name_en": "Wild Magic",
            "description": "Zmienność, zawirowania i czysty potok kapryśnej Mocy wpływają na twoje wybuchowe ataki.",
            "description_en": "Chaotic surges of power influence your explosive spells.",
            "features": {
                1: ["Dziki Podmuch: GM może wywołać rzut na Tabelę Dzikiej Magii po rzuceniu zaklęcia poziomu 1+.", "Tides of Chaos: Otrzymujesz Zaletę na 1 rzut d20, po czym GM szybciej włącza tabelę Dzikiej Magii."],
                6: ["Wyginanie Szczęścia: Używając Punktów Magii możesz dodać lub ująć k4 do dowolnego rzutu obok ciebie."],
                14: ["Zapanowanie nad Dzikością: Od teraz zawsze rzucasz 2 razy na Tabelę Dzikich Efektów wybierając pożądany wynik."],
                18: ["Magiczne Zniszczenie: Rzucając max obrażenia z wybranej puli czarów, dodajesz kolejne rzuty kostką na obrażenia."]
            }
        },
    },
    "warlock": {
        "archfey": {
            "name": "Arcywróżka", "name_en": "The Archfey",
            "description": "Twoim patronem jest władca Feywild - domena czarującej magii, pęt i zauroczenia faerie.",
            "description_en": "Patron from the Feywild, master of enchanting magic.",
            "features": {
                1: ["Fey Presence: Emanujesz aurą przerażenia lub zauroczenia w promieniu 3 metrów raz na krótki odpoczynek."],
                6: ["Mglista Ucieczka (Misty Escape): Gdy otrzymasz obrażenia używasz Reakcji stając się niewidzialnym i teleportując 18m."],
                10: ["Beguiling Defenses: Jesteś odporny na urok. Możesz w reakcji odwrócić efekt zauroczenia przeciw atakującemu."],
                14: ["Mroczne Iluzje: Topisz wybranego wroga w koszmarze pełnym halucynacji w ramach akcji na 1 minutę."]
            }
        },
        "fiend": {
            "name": "Diabelski Patron", "name_en": "The Fiend",
            "description": "Twój patron pochodzi z niższych piekieł. Daje Ci destruktywną magię pożogi.",
            "description_en": "Fiendish patron granting destructive hellfire magic.",
            "features": {
                1: ["Mroczne Błogosławieństwo: Odzyskujesz Tymczasowe HP z Mod + Poziom Warlocka każdorazowo po zabiciu celu."],
                6: ["Piekielne Szczęście: Darmowa kość k10 do nieudanego testu Atrybutu lub rzutu obronnego."],
                10: ["Demon Ochronny: Zmieniasz po odpoczynku odporność na dany typ zniszczeń broni lub magii."],
                14: ["Piekielny Wymiar: Teleportujesz zaatakowanego wroga do Piekła na 1 rundę, po powrocie traci ogromne psychiczne HP (10k10)."]
            }
        },
        "great_old_one": {
            "name": "Wielki Przedwieczny", "name_en": "The Great Old One",
            "description": "Patron ukryty w odmętach kosmosu lub głębinach, uczy potęgi umysłowej i kontroli woli (Lovecraft).",
            "description_en": "Lovecraftian patron granting mental power and telepathy.",
            "features": {
                1: ["Telepatia Obudzona: Pasywna telepatia z dowolnym stworem dookoła 9m jeśli znasz język lub on go zna."],
                6: ["Przebłysk Woli: Jeśli atak wroga z gorszą Wolą Cię chybi zyskujesz nad nim z automatu Przewagę Ataku w swojej turze."],
                10: ["Magia Tarczy Umysłu: Jesteś odporny na psychiczne obrażenia z zewnątrz, i odbijasz taki atak w zadającego po równo!"],
                14: ["Zniewalanie: Nakładasz magiczną kontrolę we władanie nieświadomego lub obezwładnionego humanoida do puki inny Ci go nie rozproszy."]
            }
        },
    },
    "wizard": {
        "abjuration": {
            "name": "Szkoła Odrzucania", "name_en": "School of Abjuration",
            "description": "Specjalista w blokowaniu magii, obronach fizycznych i usuwaniu przekleństw z potężną magiczną barierą HP.",
            "description_en": "Specialist in blocking magic and defensive barriers.",
            "features": {
                2: ["Magiczna Bariera (Arcane Ward): Rzucając zaklęcie obronne ładujesz Magiczną Tarczę HP równą Poziom*2 + Mod_Int. Chłonie obrażenia za Ciebie."],
                6: ["Wysunięta Ochrona: Używasz swojej Bariery by pochłonąć na reakcję obrażenia zmierzające w kolegę z zespołu."],
                10: ["Mistrz Odcięcia Magii: Twoje Rozproszenie i Kontrzaklęcie otrzymują bonusowy modyfikator Twojej biegłości (Proficiency)."],
                14: ["Zaawansowana Odporność na Magię: Posiadasz odporność z urzędu przed atakami Magicznymi a testy Obronne wykonujesz z Przewagą."]
            }
        },
        "evocation": {
            "name": "Szkoła Wywoływania", "name_en": "School of Evocation",
            "description": "Nuker, kontrolujący elementy by niszczyć wszystko Kule Ognia itp.",
            "description_en": "Powerful nuker, master of destructive elements.",
            "features": {
                2: ["Rzeźbiarz Magii (Sculpt Spells): Rzucasz AOE chroniąc wybrane stwory w strefie uderzenia."],
                6: ["Niszczycielska Sztuczka: Kiedy sztuczka zadająca obrażenia nie trafi celu, cel i tak otrzymuje połowę bazy bez bonusów."],
                10: ["Wzmocnione Wywoływanie: Twoje zaklęcia evocation zdobywają twój Int Modifier wprost jako czysty zysk do DMG na 1 rolkę kości."],
                14: ["Przeciążenie (Overchannel): Rzucasz Max z kostek na DMG 1-5 lvla zaklęcia, za każdą kolejną pozycję psując samego siebie."]
            }
        },
        "illusion": {
            "name": "Szkoła Iluzji", "name_en": "School of Illusion",
            "description": "Mydlenie oczu, zmiana rzeczywistości percepcyjnej i unikanie zagrożeń.",
            "description_en": "Master of perception, blurring reality and evading threats.",
            "features": {
                2: ["Mniejsza Iluzja za darmo, do której dodajesz naraz Dźwięk oraz Obraz zamiast zaledwie jednego z tych aspektów."],
                6: ["Płynna Iluzja: Kiedy stworzysz stałą iluzję przez magię poziomu 1 lub więcej, możesz za sprawą akcji zmieniać potem nadal naturę iluzji bez rzucania od nowa zaklęcia."],
                10: ["Złudna Natura Siebie: Pasywna reakcja z automatu pudłująca dany w ciebie wrogi atak wymijając cios własnym iluzorycznym bliźniakiem 1/odpoczynek."],
                14: ["Illusion Reality: Możesz w każdej Iluzji nałożonej przez poziom 1 lub więcej wyciągnąć 1 Obiekt iluzoryczny i magicznie nadać mu na 1 minute twardość Rzeczywistą świata."]
            }
        },
        "divination": {
            "name": "Szkoła Wróżbiarstwa", "name_en": "School of Divination",
            "description": "Przewidujesz przyszłość i naginasz kości losu w rzutach.",
            "description_en": "You see the future and bend the dice of fate.",
            "features": {
                2: ["Wieszczenie (Portent): Rolujesz po odpoczynku 2 kostki d20. Podmieniasz rzut kostką swój, lub ataku, przed tym jak kość rzuci stół - wynikiem z twoich wyroczni."],
                6: ["Zwrot Magiczny dla Wieszczenia: Za użycie zaklęć wieszczenia na poziomie 2+ odzyskujesz slot na poziomie niższym z powrotem."],
                10: ["Trzecie Oko: Uzyskujesz pasywny stały wzrok Eteryczny, Widzenie Niewidzialnych, Przenikanie wzrokiem ciemności itp."],
                14: ["Wielkie Przepowiednie: Posiadasz teraz 3 kości wyroczni do rezerwacji z rana na całą reszte dnia (d20)!"]
            }
        },
        "conjuration": {
            "name": "Szkoła Przywoływania", "name_en": "School of Conjuration",
            "description": "Koncentruje się na tworzeniu istot z energii oraz ich przyzywaniu i teleportacji.",
            "description_en": "Focuses on summoning creatures and teleportation.",
            "features": {
                2: ["Pomniejsze Przywołanie: Materializujesz nienależny krótkożyjący obiekt we własnej ręce jako akcję."],
                6: ["Krok Magiczny: Możesz się raz na teleportnąć do 9 metrów wolnego pola przed sobą, jakby Krok Mgły lub po zmianie miejsca z towarzyszem (swap)."],
                10: ["Skupione Zjawisko: Podczas zogniskowania na Magii z klasyfikacji Przywołania byle wrogi Atak nie przerywa Ci już z automatu utrzymywanej Koncentracji."],
                14: ["Mocarne Przywoływanie: Stworzone stwory wezwane od ciebie posiadają o 30 więcej Temp HP dając im mocne przetrwanie."]
            }
        },
        "enchantment": {
            "name": "Szkoła Oczarowania", "name_en": "School of Enchantment",
            "description": "Nagina emocje wrogów poprzez urzekający styl bycia i potęgę uśpienia.",
            "description_en": "Bends emotions and controls minds.",
            "features": {
                2: ["Urok Hipnozy: Akcja w Promieniu 1.5 metra stawia wrogi byt w kompletny trans gapiąc się na urok czarodzieja i dając się wpasować w Stun-Stun bez atakowania przez niego."],
                6: ["Refleks Instynktowny (Instinctive Charm): Jako reakcja rozpraszasz ataki kogoś skierowane prosto w ciebie, tak iż nagle atakują stwora co stał tuż obok, a nie ciebie."],
                10: ["Podwójne Zaklęcia Umysłu: Rzucając magiczne uderzenie kontrolne tylko dla 1 osoby, możesz od tego punktu wbić darmowo bez używania Twinned Spella (kolejnego kandydata w zasieg czaru)."],
                14: ["Oczarowana Amnezja: W trakcie czarowania wpływu mentalnego zmuszasz kolesia by totalnie nie zorientował się w ogóle żeś go przed chwilą czarował albo rozmawiał!"]
            }
        },
        "necromancy": {
            "name": "Szkoła Nekromancji", "name_en": "School of Necromancy",
            "description": "Ożywiasz martwych na usługi oraz kradniesz energię witalną żywym i wysyłasz w nich strach i zarazę.",
            "description_en": "Raises the dead and drains life energy.",
            "features": {
                2: ["Ponure Żniwo (Grim Harvest): Gdy zabijesz kogoś z użyciem czaru wyższego niż Level 1, Twój organizm odzyskuje hp proporcjonalnie x2-x3 na poziom czaru rzuconego w zmarłego!"],
                6: ["Słudzy Śmierci: Ożywiasz Trudniej zabijalne nieumarłe zombie i dostajesz od teraz 1 gratisowego zombie więcej po podniesieniu ich. Zadają więcej DMG i stają się grubsi o twój Wizzard lvl."],
                10: ["Złagodzenie Martwoty: Odporność na rany typu necrotic! Od teraz twoje Maksymalne Zdrowie HP nie ulegnie żadnej obniżce od zmarłych wampirów itp!"],
                14: ["Rozkazanie Zmarłym (Command Undead): Zdolność zdominowania umysłu mocnych Nieumarłych potworów, poddania go woli kontrolera... NA ZAWSZE, chybaze mają wysoką INT."]
            }
        },
        "transmutation": {
            "name": "Szkoła Transmutacji", "name_en": "School of Transmutation",
            "description": "Panujesz nad materia i rzeźbisz otoczenie by tworzyć złoto ze srebra, alchemizować mikstury itp.",
            "description_en": "Masters matter and sculpts the environment.",
            "features": {
                2: ["Alchemia Transmutacyjna: Tworzenie Drewna z Żelaza na bardzo krótkie akcje w ciągu czasu itp, przydatne."],
                6: ["Kamień Transmutacji: Dajesz sobie i komuś Kamień dający Prędkość ruchu, Oporność na wode i inne lub proficiency saving z ratunku z Constitution!"],
                10: ["Mistrz Zwierzakokształtności: Daje czar Polymorph totalnie za darmo ze zmniejszeniem zasiegu skali na CR=1 zaledwie w darmowej cenie ale pozwala szpiegować niekończenie w darmowo."],
                14: ["Wielki Twórca Pan Transmuter: Masz MOC. Ożywienie zmarłego za kamień, Przywrócenie pełni zdrowia czary-mary, Zniesienie Chorób czy Totalna destrukcja i odmłodzenie z włączeniem w to magii od starzenia."]
            }
        }
    },
}

# ─── ASI Levels per Class ───
ASI_LEVELS = {
    "barbarian": [4, 8, 12, 16, 19],
    "bard":      [4, 8, 12, 16, 19],
    "cleric":    [4, 8, 12, 16, 19],
    "druid":     [4, 8, 12, 16, 19],
    "fighter":   [4, 6, 8, 12, 14, 16, 19],  # Fighters get extra ASIs
    "monk":      [4, 8, 12, 16, 19],
    "paladin":   [4, 8, 12, 16, 19],
    "ranger":    [4, 8, 12, 16, 19],
    "rogue":     [4, 8, 10, 12, 16, 19],  # Rogues get extra ASI at 10
    "sorcerer":  [4, 8, 12, 16, 19],
    "warlock":   [4, 8, 12, 16, 19],
    "wizard":    [4, 8, 12, 16, 19],
}

# ─── Class Features by Level (key features only) ───
CLASS_FEATURES = {
    "barbarian": {
        1: ["Szał (2/długi odp.)", "Obrona bez pancerza"],
        2: ["Brawurowy Atak", "Zmysł Zagrożenia"],
        3: ["Ścieżka Prymitywna (subklasa)"],
        5: ["Dodatkowy Atak", "Szybki Ruch (+3m)"],
        7: ["Instynkt Drapieżnika"],
        9: ["Brutalne Trafienie Krytyczne (+1k)"],
        11: ["Nieustępliwy Szał"],
        15: ["Nieustanny Szał"],
        18: ["Niepokonana Siła"],
        20: ["Pradawny Czempion (STR/CON +4, max 24)"],
    },
    "bard": {
        1: ["Rzucanie zaklęć (Cha)", "Bardowska Inspiracja (k6)"],
        2: ["Pieśń Odpoczynku (k6)", "Magiczny Talent"],
        3: ["Kolegium Barda (subklasa)", "Wiedza Eksperta"],
        5: ["Bardowska Inspiracja (k8)", "Źródło Inspiracji"],
        6: ["Kontr-urok"],
        10: ["Bardowska Inspiracja (k10)", "Magiczne Sekrety"],
        14: ["Magiczne Sekrety"],
        15: ["Bardowska Inspiracja (k12)"],
        18: ["Magiczne Sekrety"],
        20: ["Wyższa Inspiracja"],
    },
    "cleric": {
        1: ["Rzucanie zaklęć (Mdr)", "Boska Domena (subklasa)"],
        2: ["Boska Interwencja (1/odp.)", "Zdolność Domeny"],
        5: ["Zniszczenie Nieumarłych (ST 1/2)"],
        6: ["Zdolność Domeny"],
        8: ["Zniszczenie Nieumarłych (ST 1)", "Zdolność Domeny"],
        10: ["Boska Interwencja"],
        11: ["Zniszczenie Nieumarłych (ST 2)"],
        14: ["Zniszczenie Nieumarłych (ST 3)"],
        17: ["Zniszczenie Nieumarłych (ST 4)", "Zdolność Domeny"],
        20: ["Boska Interwencja (automatyczna)"],
    },
    "druid": {
        1: ["Rzucanie zaklęć (Mdr)", "Druidzki język"],
        2: ["Dzika Postać (ST 1/4)", "Krąg Druida (subklasa)"],
        4: ["Dzika Postać (ST 1/2)"],
        8: ["Dzika Postać (ST 1)"],
        18: ["Wiekuiste Ciało", "Zaklęcia Bestii"],
        20: ["Arcydruid"],
    },
    "fighter": {
        1: ["Styl Walki", "Drugi Oddech (1k10 + lvl)"],
        2: ["Zryw Akcji (1/odp.)"],
        3: ["Archetyp Bojowy (subklasa)"],
        5: ["Dodatkowy Atak"],
        9: ["Nieugiętość (1/odp.)"],
        11: ["Dodatkowy Atak (2)"],
        13: ["Nieugiętość (2/odp.)"],
        17: ["Zryw Akcji (2/odp.)", "Nieugiętość (3/odp.)"],
        20: ["Dodatkowy Atak (3)"],
    },
    "monk": {
        1: ["Obrona bez pancerza", "Sztuki walki"],
        2: ["Ki", "Niewstrzy­many Ruch (+3m)"],
        3: ["Tradycja Monastyczna (subklasa)", "Odbijanie Pocisków"],
        4: ["Powolny Upadek"],
        5: ["Dodatkowy Atak", "Oszała­jące Uderzenie"],
        6: ["Uderzenia Ki = magiczne"],
        7: ["Unik", "Spokój Umysłu"],
        10: ["Czystość Ciała"],
        13: ["Język Słońca i Księżyca"],
        14: ["Diamentowa Dusza"],
        15: ["Wieczna Młodość"],
        18: ["Puste Ciało"],
        20: ["Doskonałość"],
    },
    "paladin": {
        1: ["Boskie Poczucie", "Nałożenie Rąk"],
        2: ["Rzucanie zaklęć (Cha)", "Styl Walki", "Boskie Rażenie"],
        3: ["Święta Przysięga (subklasa)", "Boskie Zdrowie"],
        5: ["Dodatkowy Atak"],
        6: ["Aura Ochrony (+Cha do rzutów obr. sojuszników w 3m)"],
        10: ["Aura Odwagi"],
        11: ["Ulepszone Boskie Rażenie"],
        14: ["Oczyszczający Dotyk"],
        18: ["Aura powiększona do 9m"],
        20: ["Zdolność Przysięgi"],
    },
    "ranger": {
        1: ["Ulubiony Wróg", "Naturalne Badanie"],
        2: ["Rzucanie zaklęć (Mdr)", "Styl Walki"],
        3: ["Archetyp Łowcy (subklasa)", "Pradawna Świadomość"],
        5: ["Dodatkowy Atak"],
        8: ["Wędrowiec po Ziemi"],
        10: ["Ukrycie w Naturze"],
        14: ["Zanik"],
        18: ["Zmysł Drapieżnika"],
        20: ["Wróg Zabójca"],
    },
    "rogue": {
        1: ["Wiedza Eksperta (2)", "Atak Skrytobójczy (1k6)", "Złodziejski Żargon"],
        2: ["Cwana Akcja"],
        3: ["Archetyp Łotrzyka (subklasa)", "Atak Skrytobójczy (2k6)"],
        5: ["Niezwykły Unik", "Atak Skrytobójczy (3k6)"],
        6: ["Wiedza Eksperta (2 dodatkowe)"],
        7: ["Unik", "Atak Skrytobójczy (4k6)"],
        9: ["Atak Skrytobójczy (5k6)"],
        11: ["Niezawodny Talent", "Atak Skrytobójczy (6k6)"],
        13: ["Atak Skrytobójczy (7k6)"],
        14: ["Ślepy Zmysł"],
        15: ["Śliski Umysł", "Atak Skrytobójczy (8k6)"],
        17: ["Atak Skrytobójczy (9k6)"],
        18: ["Nieuchwytność"],
        19: ["Atak Skrytobójczy (10k6)"],
        20: ["Uderzenie Szczęściarza"],
    },
    "sorcerer": {
        1: ["Rzucanie zaklęć (Cha)", "Magiczne Źródło (subklasa)"],
        2: ["Źródło Czarów (pkt = lvl)"],
        3: ["Metamagia (2 opcje)"],
        6: ["Zdolność Źródła"],
        10: ["Metamagia (+1 opcja)"],
        14: ["Zdolność Źródła"],
        17: ["Metamagia (+1 opcja)"],
        18: ["Zdolność Źródła"],
        20: ["Regeneracja Czarów"],
    },
    "warlock": {
        1: ["Pakt Okultystyczny (subklasa)", "Magia Paktu"],
        2: ["Mroczne Inwokacje (2)"],
        3: ["Dar Paktu"],
        5: ["Mroczne Inwokacje (3)"],
        7: ["Mroczne Inwokacje (4)"],
        9: ["Mroczne Inwokacje (5)"],
        11: ["Mistyczny Arcanum (6 lvl)"],
        12: ["Mroczne Inwokacje (6)"],
        13: ["Mistyczny Arcanum (7 lvl)"],
        15: ["Mistyczny Arcanum (8 lvl)", "Mroczne Inwokacje (7)"],
        17: ["Mistyczny Arcanum (9 lvl)"],
        18: ["Mroczne Inwokacje (8)"],
        20: ["Mistrz Eldryczny"],
    },
    "wizard": {
        1: ["Rzucanie zaklęć (Int)", "Odzysk Arcanum"],
        2: ["Tradycja Arcanum (subklasa)"],
        6: ["Zdolność Tradycji"],
        10: ["Zdolność Tradycji"],
        14: ["Zdolność Tradycji"],
        18: ["Mistrzostwo Zaklęć"],
        20: ["Podpisowe Zaklęcia"],
    },
}

# ─── Sneak Attack Dice by Rogue Level ───
SNEAK_ATTACK_DICE = {
    1:1, 2:1, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4, 9:5, 10:5,
    11:6, 12:6, 13:7, 14:7, 15:8, 16:8, 17:9, 18:9, 19:10, 20:10,
}

# ─── Barbarian Rage Count & Damage ───
RAGE_COUNT = {1:2,2:2,3:3,4:3,5:3,6:4,7:4,8:4,9:4,10:4,11:4,12:5,13:5,14:5,15:5,16:5,17:6,18:6,19:6,20:99}
RAGE_DAMAGE = {1:2,2:2,3:2,4:2,5:2,6:2,7:2,8:2,9:3,10:3,11:3,12:3,13:3,14:3,15:3,16:4,17:4,18:4,19:4,20:4}

# ─── Monk Ki Points & Martial Arts Die ───
MONK_MARTIAL_ARTS = {1:"1d4",2:"1d4",3:"1d4",4:"1d4",5:"1d6",6:"1d6",7:"1d6",8:"1d6",9:"1d6",10:"1d6",11:"1d8",12:"1d8",13:"1d8",14:"1d8",15:"1d8",16:"1d8",17:"1d10",18:"1d10",19:"1d10",20:"1d10"}
# Ki points = monk level

# ─── Spell slot type per class ───
CASTER_TYPE = {
    "bard": "full", "cleric": "full", "druid": "full",
    "sorcerer": "full", "wizard": "full",
    "paladin": "half", "ranger": "half",
    "warlock": "pact",
    "fighter": "none",  # Eldritch Knight = 1/3 (handled by subclass)
    "rogue": "none",    # Arcane Trickster = 1/3 (handled by subclass)
    "barbarian": "none", "monk": "none",
}

# 1/3 caster slots (Eldritch Knight, Arcane Trickster)
THIRD_CASTER_SLOTS = {
    1:[0,0,0,0],2:[0,0,0,0],3:[2,0,0,0],4:[3,0,0,0],5:[3,0,0,0],6:[3,0,0,0],
    7:[4,2,0,0],8:[4,2,0,0],9:[4,2,0,0],10:[4,3,0,0],11:[4,3,0,0],12:[4,3,0,0],
    13:[4,3,2,0],14:[4,3,2,0],15:[4,3,2,0],16:[4,3,3,0],17:[4,3,3,0],18:[4,3,3,0],
    19:[4,3,3,1],20:[4,3,3,1],
}
