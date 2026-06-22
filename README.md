# ⚔️ D&D 5e Character Creator

> A full-featured web application for building Dungeons & Dragons 5th Edition characters, complete with automated stat generation, skill proficiency management, spell selection, and instant PDF character sheet export.

**Live Demo:** [Deployed on Render.com](https://your-app.onrender.com) &nbsp;|&nbsp; **Author:** [Witold Włuczkowski](https://earthalign.github.io/witoldwluczkowski/strona2.html)

---

## ✨ Features

### 🧙 Character Creator
- **Full D&D 5e PHB compliance** — races, classes, backgrounds, and skill rules implemented faithfully
- **Point Buy system** — 27-point budget with live cost tracking and validation
- **Dice Roll mode** — roll 4d6 drop lowest for classic stat generation
- **Auto-Assign stats** — smart stat optimizer that distributes stats based on class priorities
- **Racial bonuses** — automatically applied ASI (Ability Score Improvements) per race
- **Armor Class preview** — computed in real time, with Barbarian/Monk variants
- **Initiative & Passive Perception** — derived stats updated dynamically

### 🎓 Skill Proficiencies
- Class-based skill choices with correct limits (e.g., Rogue gets 4, Fighter gets 2)
- Background automatic proficiencies (locked, cannot be deselected)
- Racial proficiencies (High Elf, Wood Elf → Perception; Half-Orc → Intimidation)
- Human bonus skill (1 free extra proficiency)
- **Expertise system** for Rogues (double proficiency on 2 skills)

### 🔮 Spell Selection
- Dynamic spell lists filtered by class at character level 1
- Correct spell slot counts per class (e.g., Wizard prepares INT mod + 1 spells)
- Cantrip selection with class/racial limits (High Elf gets a free Wizard cantrip)
- Spell Save DC & Spell Attack Bonus preview
- Spell data stored locally — no external API required for character creation

### 📖 Spellbook Browser
- Browse the full D&D 5e spell list via the [dnd5eapi.co](https://www.dnd5eapi.co) public API
- Filter by class and spell level
- Print-ready spell cards in standard playing card format (63×88mm)
- Rate-limit protection with chunked fetching (max 10 spells/batch)

### 📄 PDF Export
- Instant in-memory PDF generation using **PyMuPDF**
- Fills an official-style interactive D&D 5e character sheet template
- No disk writes — PDF is generated in RAM and streamed directly to the browser
- Bilingual support: Polish/English spell names on the character sheet

### 🌐 Multilingual UI
- Full Polish/English toggle (PL/EN button)
- i18n system with dynamic label replacement throughout the entire UI
- Persists language choice during the session

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.11+, FastAPI, Uvicorn |
| **Templating** | Jinja2 |
| **PDF Generation** | PyMuPDF (fitz) |
| **Frontend** | Vanilla HTML5, CSS3, JavaScript (ES2020) |
| **Styling** | Tailwind CSS (CDN), custom CSS |
| **Fonts** | Google Fonts — Cinzel (display), Outfit (body) |
| **Deployment** | Docker, Render.com |

---

## 🗂️ Project Structure

```
dnd/
├── main.py                     # FastAPI app entry point
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container configuration
├── render.yaml                 # Render.com deployment config
│
└── app/
    ├── core/
    │   └── rules.py            # D&D 5e data: classes, races, spells, backgrounds
    ├── schemas/
    │   └── character.py        # Pydantic schema for form validation
    ├── services/
    │   ├── character.py        # Business logic: stat calculation, sheet building
    │   └── pdf.py              # In-memory PDF generation service
    ├── templates/
    │   ├── index.html          # Main character creator page
    │   └── spellbook.html      # Spell browser page
    ├── static/
    │   ├── css/
    │   │   ├── style.css       # Main app styles
    │   │   └── spellbook.css   # Spell card styles (web + print)
    │   └── js/
    │       ├── creator.js      # Character creator logic (state, UI, validation)
    │       ├── i18n.js         # Internationalization (PL/EN)
    │       ├── dice.js         # Dice rolling modal
    │       └── spellbook.js    # Spellbook API fetching & rendering
    └── data/
        └── karta-postaci-interaktywna.pdf  # PDF template
```

---

## 🚀 Running Locally

### Prerequisites
- Python 3.11+
- pip

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/dnd.git
cd dnd

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
# or
.\venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the development server
uvicorn main:app --reload --port 10000
```

Open your browser at **http://localhost:10000**

---

## 🐳 Docker

```bash
# Build the image
docker build -t dnd-creator .

# Run the container
docker run -p 10000:10000 dnd-creator
```

---

## 🌍 Deploying to Render.com

This project is pre-configured for Render.com via `render.yaml`.

1. Push the repository to GitHub
2. Connect your repo in the Render.com dashboard
3. Render will automatically detect `render.yaml` and build/deploy the Docker container
4. The app will be available at your Render subdomain

> **Note:** The `karta-postaci-interaktywna.pdf` template must be present in `app/data/` for PDF generation to work.

---

## 🔌 API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Main character creator UI |
| `GET` | `/spellbook` | Spell browser UI |
| `POST` | `/generate-pdf` | Generate & download character sheet PDF |
| `POST` | `/api/auto-stats` | Get optimized stat distribution for a class |

---

## 📦 Dependencies

```
fastapi>=0.110.0
uvicorn>=0.28.0
jinja2>=3.1.3
python-multipart>=0.0.9
pymupdf>=1.24.0
```

---

## 👤 Author

**Witold Włuczkowski**

🌐 [Portfolio & Contact](https://earthalign.github.io/witoldwluczkowski/strona2.html)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

D&D 5e rules and terminology are property of Wizards of the Coast. This is a fan-made tool for personal and educational use.
