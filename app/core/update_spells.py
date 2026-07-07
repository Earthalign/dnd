import re

with open('d:/python_projects/dnd/app/core/rules.py', 'r', encoding='utf-8') as f:
    code = f.read()

spells_to_update = ['cure_wounds', 'detect_magic', 'identify', 'alarm', 'disguise_self', 'feather_fall', 'jump', 'longstrider', 'purify_food_and_drink', 'sanctuary']
cantrips_to_update = ['mending', 'prestidigitation', 'light', 'mage_hand', 'ray_of_frost', 'shocking_grasp', 'fire_bolt', 'poison_spray', 'guidance', 'resistance', 'acid_splash']

for spell in spells_to_update + cantrips_to_update:
    # We find the id, then the classes array.
    pattern = r'("id":\s*"' + spell + r'"[\s\S]*?"classes":\s*\[)([\s\S]*?)(\])'
    def repl(m):
        classes = m.group(2)
        if '"artificer"' not in classes:
            if classes.strip():
                classes += ',\n                "artificer"'
            else:
                classes += '\n                "artificer"'
        return m.group(1) + classes + m.group(3)
    code = re.sub(pattern, repl, code)

with open('d:/python_projects/dnd/app/core/rules.py', 'w', encoding='utf-8') as f:
    f.write(code)
print('Updated spells')
