from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.core.rules import CLASSES, RACES, BACKGROUNDS, SKILLS, SPELLS
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
            "spells": SPELLS
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
    for spell_id in form_data.selected_cantrips:
        for s in SPELLS.get("cantrip", []):
            if s["id"] == spell_id:
                cantrip_names.append(s["name_pl"])
                break
    
    spell1_names = []
    for spell_id in form_data.selected_spells_1:
        for s in SPELLS.get("level_1", []):
            if s["id"] == spell_id:
                spell1_names.append(s["name_pl"])
                break
    
    sheet["cantrip_names"] = cantrip_names
    sheet["spell1_names"] = spell1_names
    
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