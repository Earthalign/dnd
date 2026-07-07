from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random

from app.core.rules import CLASSES, RACES, BACKGROUNDS, SKILLS, SPELLS, FEATS, WILD_SHAPE_FORMS
from app.core.equipment import CLASS_EQUIPMENT, WEAPONS, ARMORS
from app.core import progression
from app.schemas.character import CharacterCreateSchema
from app.services.character import (
    build_character_sheet,
    auto_assign_stats_try_harder,
    auto_assign_stats_balanced,
    validate_point_buy
)
from app.services.pdf import generate_character_pdf

app = FastAPI(title="D&D 5e Character Creator")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup HTML templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={
            "classes": CLASSES,
            "races": RACES,
            "backgrounds": BACKGROUNDS,
            "skills": SKILLS,
            "spells": SPELLS,
            "feats": FEATS,
            "class_equipment": CLASS_EQUIPMENT,
            "weapons": WEAPONS,
            "armors": ARMORS,
            "wild_shape_forms": WILD_SHAPE_FORMS,
            "progression": {
                "PROFICIENCY_BY_LEVEL": progression.PROFICIENCY_BY_LEVEL,
                "SUBCLASS_LEVEL": progression.SUBCLASS_LEVEL,
                "SUBCLASSES": progression.SUBCLASSES,
                "CANTRIPS_KNOWN": progression.CANTRIPS_KNOWN,
                "SPELLS_KNOWN": progression.SPELLS_KNOWN,
                "FULL_CASTER_SLOTS": progression.FULL_CASTER_SLOTS,
                "HALF_CASTER_SLOTS": progression.HALF_CASTER_SLOTS,
                "THIRD_CASTER_SLOTS": progression.THIRD_CASTER_SLOTS,
                "WARLOCK_SLOTS": progression.WARLOCK_SLOTS,
                "CASTER_TYPE": progression.CASTER_TYPE,
                "CLASS_FEATURES": progression.CLASS_FEATURES,
                "ASI_LEVELS": progression.ASI_LEVELS
            }
        }
    )

@app.get("/spellbook", response_class=HTMLResponse)
async def spellbook(request: Request):
    return templates.TemplateResponse(request=request, name="spellbook.html")

@app.post("/api/auto-stats")
async def api_auto_stats(data: dict):
    """Endpoint returning automatically distributed stats based on mode."""
    mode = data.get("mode", "try_harder")
    char_class = data.get("char_class", "fighter")
    race = data.get("race", "human")
    
    if mode == "try_harder":
        stats = auto_assign_stats_try_harder(char_class, race)
    else:
        stats = auto_assign_stats_balanced(char_class, race)
        
    return {"stats": stats}


@app.post("/api/auto-character")
async def api_auto_character(data: dict = {}):
    """Generate a fully random, coherent D&D 5e character at the requested level."""
    # Use provided level or default to 1
    level = int(data.get("level", 1))
    level = max(1, min(20, level))  # clamp to valid range
    
    # Random picks
    char_class = random.choice(list(CLASSES.keys()))
    race = random.choice(list(RACES.keys()))
    background = random.choice(list(BACKGROUNDS.keys()))
    
    ALIGNMENTS = [
        "Praworządny Dobry", "Neutralny Dobry", "Chaotyczny Dobry",
        "Praworządny Neutralny", "Prawdziwy Neutralny", "Chaotyczny Neutralny",
        "Praworządny Zły", "Neutralny Zły", "Chaotyczny Zły"
    ]
    alignment = random.choice(ALIGNMENTS)

    NAMES = [
        "Arador", "Sylvara", "Tormund", "Elara", "Grimshaw", "Lyria", "Aldric",
        "Faewyn", "Brom", "Seraphel", "Kazimir", "Thalia", "Vorak", "Neria",
        "Durgrim", "Isolde", "Ragnar", "Caelia", "Oswin", "Mireille"
    ]
    name = random.choice(NAMES)

    # Stats: roll 4d6 drop lowest for each stat
    def roll_stat():
        rolls = sorted([random.randint(1, 6) for _ in range(4)])
        return sum(rolls[1:])  # drop lowest

    raw = {stat: roll_stat() for stat in ["str", "dex", "con", "int", "wis", "cha"]}

    # Skills: pick from class choices
    class_data = CLASSES[char_class]
    num_skills = class_data.get("num_skills", 2)
    choices = class_data.get("skill_choices", [])
    if choices == "all":
        choices = list(SKILLS.keys())
    skills = random.sample(choices, min(num_skills, len(choices)))

    # Cantrips: pick random cantrips for spellcasting classes
    cantrips = []
    spell_lvls = {}
    caster_type = progression.CASTER_TYPE.get(char_class, "none")
    if caster_type != "none":
        class_cantrips = [s["id"] for s in SPELLS.get("cantrip", []) if char_class in s["classes"]]
        # Pick cantrip count from progression
        ct_known = progression.CANTRIPS_KNOWN.get(char_class, {})
        ct_count = 0
        for l in sorted(ct_known.keys()):
            if level >= l: ct_count = ct_known[l]
        cantrips = random.sample(class_cantrips, min(ct_count, len(class_cantrips)))
        
        # Pick 1-2 level 1 spells
        l1_spells = [s["id"] for s in SPELLS.get("level_1", []) if char_class in s["classes"]]
        spell_lvls["spells_1"] = random.sample(l1_spells, min(2, len(l1_spells)))

    # ASI slots
    asi_level_list = [l for l in (progression.ASI_LEVELS.get(char_class) or []) if level >= l]
    feat_keys = list(FEATS.keys())
    asi_slots = []
    for _ in asi_level_list:
        choice = random.choice(["feat", "+2", "+1+1"])
        slot = {"type": choice, "feat": "", "stat1": "", "stat2": ""}
        if choice == "feat":
            slot["feat"] = random.choice(feat_keys)
        elif choice == "+2":
            slot["stat1"] = random.choice(["str", "dex", "con", "int", "wis", "cha"])
        else:
            stats_pool = ["str", "dex", "con", "int", "wis", "cha"]
            slot["stat1"], slot["stat2"] = random.sample(stats_pool, 2)
        asi_slots.append(slot)

    # Equipment: pick a random package
    eq_options = CLASS_EQUIPMENT.get(char_class, {}).get("options", [])
    eq_package = random.choice(eq_options)["id"] if eq_options else None

    # Human variant free feat
    human_variant_feat = ""
    if race == "human_variant":
        human_variant_feat = random.choice(feat_keys)

    return {
        "name": name,
        "char_class": char_class,
        "race": race,
        "background": background,
        "level": level,
        "alignment": alignment,
        "stats": raw,
        "skills": skills,
        "expertise": [],
        "cantrips": cantrips,
        **{f"spells_{i}": spell_lvls.get(f"spells_{i}", []) for i in range(1, 10)},
        "asi_slots": asi_slots,
        "human_variant_feat": human_variant_feat,
        "equipment_package": eq_package,
        "background_skills": BACKGROUNDS.get(background, {}).get("skills", []),
    }

@app.post("/generate-pdf")
async def generate_pdf(request: Request):
    # Parse form data through Pydantic schema
    form_data = await CharacterCreateSchema.from_form(request)
    
    # Validate Point Buy if selected
    if form_data.stat_mode == "point_buy":
        stats_to_validate = {
            "str": form_data.strength,
            "dex": form_data.dexterity,
            "con": form_data.constitution,
            "int": form_data.intelligence,
            "wis": form_data.wisdom,
            "cha": form_data.charisma,
        }
        is_valid, err_msg = validate_point_buy(stats_to_validate)
        if not is_valid:
            raise HTTPException(status_code=400, detail=err_msg)
            
    # Build complete character sheet calculations
    sheet = build_character_sheet(form_data)
    
    # Map selected spells to Polish names for the PDF sheet
    cantrip_names = []
    all_spell_ids = []
    for spell_id in form_data.selected_cantrips:
        for s in SPELLS.get("cantrip", []):
            if s["id"] == spell_id:
                cantrip_names.append(s["name_pl"])
                all_spell_ids.append((spell_id, s["name_pl"], 0))
                break
    
    sheet["cantrip_names"] = cantrip_names
    
    for level in range(1, 10):
        spell_names = []
        selected = getattr(form_data, f"selected_spells_{level}")
        for spell_id in selected:
            for s in SPELLS.get(f"level_{level}", []):
                if s["id"] == spell_id:
                    spell_names.append(s["name_pl"])
                    all_spell_ids.append((spell_id, s["name_pl"], level))
                    break
        sheet[f"spell{level}_names"] = spell_names
    
    sheet["all_spell_ids"] = all_spell_ids
    
    # Generate PDF in-memory (returning bytes)
    try:
        pdf_bytes = generate_character_pdf(sheet)
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Błąd generowania PDF: {str(e)}")
    
    filename = f"character_{form_data.name.replace(' ', '_')}.pdf"
    
    # Send PDF byte stream as attachment
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )