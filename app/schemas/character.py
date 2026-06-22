from pydantic import BaseModel, Field
from typing import List, Optional
from fastapi import Request

class CharacterCreateSchema(BaseModel):
    name: str = "Bohater"
    char_class: str = "fighter"
    level: int = 1
    race: str = "human"
    background: str = "folk_hero"
    alignment: str = "Neutralny"
    strength: int = 10
    dexterity: int = 10
    constitution: int = 10
    intelligence: int = 10
    wisdom: int = 10
    charisma: int = 10
    stat_mode: str = "point_buy"
    skills: List[str] = Field(default_factory=list)
    expertise: List[str] = Field(default_factory=list)
    subclass: Optional[str] = None
    selected_cantrips: List[str] = Field(default_factory=list)
    selected_spells_1: List[str] = Field(default_factory=list)
    selected_spells_2: List[str] = Field(default_factory=list)
    selected_spells_3: List[str] = Field(default_factory=list)
    selected_spells_4: List[str] = Field(default_factory=list)
    selected_spells_5: List[str] = Field(default_factory=list)
    selected_spells_6: List[str] = Field(default_factory=list)
    selected_spells_7: List[str] = Field(default_factory=list)
    selected_spells_8: List[str] = Field(default_factory=list)
    selected_spells_9: List[str] = Field(default_factory=list)
    personality: str = ""
    ideals: str = ""
    bonds: str = ""
    flaws: str = ""
    backstory: str = ""
    appearance: str = ""
    age: str = ""
    height: str = ""
    weight: str = ""
    eyes: str = ""
    skin: str = ""
    hair: str = ""
    equipment: str = ""
    attacks: str = ""
    player: str = ""

    @classmethod
    async def from_form(cls, request: Request) -> "CharacterCreateSchema":
        """Parse character fields from incoming FastAPI Request form data."""
        form = await request.form()
        return cls(
            name=str(form.get("name", "Bohater")),
            char_class=str(form.get("char_class", "fighter")),
            level=int(form.get("level", 1)),
            race=str(form.get("race", "human")),
            background=str(form.get("background", "folk_hero")),
            alignment=str(form.get("alignment", "Neutralny")),
            strength=int(form.get("strength", 10)),
            dexterity=int(form.get("dexterity", 10)),
            constitution=int(form.get("constitution", 10)),
            intelligence=int(form.get("intelligence", 10)),
            wisdom=int(form.get("wisdom", 10)),
            charisma=int(form.get("charisma", 10)),
            stat_mode=str(form.get("stat_mode", "point_buy")),
            skills=form.getlist("skills"),
            expertise=form.getlist("expertise"),
            subclass=form.get("subclass", None) if form.get("subclass", "") != "" else None,
            selected_cantrips=form.getlist("selected_cantrips"),
            selected_spells_1=form.getlist("selected_spells_1"),
            selected_spells_2=form.getlist("selected_spells_2"),
            selected_spells_3=form.getlist("selected_spells_3"),
            selected_spells_4=form.getlist("selected_spells_4"),
            selected_spells_5=form.getlist("selected_spells_5"),
            selected_spells_6=form.getlist("selected_spells_6"),
            selected_spells_7=form.getlist("selected_spells_7"),
            selected_spells_8=form.getlist("selected_spells_8"),
            selected_spells_9=form.getlist("selected_spells_9"),
            personality=str(form.get("personality", "")),
            ideals=str(form.get("ideals", "")),
            bonds=str(form.get("bonds", "")),
            flaws=str(form.get("flaws", "")),
            backstory=str(form.get("backstory", "")),
            appearance=str(form.get("appearance", "")),
            age=str(form.get("age", "")),
            height=str(form.get("height", "")),
            weight=str(form.get("weight", "")),
            eyes=str(form.get("eyes", "")),
            skin=str(form.get("skin", "")),
            hair=str(form.get("hair", "")),
            equipment=str(form.get("equipment", "")),
            attacks=str(form.get("attacks", "")),
            player=str(form.get("player", "")),
        )
