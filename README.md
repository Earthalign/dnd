# ⚔️ D&D 5e Character Creator

> A full-featured web application for building Dungeons & Dragons 5th Edition characters, complete with automated stat generation, skill proficiency management, spell selection, and instant PDF character sheet export.

**Live Demo:** [Deployed on Render.com](https://your-app.onrender.com) &nbsp;|&nbsp; **Author:** [Witold Włuczkowski](https://earthalign.github.io/witoldwluczkowski/main.html)

---

## ✨ Features

### 🧙 Character Creator
- **2014 D&D 5e character rules** — PHB options plus selected official supplemental race variants; campaign availability is determined by the DM
- **Point Buy system** — 27-point budget with live cost tracking and validation
- **Dice Roll mode** — roll 4d6 drop lowest for classic stat generation
- **Auto-Assign stats** — smart stat optimizer that distributes stats based on class priorities
- **Racial bonuses** — automatically applied ASI (Ability Score Improvements) per race
- **Armor Class preview** — computed in real time, with Barbarian/Monk variants
- **Initiative & Passive Perception** — derived stats updated dynamically

Race selection groups humans, elves, dwarves, gnomes, halflings, and aasimar with their supported variants. The human variant is an optional PHB 2014 rule. Race summaries use [dnd5e.wikidot.com](https://dnd5e.wikidot.com/) as a reference; the app does not include every published lineage or setting-specific option, and the DM determines which sources are allowed.

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

## ✅ Quality Checks

Install development tools, set up the Git hooks, then run the checks locally:

```bash
python -m pip install -r requirements-dev.txt
pre-commit install
pre-commit run --all-files
pytest
```

The `Python CI` GitHub Actions workflow runs pre-commit and pytest as separate jobs on pushes and pull requests. Its Copilot summary job runs only for pushes to `main`; the read-only Copilot review job runs on pull requests from branches in this repository (not forks).

---

## 🤖 AI Commit Summaries and Reviews

The Copilot summary job describes the latest commit pushed to `main`. The review job analyzes a pull request diff using a fixed checklist (scope, correctness, regressions, tests, security/error handling, findings, and limitations). Both results appear in the workflow run's **Summary** tab; the reviewer does not post comments or modify code.

Both jobs use the official GitHub Copilot CLI. Add a fine-grained personal access token with the **Copilot Requests** account permission as the `COPILOT_GITHUB_TOKEN` Actions repository secret under **Settings → Secrets and variables → Actions**. The token must belong to a personal account with an active Copilot subscription.

Each AI job reports the number of Copilot CLI prompts it submitted. The CLI does not expose exact token consumption or the remaining account quota, so those values are reported as unavailable rather than estimated; check [GitHub billing settings](https://github.com/settings/billing) for account usage. The commit or pull request diff is sent to GitHub Copilot for processing. Do not enable these jobs for repositories containing code or data that must not be shared with GitHub.

---

## 🐳 Docker

```bash
# Build the image
docker build -t dnd-creator .

# Run the container
docker run -p 10000:10000 dnd-creator
```

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

🌐 [Portfolio & Contact](https://earthalign.github.io/witoldwluczkowski/portfolio.html)

---

## 📜 License

This project is only for private use.

D&D 5e rules and terminology are property of Wizards of the Coast. This is a fan-made tool for personal and educational use.
