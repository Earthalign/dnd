"""
Character creation utilities - stat calculations and auto-assignment logic.
Based on D&D 5e rules (PHB).
"""
import math
import json
from typing import Dict, List, Tuple
from app.core.rules import (
    CLASSES, RACES, BACKGROUNDS, SKILLS, SPELLS, STAT_NAMES,
    POINT_BUY_COSTS, POINT_BUY_TOTAL, POINT_BUY_MIN, POINT_BUY_MAX,
    STANDARD_ARRAY, CLASS_STAT_PRIORITY, PROFICIENCY_BY_LEVEL
)
from app.core.progression import CASTER_TYPE, FULL_CASTER_SLOTS, HALF_CASTER_SLOTS, THIRD_CASTER_SLOTS, WARLOCK_SLOTS, SUBCLASSES, CLASS_FEATURES
from app.core.equipment import CLASS_EQUIPMENT, WEAPONS, ARMORS
from app.schemas.character import CharacterCreateSchema


def get_modifier(score: int) -> int:
    """Calculate ability modifier from score."""
    return math.floor((score - 10) / 2)


def get_proficiency_bonus(level: int) -> int:
    """Get proficiency bonus for given level."""
    return PROFICIENCY_BY_LEVEL.get(level, 2)


def calculate_hp(char_class: str, level: int, con_score: int) -> int:
    """Calculate max HP based on class, level, and constitution."""
    hit_die = CLASSES[char_class]["hit_die"]
    con_mod = get_modifier(con_score)
    avg_per_level = (hit_die // 2) + 1
    return hit_die + con_mod + (avg_per_level + con_mod) * (level - 1)


def calculate_ac(armor_type: str, dex_score: int, con_score: int = 10, wis_score: int = 10) -> int:
    """Calculate armor class."""
    dex_mod = get_modifier(dex_score)
    con_mod = get_modifier(con_score)
    wis_mod = get_modifier(wis_score)

    armor_table = {
        "none": 10 + dex_mod,
        "barbarian_unarmored": 10 + dex_mod + con_mod,
        "monk_unarmored": 10 + dex_mod + wis_mod,
        "leather": 11 + dex_mod,
        "studded_leather": 12 + dex_mod,
        "hide": 12 + min(dex_mod, 2),
        "chain_mail": 16,
        "scale_mail": 14 + min(dex_mod, 2),
        "breastplate": 14 + min(dex_mod, 2),
        "half_plate": 15 + min(dex_mod, 2),
        "ring_mail": 14,
        "chain_mail_heavy": 16,
        "splint": 17,
        "plate": 18,
    }
    return armor_table.get(armor_type, 10 + dex_mod)


def apply_racial_asi(base_stats: Dict[str, int], race_key: str) -> Dict[str, int]:
    """Apply racial ability score improvements."""
    race = RACES.get(race_key, {})
    asi = race.get("asi", {})
    result = dict(base_stats)
    for stat, bonus in asi.items():
        result[stat] = result.get(stat, 8) + bonus
    return result


def auto_assign_stats_try_harder(char_class: str, race_key: str) -> Dict[str, int]:
    """
    'Try Harder' mode: Assign highest stats to most important attributes for the class.
    Uses array [15, 15, 15, 8, 8, 8].
    """
    priority = CLASS_STAT_PRIORITY.get(char_class, ["str", "dex", "con", "int", "wis", "cha"])
    stat_keys = ["str", "dex", "con", "int", "wis", "cha"]
    values = [15, 15, 15, 8, 8, 8]

    # Sort stats by priority
    ordered = sorted(stat_keys, key=lambda s: priority.index(s) if s in priority else 99)
    base = {stat: val for stat, val in zip(ordered, values)}

    return base


def auto_assign_stats_balanced(char_class: str, race_key: str) -> Dict[str, int]:
    """
    'Balanced' mode: Primary stats get high scores, but secondary stats are not neglected.
    Ensures no stat below 10 (before racial bonuses). Sums to exactly 27 points.
    """
    priority = CLASS_STAT_PRIORITY.get(char_class, ["str", "dex", "con", "int", "wis", "cha"])
    stat_keys = ["str", "dex", "con", "int", "wis", "cha"]

    # Balanced distribution spending exactly 27 points: [14, 14, 13, 12, 10, 10]
    balanced_array = [14, 14, 13, 12, 10, 10]
    ordered = sorted(stat_keys, key=lambda s: priority.index(s) if s in priority else 99)
    base = {stat: val for stat, val in zip(ordered, balanced_array)}

    return base


def point_buy_remaining(stats: Dict[str, int]) -> int:
    """Calculate remaining point buy budget."""
    spent = sum(POINT_BUY_COSTS.get(v, 0) for v in stats.values())
    return POINT_BUY_TOTAL - spent


def validate_point_buy(stats: Dict[str, int]) -> Tuple[bool, str]:
    """Validate point buy stats."""
    for stat, val in stats.items():
        if val < POINT_BUY_MIN:
            return False, f"{STAT_NAMES.get(stat, stat)}: minimalna wartość to {POINT_BUY_MIN}"
        if val > POINT_BUY_MAX:
            return False, f"{STAT_NAMES.get(stat, stat)}: maksymalna wartość to {POINT_BUY_MAX}"
        if val not in POINT_BUY_COSTS:
            return False, f"Nieprawidłowa wartość: {val}"
    remaining = point_buy_remaining(stats)
    if remaining != 0:
        return False, f"Musisz rozdzielić dokładnie wszystkie 27 punktów (pozostało: {remaining} pkt)"
    return True, "OK"


def get_skill_bonus(skill_key: str, stats: Dict[str, int], proficiencies: List[str], expertise: List[str], level: int) -> int:
    """Calculate total skill bonus."""
    skill = SKILLS.get(skill_key, {})
    stat = skill.get("stat", "str")
    mod = get_modifier(stats.get(stat, 10))
    prof = get_proficiency_bonus(level)

    if skill_key in expertise:
        return mod + prof * 2
    elif skill_key in proficiencies:
        return mod + prof
    return mod


def get_saving_throw_bonus(stat: str, stats: Dict[str, int], proficiencies: List[str], level: int) -> int:
    """Calculate saving throw bonus."""
    mod = get_modifier(stats.get(stat, 10))
    if stat in proficiencies:
        return mod + get_proficiency_bonus(level)
    return mod


def build_character_sheet(data: CharacterCreateSchema) -> Dict:
    """
    Build complete character sheet from form schema data.
    Returns structured dict with all calculated values.
    """
    char_class = data.char_class
    race = data.race
    background = data.background
    level = data.level
    name = data.name
    player = data.player
    alignment = data.alignment
    subclass_key = data.subclass

    # Base stats (from Point Buy/Standard Array, 8-15)
    base_stats = {
        "str": data.strength,
        "dex": data.dexterity,
        "con": data.constitution,
        "int": data.intelligence,
        "wis": data.wisdom,
        "cha": data.charisma,
    }

    # Final stats are base stats + racial ASI
    raw_stats = apply_racial_asi(base_stats, race)

    # Apply ASI bonuses from level-up choices
    asi_slots = []
    try:
        if data.asi_slots_json:
            asi_slots = json.loads(data.asi_slots_json)
    except Exception:
        pass

    asi_feats = []
    for slot in asi_slots:
        slot_type = slot.get("type", "feat")
        if slot_type == "feat" and slot.get("feat"):
            asi_feats.append(slot["feat"])
        elif slot_type == "+2" and slot.get("stat1"):
            raw_stats[slot["stat1"]] = raw_stats.get(slot["stat1"], 10) + 2
        elif slot_type == "+1+1":
            if slot.get("stat1"):
                raw_stats[slot["stat1"]] = raw_stats.get(slot["stat1"], 10) + 1
            if slot.get("stat2"):
                raw_stats[slot["stat2"]] = raw_stats.get(slot["stat2"], 10) + 1

    # Human variant free feat
    if data.human_variant_feat:
        asi_feats.append(data.human_variant_feat)

    class_data = CLASSES.get(char_class, {})
    race_data = RACES.get(race, {})
    bg_data = BACKGROUNDS.get(background, {})

    prof_bonus = get_proficiency_bonus(level)

    # Proficiencies
    saving_throw_profs = class_data.get("saving_throws", [])
    skill_profs = data.skills
    expertise = data.expertise
    feats = data.feats

    # Modifiers
    mods = {stat: get_modifier(val) for stat, val in raw_stats.items()}

    # HP
    hp = calculate_hp(char_class, level, raw_stats["con"])

    # Initiative
    initiative = mods["dex"]

    # Passive Perception
    perception_prof = 1 if "postrzeganie" in skill_profs else 0
    passive_perception = 10 + mods["wis"] + (prof_bonus if perception_prof else 0)

    # AC — consider selected equipment package armor
    if char_class == "barbarian":
        ac = 10 + mods["dex"] + mods["con"]
    elif char_class == "monk":
        ac = 10 + mods["dex"] + mods["wis"]
    else:
        ac = 10 + mods["dex"]  # default unarmored
        # Look up the selected equipment package for armor
        eq_pkg_id = data.equipment_package
        if eq_pkg_id:
            pkg_options = CLASS_EQUIPMENT.get(char_class, {}).get("options", [])
            for pkg in pkg_options:
                if pkg["id"] == eq_pkg_id:
                    armor_key = pkg.get("armor", "none")
                    has_shield = pkg.get("shield", False)
                    armor_ac_map = {
                        "none": 10 + mods["dex"],
                        "padded": 11 + mods["dex"],
                        "leather": 11 + mods["dex"],
                        "studded_leather": 12 + mods["dex"],
                        "hide": 12 + min(mods["dex"], 2),
                        "chain_shirt": 13 + min(mods["dex"], 2),
                        "scale_mail": 14 + min(mods["dex"], 2),
                        "breastplate": 14 + min(mods["dex"], 2),
                        "half_plate": 15 + min(mods["dex"], 2),
                        "ring_mail": 14,
                        "chain_mail": 16,
                        "splint": 17,
                        "plate": 18,
                    }
                    if armor_key in armor_ac_map:
                        ac = armor_ac_map[armor_key]
                    if has_shield:
                        ac += 2
                    break

    # Saving throws
    saves = {}
    for stat in ["str", "dex", "con", "int", "wis", "cha"]:
        saves[stat] = get_saving_throw_bonus(stat, raw_stats, saving_throw_profs, level)

    # Skill bonuses
    skill_bonuses = {}
    for skill_key in SKILLS:
        skill_bonuses[skill_key] = get_skill_bonus(skill_key, raw_stats, skill_profs, expertise, level)

    # Gather class features up to current level
    class_features = []
    features_dict = CLASS_FEATURES.get(char_class, {})
    for lvl in range(1, level + 1):
        if lvl in features_dict:
            class_features.extend(features_dict[lvl])
            
    # Add subclass features/name
    subclass_name = ""
    if subclass_key:
        sc_data = SUBCLASSES.get(char_class, {}).get(subclass_key, {})
        subclass_name = sc_data.get("name", subclass_key)
        
    class_display_name = class_data.get("name", char_class)
    if subclass_name:
        class_display_name += f" ({subclass_name})"

    # Calculate spell slots
    spell_slots = {}
    caster_type = CASTER_TYPE.get(char_class, "none")
    if subclass_key in ["eldritch_knight", "arcane_trickster"]:
        caster_type = "third"
        
    if caster_type == "full":
        slots_list = FULL_CASTER_SLOTS.get(level, [0]*9)
        spell_slots = {i+1: slots_list[i] for i in range(9)}
    elif caster_type == "half":
        slots_list = HALF_CASTER_SLOTS.get(level, [0]*5)
        spell_slots = {i+1: slots_list[i] for i in range(5)}
    elif caster_type == "third":
        slots_list = THIRD_CASTER_SLOTS.get(level, [0]*4)
        spell_slots = {i+1: slots_list[i] for i in range(4)}
    elif caster_type == "pact":
        warlock_data = WARLOCK_SLOTS.get(level, {"slots": 0, "slot_level": 0})
        slots_count = warlock_data["slots"]
        slot_level = warlock_data["slot_level"]
        if slot_level > 0:
            spell_slots = {slot_level: slots_count}

    # Build equipment info string — class package + background items
    equipment_info = ""
    eq_pkg = data.equipment_package
    if eq_pkg:
        pkg_options = CLASS_EQUIPMENT.get(char_class, {}).get("options", [])
        for pkg in pkg_options:
            if pkg["id"] == eq_pkg:
                weapon_names = [WEAPONS[w]["name"] if w in WEAPONS else w for w in pkg.get("weapons", [])]
                armor_name = ARMORS[pkg["armor"]]["name"] if pkg.get("armor") and pkg["armor"] in ARMORS else ""
                shield_str = " + Tarcza" if pkg.get("shield") else ""
                equipment_info = f"{', '.join(weapon_names)} | {armor_name}{shield_str}"
                break
    # Add background equipment
    bg_equipment = bg_data.get("equipment", [])
    if bg_equipment:
        bg_eq_str = ", ".join(bg_equipment)
        equipment_info = (equipment_info + " | " + bg_eq_str).strip(" | ") if equipment_info else bg_eq_str
    if data.equipment:
        equipment_info = (equipment_info + " | " + data.equipment).strip(" | ") if equipment_info else data.equipment

    return {
        "name": name,
        "player": player,
        "char_class": char_class,
        "class_name": class_display_name,
        "race": race,
        "race_name": race_data.get("name", race),
        "background": background,
        "background_name": bg_data.get("name", background),
        "level": level,
        "alignment": alignment,
        "stats": raw_stats,
        "modifiers": mods,
        "prof_bonus": prof_bonus,
        "hp": hp,
        "ac": ac,
        "initiative": initiative,
        "speed": race_data.get("speed", 9),
        "passive_perception": passive_perception,
        "saving_throws": saves,
        "saving_throw_profs": saving_throw_profs,
        "skill_bonuses": skill_bonuses,
        "skill_profs": skill_profs,
        "expertise": expertise,
        "feats": feats,
        "traits": race_data.get("traits", []),
        "class_features": class_features,
        "languages": race_data.get("languages", ["Wspólny"]),
        "armor_profs": class_data.get("armor_proficiencies", []),
        "weapon_profs": class_data.get("weapon_proficiencies", []),
        "hit_die": class_data.get("hit_die", 8),
        "spellcasting": class_data.get("spellcasting", False) or caster_type != "none",
        "spellcasting_stat": class_data.get("spellcasting_stat") or ("int" if caster_type == "third" else None),
        "spell_slots": spell_slots,
        "personality": data.personality,
        "ideals": data.ideals,
        "bonds": data.bonds,
        "flaws": data.flaws,
        "backstory": data.backstory,
        "appearance": data.appearance,
        "age": data.age,
        "height": data.height,
        "weight": data.weight,
        "eyes": data.eyes,
        "skin": data.skin,
        "hair": data.hair,
        "equipment": equipment_info,
        "attacks": data.attacks,
        "asi_feats": asi_feats,
    }
