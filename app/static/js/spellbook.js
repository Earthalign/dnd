/* ==========================================================================
   Spellbook Page Controller (Polish Edition)
   Loads spells locally from /api/spells with filtering & instant search
   ========================================================================== */

let debounceTimer = null;

const CLASS_PL_NAMES = {
    bard: 'Bard',
    cleric: 'Kleryk',
    druid: 'Druid',
    paladin: 'Paladyn',
    ranger: 'Łowca',
    sorcerer: 'Zaklinacz',
    warlock: 'Czarnoksiężnik',
    wizard: 'Czarodziej / Mag',
    artificer: 'Artificer'
};

async function fetchSpells() {
    const classVal = document.getElementById('class-select').value;
    const levelVal = document.getElementById('level-select').value;
    const searchVal = document.getElementById('search-input').value.trim();

    const container = document.getElementById('spell-container');
    const loading = document.getElementById('loading');
    const countEl = document.getElementById('spell-count');

    loading.classList.remove('hidden');

    try {
        const params = new URLSearchParams();
        if (classVal && classVal !== 'all') params.append('class_name', classVal);
        if (levelVal && levelVal !== 'all') params.append('level', levelVal);
        if (searchVal) params.append('search', searchVal);

        const url = `/api/spells?${params.toString()}`;
        const res = await fetch(url);
        if (!res.ok) throw new Error('Błąd pobierania zaklęć z serwera');

        const spells = await res.json();
        renderSpellCards(spells, container);
        if (countEl) countEl.innerText = spells.length;
    } catch (e) {
        console.error('Błąd podczas ładowania zaklęć:', e);
        container.innerHTML = `
            <div class="col-span-full bg-rose-950/40 border border-rose-500/40 rounded-xl p-6 text-center text-rose-300">
                <p class="font-bold text-lg mb-1">Wystąpił błąd podczas ładowania zaklęć</p>
                <p class="text-sm text-gray-400">${e.message || 'Spróbuj odświeżyć stronę lub zmienić filtry.'}</p>
            </div>
        `;
        if (countEl) countEl.innerText = '0';
    } finally {
        loading.classList.add('hidden');
    }
}

function renderSpellCards(spells, container) {
    container.innerHTML = '';

    if (!spells || spells.length === 0) {
        container.innerHTML = `
            <div class="col-span-full bg-gray-900/40 border border-gray-800 rounded-2xl p-12 text-center text-gray-400">
                <p class="text-3xl mb-3">🔍</p>
                <p class="text-lg font-serif text-amber-400 mb-1">Brak zaklęć spełniających kryteria</p>
                <p class="text-xs text-gray-500">Zmień wybraną klasę, krąg lub wyczyść pole wyszukiwania.</p>
            </div>
        `;
        return;
    }

    spells.forEach(s => {
        const card = document.createElement('div');
        card.className = 'spell-card';

        // Title and School/Level
        const levelBadge = s.level === 0 ? 'Sztuczka' : `${s.level}. Krąg`;
        const schoolText = s.school ? s.school : levelBadge;

        // Polish classes badges
        const classBadges = (s.classes || []).map(c => {
            const plName = CLASS_PL_NAMES[c] || c;
            return `<span class="bg-amber-950/40 border border-amber-600/30 text-amber-400 px-1.5 py-0.5 rounded text-[10px] font-mono">${plName}</span>`;
        }).join(' ');

        // Format Description paragraphs
        let formattedDesc = s.desc || '';
        if (s.desc_html && s.desc_html.includes('<br>')) {
            formattedDesc = s.desc_html;
        } else {
            formattedDesc = formattedDesc.replace(/\n\n/g, '<br><br>').replace(/\n/g, '<br>');
        }

        card.innerHTML = `
            <div class="flex items-start justify-between gap-2 border-b border-amber-600/20 pb-2 mb-2">
                <div class="spell-card-title !mb-0 !pb-0 !border-0">${s.name_pl}</div>
                <span class="bg-amber-500/10 border border-amber-500/30 text-amber-300 px-2 py-0.5 rounded text-[11px] font-bold font-mono whitespace-nowrap">
                    ${levelBadge}
                </span>
            </div>
            
            <div class="spell-card-meta flex items-center justify-between text-xs text-gray-400 mb-2">
                <span>${schoolText}</span>
                <div class="flex flex-wrap gap-1">${classBadges}</div>
            </div>

            <div class="spell-card-stats">
                <div><strong>Czas:</strong> ${s.casting_time || '-'}</div>
                <div><strong>Zasięg:</strong> ${s.range || '-'}</div>
                <div><strong>Komp:</strong> ${s.components || '-'}</div>
                <div><strong>Trwanie:</strong> ${s.duration || '-'}</div>
            </div>

            <div class="spell-card-desc">
                ${formattedDesc}
            </div>
        `;

        container.appendChild(card);
    });
}

function handleSearchDebounced() {
    const clearBtn = document.getElementById('clear-search');
    const searchVal = document.getElementById('search-input').value;
    if (clearBtn) {
        if (searchVal.length > 0) {
            clearBtn.classList.remove('hidden');
        } else {
            clearBtn.classList.add('hidden');
        }
    }

    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
        fetchSpells();
    }, 250);
}

function clearSearch() {
    const input = document.getElementById('search-input');
    if (input) {
        input.value = '';
        const clearBtn = document.getElementById('clear-search');
        if (clearBtn) clearBtn.classList.add('hidden');
        fetchSpells();
    }
}

// Initial load
document.addEventListener('DOMContentLoaded', () => {
    fetchSpells();
});
