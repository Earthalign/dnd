import ast
import json

feats_data = {
    'alert': {'name': 'Czujny', 'name_en': 'Alert', 'desc': '+5 do inicjatywy, nie można cię zaskoczyć dopóki jesteś przytomny.'},
    'tough': {'name': 'Twardziel', 'name_en': 'Tough', 'desc': 'Twoje maksimum Punktów Wytrzymałości rośnie o 2 za każdy twój poziom.'},
    'lucky': {'name': 'Szczęściarz', 'name_en': 'Lucky', 'desc': 'Masz 3 punkty szczęścia. Możesz ich użyć, by przerzucić k20 lub zmusić wroga do przerzutu.'},
    'mobile': {'name': 'Mobilny', 'name_en': 'Mobile', 'desc': 'Twoja prędkość rośnie o 3 metry. Ataki z ukrycia (Dash) trudnym terenem cię nie spowalniają.'},
    'sharpshooter': {'name': 'Strzelec Wyborowy', 'name_en': 'Sharpshooter', 'desc': 'Ignorujesz częściową osłonę. Możesz przyjąć -5 do ataku za +10 do obrażeń przy ataku dystansowym.'},
    'great_weapon_master': {'name': 'Mistrz Broni Dwuręcznej', 'name_en': 'Great Weapon Master', 'desc': 'Gdy trafisz krytycznie lub zabijesz, możesz wykonać atak bonusowy. Przyjęcie -5 do ataku daje +10 obrażeń ciężką bronią.'},
    'war_caster': {'name': 'Mag Bitewny', 'name_en': 'War Caster', 'desc': 'Przewaga na rzuty obronne na Koncentrację. Możesz rzucać czary mając broń/tarczę w dłoniach. Zaklęcie na atak okazyjny.'},
    'sentinel': {'name': 'Strażnik', 'name_en': 'Sentinel', 'desc': 'Trafienie okazyjne redukuje prędkość celu do 0. Istoty uciekające od ciebie prowokują atak, nawet przy Odskoku.'},
    'resilient': {'name': 'Odporny', 'name_en': 'Resilient', 'desc': '+1 do wybranej cechy oraz biegłość w Rzutach Obronnych z niej.'},
    'actor': {'name': 'Aktor', 'name_en': 'Actor', 'desc': '+1 do Charyzmy. Przewaga na oszustwo i występy w przebraniu.'},
    'observant': {'name': 'Spostrzegawczy', 'name_en': 'Observant', 'desc': '+1 do Inteligencji lub Mądrości. Czytasz z ruchu warg, +5 do pasywnej percepcji i pasywnego śledztwa.'},
    'polearm_master': {'name': 'Mistrz Broni Drzewcowej', 'name_en': 'Polearm Master', 'desc': 'Atakujesz z akcji bonusowej tępym końcem broni. Wróg prowokuje atak okazyjny gdy wchodzi w twój zasięg.'},
    'spell_sniper': {'name': 'Snajper Zaklęć', 'name_en': 'Spell Sniper', 'desc': 'Zasięg zaklęć ataku x2. Ignorują one pół osłony. 1 dodatkowa sztuczka wymagająca ataku.'},
}

new_spells = {
    'level_2': [
        {'id': 'blindness_deafness', 'name_pl': 'Ślepota/Głuchota', 'name_en': 'Blindness/Deafness', 'classes': ['bard', 'cleric', 'sorcerer', 'wizard']},
        {'id': 'blur', 'name_pl': 'Rozmycie', 'name_en': 'Blur', 'classes': ['sorcerer', 'wizard']},
        {'id': 'darkness', 'name_pl': 'Ciemność', 'name_en': 'Darkness', 'classes': ['sorcerer', 'warlock', 'wizard']},
        {'id': 'hold_person', 'name_pl': 'Unieruchomienie Osoby', 'name_en': 'Hold Person', 'classes': ['bard', 'cleric', 'druid', 'sorcerer', 'warlock', 'wizard']},
        {'id': 'invisibility', 'name_pl': 'Niewidzialność', 'name_en': 'Invisibility', 'classes': ['bard', 'sorcerer', 'warlock', 'wizard']},
        {'id': 'misty_step', 'name_pl': 'Krok Mgły', 'name_en': 'Misty Step', 'classes': ['sorcerer', 'warlock', 'wizard']},
        {'id': 'scorching_ray', 'name_pl': 'Piekący Promień', 'name_en': 'Scorching Ray', 'classes': ['sorcerer', 'wizard']},
        {'id': 'shatter', 'name_pl': 'Roztrzaskanie', 'name_en': 'Shatter', 'classes': ['bard', 'sorcerer', 'warlock', 'wizard']},
        {'id': 'spiritual_weapon', 'name_pl': 'Duchowa Broń', 'name_en': 'Spiritual Weapon', 'classes': ['cleric']}
    ],
    'level_3': [
        {'id': 'counterspell', 'name_pl': 'Kontrzaklęcie', 'name_en': 'Counterspell', 'classes': ['sorcerer', 'warlock', 'wizard']},
        {'id': 'dispel_magic', 'name_pl': 'Rozproszenie Magii', 'name_en': 'Dispel Magic', 'classes': ['bard', 'cleric', 'druid', 'paladin', 'sorcerer', 'warlock', 'wizard']},
        {'id': 'fireball', 'name_pl': 'Kula Ognia', 'name_en': 'Fireball', 'classes': ['sorcerer', 'wizard']},
        {'id': 'fly', 'name_pl': 'Lot', 'name_en': 'Fly', 'classes': ['sorcerer', 'warlock', 'wizard']},
        {'id': 'haste', 'name_pl': 'Przyspieszenie', 'name_en': 'Haste', 'classes': ['sorcerer', 'wizard']},
        {'id': 'lightning_bolt', 'name_pl': 'Piorun', 'name_en': 'Lightning Bolt', 'classes': ['sorcerer', 'wizard']},
        {'id': 'revivify', 'name_pl': 'Ożywienie', 'name_en': 'Revivify', 'classes': ['cleric', 'paladin']}
    ],
    'level_4': [
        {'id': 'banishment', 'name_pl': 'Wygnanie', 'name_en': 'Banishment', 'classes': ['cleric', 'paladin', 'sorcerer', 'warlock', 'wizard']},
        {'id': 'blight', 'name_pl': 'Zaraza', 'name_en': 'Blight', 'classes': ['druid', 'sorcerer', 'warlock', 'wizard']},
        {'id': 'dimension_door', 'name_pl': 'Drzwi przez Wymiary', 'name_en': 'Dimension Door', 'classes': ['bard', 'sorcerer', 'warlock', 'wizard']},
        {'id': 'greater_invisibility', 'name_pl': 'Większa Niewidzialność', 'name_en': 'Greater Invisibility', 'classes': ['bard', 'sorcerer', 'wizard']},
        {'id': 'polymorph', 'name_pl': 'Polimorfia', 'name_en': 'Polymorph', 'classes': ['bard', 'druid', 'sorcerer', 'wizard']}
    ],
    'level_5': [
        {'id': 'cloudkill', 'name_pl': 'Zabójcza Chmura', 'name_en': 'Cloudkill', 'classes': ['sorcerer', 'wizard']},
        {'id': 'cone_of_cold', 'name_pl': 'Stożek Zimna', 'name_en': 'Cone of Cold', 'classes': ['sorcerer', 'wizard']},
        {'id': 'greater_restoration', 'name_pl': 'Większe Uzdrowienie', 'name_en': 'Greater Restoration', 'classes': ['bard', 'cleric', 'druid']},
        {'id': 'hold_monster', 'name_pl': 'Unieruchomienie Potwora', 'name_en': 'Hold Monster', 'classes': ['bard', 'sorcerer', 'warlock', 'wizard']},
        {'id': 'mass_cure_wounds', 'name_pl': 'Masowe Leczenie Ran', 'name_en': 'Mass Cure Wounds', 'classes': ['bard', 'cleric', 'druid']}
    ],
    'level_6': [
        {'id': 'chain_lightning', 'name_pl': 'Łańcuch Piorunów', 'name_en': 'Chain Lightning', 'classes': ['sorcerer', 'wizard']},
        {'id': 'disintegrate', 'name_pl': 'Dezintegracja', 'name_en': 'Disintegrate', 'classes': ['sorcerer', 'wizard']},
        {'id': 'heal', 'name_pl': 'Uzdrawianie', 'name_en': 'Heal', 'classes': ['cleric', 'druid']},
        {'id': 'sunbeam', 'name_pl': 'Promień Słońca', 'name_en': 'Sunbeam', 'classes': ['druid', 'sorcerer', 'wizard']},
        {'id': 'true_seeing', 'name_pl': 'Prawdziwe Widzenie', 'name_en': 'True Seeing', 'classes': ['bard', 'cleric', 'sorcerer', 'warlock', 'wizard']}
    ],
    'level_7': [
        {'id': 'delayed_blast_fireball', 'name_pl': 'Opóźniona Kula Ognia', 'name_en': 'Delayed Blast Fireball', 'classes': ['sorcerer', 'wizard']},
        {'id': 'finger_of_death', 'name_pl': 'Palec Śmierci', 'name_en': 'Finger of Death', 'classes': ['sorcerer', 'warlock', 'wizard']},
        {'id': 'forcecage', 'name_pl': 'Klatka Mocy', 'name_en': 'Forcecage', 'classes': ['bard', 'warlock', 'wizard']},
        {'id': 'plane_shift', 'name_pl': 'Przesunięcie Planów', 'name_en': 'Plane Shift', 'classes': ['cleric', 'druid', 'sorcerer', 'warlock', 'wizard']},
        {'id': 'resurrection', 'name_pl': 'Zmartwychwstanie', 'name_en': 'Resurrection', 'classes': ['bard', 'cleric']}
    ],
    'level_8': [
        {'id': 'antimagic_field', 'name_pl': 'Pole Antymagiczne', 'name_en': 'Antimagic Field', 'classes': ['cleric', 'wizard']},
        {'id': 'dominate_monster', 'name_pl': 'Zdominowanie Potwora', 'name_en': 'Dominate Monster', 'classes': ['bard', 'sorcerer', 'warlock', 'wizard']},
        {'id': 'feeblemind', 'name_pl': 'Słaboumysłowość', 'name_en': 'Feeblemind', 'classes': ['bard', 'druid', 'warlock', 'wizard']},
        {'id': 'incendiary_cloud', 'name_pl': 'Zapalająca Chmura', 'name_en': 'Incendiary Cloud', 'classes': ['sorcerer', 'wizard']},
        {'id': 'sunburst', 'name_pl': 'Eksplozja Słońca', 'name_en': 'Sunburst', 'classes': ['druid', 'sorcerer', 'wizard']}
    ],
    'level_9': [
        {'id': 'meteor_swarm', 'name_pl': 'Rój Meteorów', 'name_en': 'Meteor Swarm', 'classes': ['sorcerer', 'wizard']},
        {'id': 'power_word_kill', 'name_pl': 'Słowo Mocy: Giń', 'name_en': 'Power Word Kill', 'classes': ['bard', 'sorcerer', 'warlock', 'wizard']},
        {'id': 'time_stop', 'name_pl': 'Zatrzymanie Czasu', 'name_en': 'Time Stop', 'classes': ['sorcerer', 'wizard']},
        {'id': 'true_resurrection', 'name_pl': 'Prawdziwe Zmartwychwstanie', 'name_en': 'True Resurrection', 'classes': ['cleric', 'druid']},
        {'id': 'wish', 'name_pl': 'Życzenie', 'name_en': 'Wish', 'classes': ['sorcerer', 'wizard']}
    ]
}

with open('app/core/rules.py', 'r', encoding='utf-8') as f:
    content = f.read()

str_to_add = ''
for lvl, spells in new_spells.items():
    str_to_add += f'    "{lvl}": {json.dumps(spells, ensure_ascii=False)},\n'

parts = content.split('STAT_NAMES = {')
spells_part = parts[0]

if spells_part.strip().endswith('}'):
    idx = spells_part.rfind('}')
    spells_part = spells_part[:idx] + ',\n' + str_to_add + '}\n\n'

with open('app/core/rules.py', 'w', encoding='utf-8') as f:
    f.write(spells_part + 'STAT_NAMES = {' + parts[1])

with open('app/core/rules.py', 'r', encoding='utf-8') as f:
    content = f.read()

if 'FEATS =' not in content:
    with open('app/core/rules.py', 'a', encoding='utf-8') as f:
        f.write('\n\nFEATS = ' + json.dumps(feats_data, indent=4, ensure_ascii=False) + '\n')

print("Update complete")
