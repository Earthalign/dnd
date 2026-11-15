from app.core.rules import RACES, RACE_FAMILIES, RACE_SUBRACE_KEYS


def test_race_families_reference_races_and_hide_subraces_from_top_level():
    for family in RACE_FAMILIES.values():
        assert family["subraces"]
        assert all(race_key in RACES for race_key in family["subraces"])
        assert all(race_key in RACE_SUBRACE_KEYS for race_key in family["subraces"])


def test_human_variants_are_grouped_and_have_distinct_asi_rules():
    assert RACE_FAMILIES["human"]["subraces"] == ["human", "human_variant"]
    assert RACES["human"]["asi"] == {
        "str": 1,
        "dex": 1,
        "con": 1,
        "int": 1,
        "wis": 1,
        "cha": 1,
    }
    assert RACES["human_variant"]["asi"] == {}


def test_halfling_family_includes_phb_and_supplement_subraces():
    assert RACE_FAMILIES["halfling"]["subraces"] == [
        "halfling_lightfoot",
        "halfling_stout",
        "halfling_ghostwise",
        "halfling_lotusden",
        "halfling_mark_hospitality",
        "halfling_mark_healing",
    ]
    assert RACES["halfling_stout"]["asi"] == {"dex": 2, "con": 1}
    assert any("poison damage" in trait for trait in RACES["halfling_stout"]["traits_en"])
    assert RACES["halfling_ghostwise"]["asi"] == {"dex": 2, "wis": 1}
    assert RACES["halfling_lotusden"]["asi"] == {"dex": 2, "wis": 1}
    assert RACES["halfling_mark_hospitality"]["asi"] == {"dex": 2, "cha": 1}
    assert RACES["halfling_mark_healing"]["asi"] == {"dex": 2, "wis": 1}


def test_non_phb_race_corrections_are_present():
    assert "Wycofania" in RACES["goblin"]["traits"][1]
    assert "stworzeniu większemu od ciebie" in RACES["goblin"]["traits"][2]
    assert "bronią do walki wręcz" in RACES["halforc"]["traits"][2]
    assert "jako czar 2. poziomu" in RACES["tiefling"]["traits"][2]
    assert "Zr lub Kon" in RACES["dragonborn"]["traits"][1]
    assert "połowie poziomu" in RACES["aasimar_scourge"]["traits"][4]
    assert "elf_drow" in RACE_FAMILIES["elf"]["subraces"]
    assert "gnome_deep" in RACE_FAMILIES["gnome"]["subraces"]
    assert "aasimar_scourge" in RACE_FAMILIES["aasimar"]["subraces"]
    assert "aasimar_fallen" in RACE_FAMILIES["aasimar"]["subraces"]
