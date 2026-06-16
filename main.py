from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from character import build_character_sheet, auto_assign_stats_try_harder, auto_assign_stats_balanced, validate_point_buy
from dnd_data import CLASSES, RACES, BACKGROUNDS, SKILLS, SPELLS

app = FastAPI(title="D&D 5e Character Creator")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup szablonów HTML
templates = Jinja2Templates(directory="templates")

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
    """Endpoint zwracający automatycznie przydzielone statystyki."""
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
    form_data_raw = await request.form()
    
    # Wyciągnięcie atrybutów bazowych do walidacji Point Buy
    stats = {
        "str": int(form_data_raw.get("strength", 10)),
        "dex": int(form_data_raw.get("dexterity", 10)),
        "con": int(form_data_raw.get("constitution", 10)),
        "int": int(form_data_raw.get("intelligence", 10)),
        "wis": int(form_data_raw.get("wisdom", 10)),
        "cha": int(form_data_raw.get("charisma", 10)),
    }
    
    # Pobieranie trybu generowania atrybutów
    stat_mode = form_data_raw.get("stat_mode", "point_buy")
    
    # Walidacja Point Buy
    if stat_mode == "point_buy":
        is_valid, err_msg = validate_point_buy(stats)
        if not is_valid:
            from fastapi import HTTPException
            raise HTTPException(status_code=400, detail=err_msg)
        
    # Budowanie słownika form_data
    form_data = dict(form_data_raw)
    
    # Przemapowanie nazw atrybutów z formularza HTML (strength -> str) na te używane w character.py
    form_data["str"] = stats["str"]
    form_data["dex"] = stats["dex"]
    form_data["con"] = stats["con"]
    form_data["int"] = stats["int"]
    form_data["wis"] = stats["wis"]
    form_data["cha"] = stats["cha"]
    
    # Pobieranie list wielokrotnego wyboru (biegłości i ekspertyzy)
    form_data["skills"] = form_data_raw.getlist("skills")
    form_data["expertise"] = form_data_raw.getlist("expertise")
    
    # Pobieranie wybranych czarów
    form_data["selected_cantrips"] = form_data_raw.getlist("selected_cantrips")
    form_data["selected_spells_1"] = form_data_raw.getlist("selected_spells_1")
    
    form_data["level"] = int(form_data.get("level", 1))
    
    sheet = build_character_sheet(form_data)
    
    # Dodaj czary do sheeta (w PL)
    from dnd_data import SPELLS as SPELLS_DATA
    
    cantrip_names = []
    for spell_id in form_data.get("selected_cantrips", []):
        for s in SPELLS_DATA.get("cantrip", []):
            if s["id"] == spell_id:
                cantrip_names.append(s["name_pl"])
                break
    
    spell1_names = []
    for spell_id in form_data.get("selected_spells_1", []):
        for s in SPELLS_DATA.get("level_1", []):
            if s["id"] == spell_id:
                spell1_names.append(s["name_pl"])
                break
    
    sheet["cantrip_names"] = cantrip_names
    sheet["spell1_names"] = spell1_names
    
    # Generowanie unikalnego PDF w katalogu
    name = form_data.get("name", "Bohater")
    pdf_path = f"character_{name.replace(' ', '_')}.pdf"
    from utils.pdf_generator import generate_character_pdf
    generate_character_pdf(sheet, pdf_path)
    
    return FileResponse(pdf_path, media_type='application/pdf', filename=pdf_path)