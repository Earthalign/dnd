"""
Character creation utilities - stat calculations and auto-assignment logic.
Based on D&D 5e rules (PHB).
"""
import math
from dnd_data import (
    CLASSES, RACES, BACKGROUNDS, SKILLS, STAT_NAMES,
    STANDARD_ARRAY, POINT_BUY_COSTS, POINT_BUY_TOTAL, POINT_BUY_MIN, POINT_BUY_MAX,
    PROFICIENCY_BY_LEVEL, CLASS_STAT_PRIORITY
)


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


def apply_racial_asi(base_stats: dict, race_key: str) -> dict:
    """Apply racial ability score improvements."""
    race = RACES.get(race_key, {})
    asi = race.get("asi", {})
    result = dict(base_stats)
    for stat, bonus in asi.items():
        result[stat] = result.get(stat, 8) + bonus
    return result


def auto_assign_stats_try_harder(char_class: str, race_key: str) -> dict:
    """
    'Try Harder' mode: Assign highest stats to most important attributes for the class.
    Uses standard array [15, 14, 13, 12, 10, 8].
    """
    priority = CLASS_STAT_PRIORITY.get(char_class, ["str", "dex", "con", "int", "wis", "cha"])
    stat_keys = ["str", "dex", "con", "int", "wis", "cha"]
    values = sorted(STANDARD_ARRAY, reverse=True)

    # Sort stats by priority
    ordered = sorted(stat_keys, key=lambda s: priority.index(s) if s in priority else 99)
    base = {stat: val for stat, val in zip(ordered, values)}

    return base


def auto_assign_stats_balanced(char_class: str, race_key: str) -> dict:
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


def point_buy_remaining(stats: dict) -> int:
    """Calculate remaining point buy budget."""
    spent = sum(POINT_BUY_COSTS.get(v, 0) for v in stats.values())
    return POINT_BUY_TOTAL - spent


def validate_point_buy(stats: dict) -> tuple[bool, str]:
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


def get_skill_bonus(skill_key: str, stats: dict, proficiencies: list, expertise: list, level: int) -> int:
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


def get_saving_throw_bonus(stat: str, stats: dict, proficiencies: list, level: int) -> int:
    """Calculate saving throw bonus."""
    mod = get_modifier(stats.get(stat, 10))
    if stat in proficiencies:
        return mod + get_proficiency_bonus(level)
    return mod


def build_character_sheet(form_data: dict) -> dict:
    """
    Build complete character sheet from form data.
    Returns structured dict with all calculated values.
    """
    char_class = form_data.get("char_class", "fighter")
    race = form_data.get("race", "human")
    background = form_data.get("background", "folk_hero")
    level = int(form_data.get("level", 1))
    name = form_data.get("name", "Bohater")
    player = form_data.get("player", "")
    alignment = form_data.get("alignment", "Neutralny")

    # Base stats (from Point Buy/Standard Array, 8-15)
    base_stats = {
        "str": int(form_data.get("str", 10)),
        "dex": int(form_data.get("dex", 10)),
        "con": int(form_data.get("con", 10)),
        "int": int(form_data.get("int", 10)),
        "wis": int(form_data.get("wis", 10)),
        "cha": int(form_data.get("cha", 10)),
    }

    # Final stats are base stats + racial ASI
    raw_stats = apply_racial_asi(base_stats, race)

    class_data = CLASSES.get(char_class, {})
    race_data = RACES.get(race, {})
    bg_data = BACKGROUNDS.get(background, {})

    prof_bonus = get_proficiency_bonus(level)

    # Proficiencies
    saving_throw_profs = class_data.get("saving_throws", [])
    skill_profs = form_data.getlist("skills") if hasattr(form_data, 'getlist') else form_data.get("skills", [])
    expertise = form_data.getlist("expertise") if hasattr(form_data, 'getlist') else form_data.get("expertise", [])

    # Modifiers
    mods = {stat: get_modifier(val) for stat, val in raw_stats.items()}

    # HP
    hp = calculate_hp(char_class, level, raw_stats["con"])

    # Initiative
    initiative = mods["dex"]

    # Passive Perception
    perception_prof = 1 if "postrzeganie" in skill_profs else 0
    passive_perception = 10 + mods["wis"] + (prof_bonus if perception_prof else 0)

    # AC (default unarmored for now)
    if char_class == "barbarian":
        ac = 10 + mods["dex"] + mods["con"]
    elif char_class == "monk":
        ac = 10 + mods["dex"] + mods["wis"]
    else:
        ac = 10 + mods["dex"]

    # Saving throws
    saves = {}
    for stat in ["str", "dex", "con", "int", "wis", "cha"]:
        saves[stat] = get_saving_throw_bonus(stat, raw_stats, saving_throw_profs, level)

    # Skill bonuses
    skill_bonuses = {}
    for skill_key in SKILLS:
        skill_bonuses[skill_key] = get_skill_bonus(skill_key, raw_stats, skill_profs, expertise, level)

    return {
        "name": name,
        "player": player,
        "char_class": char_class,
        "class_name": class_data.get("name", char_class),
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
        "traits": race_data.get("traits", []),
        "class_features": class_data.get("features_1", []),
        "languages": race_data.get("languages", ["Wspólny"]),
        "armor_profs": class_data.get("armor_proficiencies", []),
        "weapon_profs": class_data.get("weapon_proficiencies", []),
        "hit_die": class_data.get("hit_die", 8),
        "spellcasting": class_data.get("spellcasting", False),
        "spellcasting_stat": class_data.get("spellcasting_stat"),
        "personality": form_data.get("personality", ""),
        "ideals": form_data.get("ideals", ""),
        "bonds": form_data.get("bonds", ""),
        "flaws": form_data.get("flaws", ""),
        "backstory": form_data.get("backstory", ""),
        "appearance": form_data.get("appearance", ""),
        "age": form_data.get("age", ""),
        "height": form_data.get("height", ""),
        "weight": form_data.get("weight", ""),
        "eyes": form_data.get("eyes", ""),
        "skin": form_data.get("skin", ""),
        "hair": form_data.get("hair", ""),
        "equipment": form_data.get("equipment", ""),
        "attacks": form_data.get("attacks", ""),
    }