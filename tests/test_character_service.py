import json

import pytest

from app.schemas.character import CharacterCreateSchema
from app.services.character import (
    apply_racial_asi,
    auto_assign_stats_balanced,
    build_character_sheet,
    get_modifier,
    get_proficiency_bonus,
    get_racial_asi,
    get_skill_bonus,
    validate_custom_stats,
    validate_point_buy,
    validate_starting_gold_purchases,
)


def test_apply_racial_asi_applies_bonus_and_caps_score():
    stats = {"int": 19, "dex": 14}

    result = apply_racial_asi(stats, "gnome_forest")

    assert result == {"int": 20, "dex": 15}
    assert stats == {"int": 19, "dex": 14}


def test_custom_racial_asi_requires_different_abilities():
    custom_asi = json.dumps({
        "mode": "two_plus_one",
        "plus_two": "int",
        "plus_one": "int",
    })

    with pytest.raises(ValueError, match="dwie różne cechy"):
        get_racial_asi("human", custom_asi)


def test_point_buy_accepts_exact_budget_and_rejects_unspent_points():
    valid_stats = {"str": 15, "dex": 15, "con": 15, "int": 8, "wis": 8, "cha": 8}
    under_budget_stats = {"str": 10, "dex": 10, "con": 10, "int": 10, "wis": 10, "cha": 10}

    assert validate_point_buy(valid_stats) == (True, "OK")
    is_valid, message = validate_point_buy(under_budget_stats)
    assert not is_valid
    assert "dokładnie wszystkie 27 punktów" in message


@pytest.mark.parametrize(
    ("score", "expected_modifier"),
    [(8, -1), (9, -1), (10, 0), (11, 0), (12, 1)],
)
def test_get_modifier_uses_dnd_score_thresholds(score, expected_modifier):
    assert get_modifier(score) == expected_modifier


@pytest.mark.parametrize(
    ("level", "expected_bonus"),
    [(1, 2), (5, 3), (9, 4), (13, 5), (17, 6)],
)
def test_proficiency_bonus_increases_at_level_thresholds(level, expected_bonus):
    assert get_proficiency_bonus(level) == expected_bonus


def test_balanced_stats_use_the_full_point_buy_budget():
    stats = auto_assign_stats_balanced("fighter", "human")

    assert validate_point_buy(stats) == (True, "OK")
    assert min(stats.values()) >= 10


def test_custom_stats_accept_endpoints_and_reject_out_of_range_values():
    assert validate_custom_stats({"str": 3, "dex": 18}) == (True, "OK")

    is_valid, message = validate_custom_stats({"str": 19})
    assert not is_valid
    assert "3-18" in message


def test_build_character_sheet_applies_race_bonuses():
    sheet = build_character_sheet(CharacterCreateSchema(race="gnome_forest"))

    assert sheet["race_name"] == "Gnom Leśny"
    assert sheet["stats"]["int"] == 12
    assert sheet["stats"]["dex"] == 11


def test_skill_expertise_doubles_proficiency_bonus():
    stats = {"wis": 14}

    assert get_skill_bonus("postrzeganie", stats, ["postrzeganie"], [], 5) == 5
    assert get_skill_bonus("postrzeganie", stats, [], ["postrzeganie"], 5) == 8


def test_starting_gold_validation_returns_remaining_coins():
    assert validate_starting_gold_purchases("fighter", 100, "{}", "none") == ({}, 0, 10000)

    with pytest.raises(ValueError, match="wzoru startowego"):
        validate_starting_gold_purchases("fighter", 40, "{}", "none")
