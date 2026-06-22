/* ==========================================================================
   Spellbook Page Controller
   ========================================================================== */

let classSpellsList = [];

async function loadSpells() {
    const cls = document.getElementById('class-select').value;
    if (!cls) return;

    const container = document.getElementById('spell-container');
    const loading = document.getElementById('loading');
    
    container.innerHTML = '';
    loading.classList.remove('hidden');

    try {
        // Get spells list for class (contains name, level, url)
        const res = await fetch(`https://www.dnd5eapi.co/api/classes/${cls}/spells`);
        const data = await res.json();
        
        classSpellsList = data.results; 
        
        // Set default level to cantrip if available to prevent loading 300 spells at once
        document.getElementById('level-select').value = "0";
        
        await filterSpells();
    } catch (e) {
        console.error(e);
        container.innerHTML = '<p class="text-rose-500">Błąd podczas pobierania zaklęć.</p>';
    } finally {
        loading.classList.add('hidden');
    }
}

async function filterSpells() {
    const level = document.getElementById('level-select').value;
    const container = document.getElementById('spell-container');
    const loading = document.getElementById('loading');
    
    container.innerHTML = '';
    loading.classList.remove('hidden');
    
    try {
        // Filter the base list by level
        let filteredList = classSpellsList;
        if (level !== 'all') {
            filteredList = classSpellsList.filter(s => s.level.toString() === level);
        }
        
        // Limit to 50 spells max at a time to prevent browser/API crash
        if (filteredList.length > 50) {
            const warning = document.createElement('div');
            warning.className = 'col-span-full text-amber-500 text-sm mb-4 bg-amber-950/30 p-3 rounded-lg border border-amber-500/30';
            warning.innerText = `Wyświetlanie pierwszych 50 z ${filteredList.length} zaklęć dla lepszej wydajności. Wybierz konkretny poziom, aby zobaczyć wszystkie.`;
            container.appendChild(warning);
            filteredList = filteredList.slice(0, 50);
        }
        
        // Fetch details in small chunks to avoid rate limits (HTTP 429)
        const chunkSize = 10;
        const fullSpells = [];
        
        for (let i = 0; i < filteredList.length; i += chunkSize) {
            const chunk = filteredList.slice(i, i + chunkSize);
            const promises = chunk.map(s => fetch(`https://www.dnd5eapi.co${s.url}`).then(r => r.json()));
            const results = await Promise.all(promises);
            fullSpells.push(...results);
        }

        // Render cards
        fullSpells.forEach(s => {
            const levelText = s.level === 0 ? 'Cantrip' : `Level ${s.level}`;
            const desc = s.desc ? s.desc.join('\n') : '';
            const comps = s.components ? s.components.join(', ') + (s.material ? ` (${s.material})` : '') : '';
            
            const card = document.createElement('div');
            card.className = 'spell-card';
            card.innerHTML = `
                <div class="spell-card-title">${s.name}</div>
                <div class="spell-card-meta">${levelText} ${s.school ? s.school.name : ''}</div>
                <div class="spell-card-stats">
                    <div><strong>Cast:</strong> ${s.casting_time}</div>
                    <div><strong>Range:</strong> ${s.range}</div>
                    <div><strong>Comp:</strong> ${comps}</div>
                    <div><strong>Dur:</strong> ${s.duration}</div>
                </div>
                <div class="spell-card-desc">${desc}</div>
            `;
            container.appendChild(card);
        });
        
    } catch (e) {
        console.error(e);
        container.innerHTML += '<p class="text-rose-500 col-span-full">Wystąpił problem podczas ładowania części zaklęć.</p>';
    } finally {
        loading.classList.add('hidden');
    }
}
