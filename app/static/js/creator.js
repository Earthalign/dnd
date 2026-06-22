/* ==========================================================================
   D&D 5e Character Creator - Core App Logic
   ========================================================================== */

const CLASSES = window.CLASSES;
const RACES = window.RACES;
const BACKGROUNDS = window.BACKGROUNDS;
const SKILLS = window.SKILLS;
const SPELLS_DATA = window.SPELLS_DATA;



// App State
const state = {
    baseStats: {
        str: 10,
        dex: 10,
        con: 10,
        int: 10,
        wis: 10,
        cha: 10
    },
    skillsSelected: new Set(),
    expertiseSelected: new Set(),
    statMode: 'point_buy',
    selectedCantrips: new Set(),
};
for (let i = 1; i <= 9; i++) {
    state[`selectedSpells${i}`] = new Set();
}

const COSTS = { 8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9 };

function getModifier(score) {
    return Math.floor((score - 10) / 2);
}

function getRacialBonus(stat, raceKey) {
    const race = RACES[raceKey];
    if (!race || !race.asi) return 0;
    return race.asi[stat] || 0;
}

function calculateRemainingPoints() {
    let spent = 0;
    for (const stat of Object.keys(state.baseStats)) {
        spent += COSTS[state.baseStats[stat]] || 0;
    }
    return 27 - spent;
}

function getBackgroundSkills(bgKey) {
    const bg = BACKGROUNDS[bgKey];
    return bg ? bg.skills : [];
}

function getRaceSkills(raceKey) {
    const skills = [];
    // In D&D 5e: Wood Elf and High Elf get Keen Senses (Perception proficiency)
    if (raceKey === 'elf_high' || raceKey === 'elf_wood') {
        skills.push('postrzeganie');
    }
    // Half-Orc gets Menacing (Intimidation proficiency)
    if (raceKey === 'halforc') {
        skills.push('zastraszanie');
    }
    return skills;
}

function getSpellLimits(classKey, level = 1, subclassKey = null) {
    const limits = { cantrips: 0, max_spell_level: 0, spells_known: 0, prepared: false };
    const casterType = PROGRESSION.CASTER_TYPE[classKey];
    let actualCasterType = casterType;

    if (subclassKey === 'eldritch_knight' || subclassKey === 'arcane_trickster') {
        actualCasterType = 'third';
    }

    if (actualCasterType === 'none' || !actualCasterType) {
        return limits;
    }

    // Cantrips
    if (PROGRESSION.CANTRIPS_KNOWN[classKey]) {
        let cantripLvlKeys = Object.keys(PROGRESSION.CANTRIPS_KNOWN[classKey]).map(Number).sort((a,b)=>a-b);
        let cantripCount = 0;
        for (let l of cantripLvlKeys) {
            if (level >= l) cantripCount = PROGRESSION.CANTRIPS_KNOWN[classKey][l];
        }
        limits.cantrips = cantripCount;
    } else if (actualCasterType === 'third') {
        limits.cantrips = (level >= 10) ? 4 : (level >= 3 ? 3 : 0);
    }

    // Max Spell Level
    if (actualCasterType === 'full') {
        let maxLvlKeys = Object.keys(PROGRESSION.FULL_CASTER_SLOTS).map(Number).sort((a,b)=>a-b);
        let slots = [];
        for (let l of maxLvlKeys) {
            if (level >= l) slots = PROGRESSION.FULL_CASTER_SLOTS[l];
        }
        limits.max_spell_level = slots.reduce((max, count, idx) => count > 0 ? idx + 1 : max, 0);
    } else if (actualCasterType === 'half') {
        let maxLvlKeys = Object.keys(PROGRESSION.HALF_CASTER_SLOTS).map(Number).sort((a,b)=>a-b);
        let slots = [];
        for (let l of maxLvlKeys) {
            if (level >= l) slots = PROGRESSION.HALF_CASTER_SLOTS[l];
        }
        limits.max_spell_level = slots.reduce((max, count, idx) => count > 0 ? idx + 1 : max, 0);
    } else if (actualCasterType === 'third') {
        let maxLvlKeys = Object.keys(PROGRESSION.THIRD_CASTER_SLOTS).map(Number).sort((a,b)=>a-b);
        let slots = [];
        for (let l of maxLvlKeys) {
            if (level >= l) slots = PROGRESSION.THIRD_CASTER_SLOTS[l];
        }
        limits.max_spell_level = slots.reduce((max, count, idx) => count > 0 ? idx + 1 : max, 0);
    } else if (actualCasterType === 'pact') {
        let maxLvlKeys = Object.keys(PROGRESSION.WARLOCK_SLOTS).map(Number).sort((a,b)=>a-b);
        let warlockData = null;
        for (let l of maxLvlKeys) {
            if (level >= l) warlockData = PROGRESSION.WARLOCK_SLOTS[l];
        }
        if (warlockData) {
            limits.max_spell_level = warlockData.slot_level;
            // Also need to count Arcanum? They are essentially known spells, but let's stick to base slots for now.
        }
    }

    // Spells Known vs Prepared
    if (['cleric', 'druid', 'paladin', 'wizard'].includes(classKey)) {
        limits.prepared = true;
        const ability = CLASSES[classKey].spellcasting_stat;
        const finalScore = state.baseStats[ability] + getRacialBonus(ability, document.getElementById('race').value);
        const mod = getModifier(finalScore);
        if (classKey === 'paladin') {
            limits.spells_known = Math.max(1, mod + Math.floor(level / 2));
        } else {
            limits.spells_known = Math.max(1, mod + level);
        }
    } else {
        limits.prepared = false;
        if (PROGRESSION.SPELLS_KNOWN[classKey]) {
            let knownKeys = Object.keys(PROGRESSION.SPELLS_KNOWN[classKey]).map(Number).sort((a,b)=>a-b);
            let knownCount = 0;
            for (let l of knownKeys) {
                if (level >= l) knownCount = PROGRESSION.SPELLS_KNOWN[classKey][l];
            }
            limits.spells_known = knownCount;
        } else if (actualCasterType === 'third') {
            const thirdKnown = {3:3, 4:4, 5:4, 6:4, 7:5, 8:6, 9:6, 10:7, 11:8, 12:8, 13:9, 14:10, 15:10, 16:11, 17:11, 18:11, 19:12, 20:13};
            let knownKeys = Object.keys(thirdKnown).map(Number).sort((a,b)=>a-b);
            let knownCount = 0;
            for (let l of knownKeys) {
                if (level >= l) knownCount = thirdKnown[l];
            }
            limits.spells_known = knownCount;
        }
    }

    // Zero out if 0 slots
    if (limits.max_spell_level === 0) {
        limits.spells_known = 0;
    }

    return limits;
}

function toggleCantrip(spellId, isChecked) {
    if (isChecked) {
        state.selectedCantrips.add(spellId);
    } else {
        state.selectedCantrips.delete(spellId);
    }
    updateUI();
}

function toggleSpell(level, spellId, isChecked) {
    if (isChecked) {
        state[`selectedSpells${level}`].add(spellId);
    } else {
        state[`selectedSpells${level}`].delete(spellId);
    }
    updateUI();
}

function updateUI() {
    const raceKey = document.getElementById('race').value;
    const classKey = document.getElementById('char_class').value;
    const bgKey = document.getElementById('background').value;
    const level = parseInt(document.getElementById('level').value) || 1;
    
    // Handle Subclass Dropdown
    const subclassContainer = document.getElementById('subclass-container');
    const subclassSelect = document.getElementById('subclass');
    const subclassReqLevel = PROGRESSION.SUBCLASS_LEVEL[classKey];
    
    let subclassKey = null;
    if (subclassReqLevel && level >= subclassReqLevel) {
        subclassContainer.classList.remove('hidden');
        
        // Populate if empty or wrong class
        if (subclassSelect.dataset.class !== classKey) {
            subclassSelect.innerHTML = '';
            const subclasses = PROGRESSION.SUBCLASSES[classKey] || {};
            for (const [key, sc] of Object.entries(subclasses)) {
                const opt = document.createElement('option');
                opt.value = key;
                opt.innerText = currentLang === 'en' && sc.name_en ? sc.name_en : sc.name;
                subclassSelect.appendChild(opt);
            }
            subclassSelect.dataset.class = classKey;
        }
        subclassKey = subclassSelect.value;
    } else {
        subclassContainer.classList.add('hidden');
        subclassSelect.innerHTML = '';
        subclassSelect.dataset.class = '';
        subclassKey = null;
    }
    
    const charClass = CLASSES[classKey];
    const race = RACES[raceKey];
    const bg = BACKGROUNDS[bgKey];
    
    // 1. Update description panels
    updateDetailsInfo(raceKey, classKey, bgKey, level, subclassKey);
    
    // 2. Update Stats and Point Buy
    const remainingPoints = calculateRemainingPoints();
    const poolEl = document.getElementById('point-pool');
    const poolTextEl = document.getElementById('point-pool-text');
    
    poolEl.innerText = remainingPoints;
    
    if (remainingPoints === 0) {
        poolEl.className = "text-4xl font-black text-emerald-400 drop-shadow-[0_0_8px_rgba(52,211,153,0.3)] transition duration-300";
        poolTextEl.innerText = t('pool_spent') || "Wykorzystane!";
        poolTextEl.className = "text-xs text-emerald-400 font-bold block";
    } else if (remainingPoints < 0) {
        poolEl.className = "text-4xl font-black text-rose-500 transition duration-300 animate-pulse";
        poolTextEl.innerText = t('pool_over') || "Za dużo!";
        poolTextEl.className = "text-xs text-rose-500 font-bold block animate-pulse";
    } else {
        poolEl.className = "text-4xl font-black text-amber-500 transition duration-300";
        poolTextEl.innerText = t('pool_remaining') || "Pozostało";
        poolTextEl.className = "text-xs text-gray-500 block";
    }
    
    // Update individual stat rows
    const statKeys = ['str', 'dex', 'con', 'int', 'wis', 'cha'];
    statKeys.forEach(s => {
        const base = state.baseStats[s];
        const racial = getRacialBonus(s, raceKey);
        const final = base + racial;
        const mod = getModifier(final);
        
        // Set input values
        const htmlId = getHtmlInputId(s);
        document.getElementById(htmlId).value = base;
        
        // Primary stat suitability hint
        const primaryHintEl = document.getElementById(`${s}-primary-hint`);
        if (charClass && charClass.primary_stats && charClass.primary_stats.includes(s)) {
            primaryHintEl.innerText = t('hint_key_stat') || "Kluczowa statystyka";
            primaryHintEl.className = "text-[9px] text-amber-400 font-bold block uppercase tracking-wider mt-0.5";
        } else if (charClass && charClass.secondary_ability && charClass.secondary_ability.toLowerCase() === s) {
            primaryHintEl.innerText = t('hint_rec_stat') || "Zalecana statystyka";
            primaryHintEl.className = "text-[9px] text-indigo-400 font-bold block uppercase tracking-wider mt-0.5";
        } else {
            primaryHintEl.innerText = "";
        }
        
        // Racial Bonus
        const racialEl = document.getElementById(`${s}-racial`);
        if (racial > 0) {
            racialEl.innerText = `+${racial}`;
            racialEl.className = "text-xs px-2 py-0.5 rounded bg-amber-950/70 border border-amber-600/35 text-amber-300 font-bold font-mono";
        } else {
            racialEl.innerText = `0`;
            racialEl.className = "text-xs px-2 py-0.5 rounded bg-gray-900/60 text-gray-500 border border-gray-800 font-mono";
        }
        
        // Final Score
        document.getElementById(`${s}-final`).innerText = final;
        
        // Modifier
        const modEl = document.getElementById(`${s}-mod`);
        const modSign = mod >= 0 ? `+${mod}` : mod;
        modEl.innerText = modSign;
        if (mod > 0) {
            modEl.className = "w-10 h-10 rounded-full border-2 border-emerald-500/40 bg-emerald-950/20 text-emerald-400 flex items-center justify-center font-bold text-sm font-mono shadow-[0_0_6px_rgba(52,211,153,0.1)]";
        } else if (mod < 0) {
            modEl.className = "w-10 h-10 rounded-full border-2 border-rose-500/40 bg-rose-950/20 text-rose-400 flex items-center justify-center font-bold text-sm font-mono shadow-[0_0_6px_rgba(244,63,94,0.1)]";
        } else {
            modEl.className = "w-10 h-10 rounded-full border border-gray-700 bg-gray-900/60 text-gray-400 flex items-center justify-center font-bold text-sm font-mono";
        }
        
        // Limits
        if (state.statMode === 'dice') {
            document.getElementById(`${s}-btn-dec`).disabled = true;
            document.getElementById(`${s}-btn-inc`).disabled = true;
        } else {
            document.getElementById(`${s}-btn-dec`).disabled = (base <= 8);
            const nextCost = (COSTS[base + 1] || 99) - (COSTS[base] || 0);
            document.getElementById(`${s}-btn-inc`).disabled = (base >= 15 || nextCost > remainingPoints);
        }
    });
    
    // Derive stats preview
    const finalDex = state.baseStats['dex'] + getRacialBonus('dex', raceKey);
    const dexMod = getModifier(finalDex);
    const dexModSign = dexMod >= 0 ? `+${dexMod}` : dexMod;
    document.getElementById('initiative-preview').innerText = dexModSign;
    
    const finalWis = state.baseStats['wis'] + getRacialBonus('wis', raceKey);
    const wisMod = getModifier(finalWis);
    
    const bgSkills = getBackgroundSkills(bgKey);
    const raceSkills = getRaceSkills(raceKey);
    const autoSkills = new Set([...bgSkills, ...raceSkills]);
    
    const hasPerception = autoSkills.has('postrzeganie') || state.skillsSelected.has('postrzeganie');
    const passivePerception = 10 + wisMod + (hasPerception ? 2 : 0);
    document.getElementById('perception-preview').innerText = passivePerception;
    
    // Armor Class calculation
    const finalCon = state.baseStats['con'] + getRacialBonus('con', raceKey);
    const conMod = getModifier(finalCon);
    let acVal = 10 + dexMod;
    if (classKey === 'barbarian') {
        acVal = 10 + dexMod + conMod;
    } else if (classKey === 'monk') {
        acVal = 10 + dexMod + wisMod;
    }
    document.getElementById('ac-preview').innerText = acVal;
    
    // 3. Update Skills Section
    const isHuman = (raceKey === 'human');
    const numClassSkills = charClass ? charClass.num_skills : 2;
    const classChoices = charClass ? charClass.skill_choices : [];
    
    // Remove automatic skills from user choices
    autoSkills.forEach(s => {
        state.skillsSelected.delete(s);
    });
    
    // Validate and clean up current selections
    let classSelectedCount = 0;
    let humanSelectedCount = 0;
    
    state.skillsSelected.forEach(s => {
        const isClassChoice = classChoices === 'all' || (classChoices && classChoices.includes(s));
        if (isClassChoice && classSelectedCount < numClassSkills) {
            classSelectedCount++;
        } else if (isHuman && humanSelectedCount < 1) {
            humanSelectedCount++;
        } else {
            state.skillsSelected.delete(s);
            state.expertiseSelected.delete(s);
        }
    });
    
    // Build skill choices instruction
    let selectionInstructions = t('skill_banner_class', {cls: charClass ? (currentLang === 'en' ? charClass.name_en || charClass.name : charClass.name) : '', num: numClassSkills, sel: classSelectedCount}) || `Klasa <strong>${charClass ? charClass.name : ''}</strong> wymaga wyboru <strong>${numClassSkills}</strong> biegłości (Wybrano: ${classSelectedCount}/${numClassSkills}).`;
    if (isHuman) {
        selectionInstructions += t('skill_banner_human', {sel: humanSelectedCount}) || ` Jako <strong>człowiek</strong> wybierasz dodatkowo <strong>1 dowolną</strong> biegłość (Wybrano: ${humanSelectedCount}/1).`;
    }
    document.getElementById('skill-selection-info').innerHTML = selectionInstructions;
    
    // Populate skills grid
    const skillListContainer = document.getElementById('skill-list-container');
    skillListContainer.innerHTML = '';
    
    const sortedSkillKeys = Object.keys(SKILLS).sort((a, b) => SKILLS[a].name.localeCompare(SKILLS[b].name));
    
    sortedSkillKeys.forEach(s => {
        const skill = SKILLS[s];
        const statAbbr = skill.stat;
        const statName = statAbbr.toUpperCase();
        
        const finalStatScore = state.baseStats[statAbbr] + getRacialBonus(statAbbr, raceKey);
        const modVal = getModifier(finalStatScore);
        
        const isAuto = autoSkills.has(s);
        const isClassChoice = classChoices === 'all' || (classChoices && classChoices.includes(s));
        const isProficient = isAuto || state.skillsSelected.has(s);
        
        // Calculate skill modifier
        const profBonus = 2; // lvl 1
        let finalBonus = modVal;
        const hasExpertise = state.expertiseSelected.has(s) && isProficient && classKey === 'rogue';
        
        if (hasExpertise) {
            finalBonus += profBonus * 2;
        } else if (isProficient) {
            finalBonus += profBonus;
        }
        
        const finalBonusSign = finalBonus >= 0 ? `+${finalBonus}` : finalBonus;
        
        // Badge info
        let sourceBadge = '';
        if (bgSkills.includes(s)) {
            sourceBadge = `<span class="text-[9px] px-1.5 py-0.5 rounded bg-indigo-950 border border-indigo-700/40 text-indigo-300 font-bold ml-1.5">${t('badge_background') || "Pochodzenie"}</span>`;
        } else if (raceSkills.includes(s)) {
            sourceBadge = `<span class="text-[9px] px-1.5 py-0.5 rounded bg-emerald-950 border border-emerald-700/40 text-emerald-300 font-bold ml-1.5">${t('badge_race') || "Rasa"}</span>`;
        } else if (state.skillsSelected.has(s)) {
            const isClass = classChoices === 'all' || (classChoices && classChoices.includes(s));
            if (isClass) {
                sourceBadge = `<span class="text-[9px] px-1.5 py-0.5 rounded bg-amber-950 border border-amber-700/40 text-amber-300 font-bold ml-1.5">${t('badge_class') || "Klasa"}</span>`;
            } else {
                sourceBadge = `<span class="text-[9px] px-1.5 py-0.5 rounded bg-purple-950 border border-purple-700/40 text-purple-300 font-bold ml-1.5">${t('badge_human') || "Człowiek"}</span>`;
            }
        }
        
        // Checkbox html
        let checkboxHtml = '';
        if (isAuto) {
            checkboxHtml = `
                <input type="checkbox" name="skills" value="${s}" checked
                    class="w-4 h-4 rounded border-gray-700 text-amber-500 bg-gray-900 focus:ring-amber-500 cursor-not-allowed"
                    style="accent-color: #d4af37;" onclick="return false;">
            `;
        } else {
            const canCheck = isProficient || 
                             (isClassChoice && classSelectedCount < numClassSkills) || 
                             (isHuman && humanSelectedCount < 1);
            
            const disabledAttr = canCheck ? '' : 'disabled';
            checkboxHtml = `
                <input type="checkbox" name="skills" value="${s}" ${isProficient ? 'checked' : ''} ${disabledAttr}
                    onchange="toggleSkill('${s}', this.checked)"
                    class="w-4 h-4 rounded border-gray-700 text-amber-500 bg-gray-900 focus:ring-amber-500 cursor-pointer disabled:opacity-20 disabled:cursor-not-allowed"
                    style="accent-color: #d4af37;">
            `;
        }
        
        // Expertise html (Rogue only)
        let expertiseHtml = '';
        if (classKey === 'rogue') {
            const expCount = state.expertiseSelected.size;
            const canCheckExp = hasExpertise || (isProficient && expCount < 2);
            const disabledExpAttr = (isProficient && canCheckExp) ? '' : 'disabled';
            
            expertiseHtml = `
                <div class="flex items-center gap-1 ml-3 border-l border-gray-800 pl-3">
                    <label class="text-[10px] ${isProficient ? 'text-gray-400' : 'text-gray-600'} cursor-pointer flex items-center gap-1 font-semibold uppercase tracking-wider">
                        <input type="checkbox" name="expertise" value="${s}" ${hasExpertise ? 'checked' : ''} ${disabledExpAttr}
                            onchange="toggleExpertise('${s}', this.checked)"
                            class="w-3.5 h-3.5 rounded-full border-gray-700 text-amber-600 bg-gray-900 focus:ring-amber-500 cursor-pointer disabled:opacity-20 disabled:cursor-not-allowed"
                            style="accent-color: #dfa839;">
                        <span>Exp</span>
                    </label>
                </div>
            `;
        }
        
        const card = document.createElement('div');
        card.className = `flex items-center justify-between p-3 rounded-xl border transition-all duration-200 ${
            isProficient 
                ? 'bg-amber-950/10 border-amber-500/25 shadow-[0_2px_8px_rgba(212,175,55,0.02)]' 
                : 'bg-gray-900/30 border-gray-850 hover:border-gray-800'
        }`;
        
        const skillNameText = SKILLS[s] ? (currentLang === 'en' && SKILLS[s].name_en ? SKILLS[s].name_en : SKILLS[s].name) : s;
        
        card.innerHTML = `
            <div class="flex items-center gap-2.5">
                ${checkboxHtml}
                <div class="flex flex-col">
                    <div class="flex items-center">
                        <span class="font-bold text-gray-200 text-sm leading-tight">${skillNameText}</span>
                        ${sourceBadge}
                    </div>
                    <span class="text-[10px] text-gray-500 font-semibold uppercase tracking-wider mt-0.5">${t('stat_' + statAbbr.toLowerCase()) || statName}</span>
                </div>
            </div>
            <div class="flex items-center">
                ${expertiseHtml}
                <span class="font-extrabold text-sm text-amber-400 font-mono w-10 text-right ml-2">${finalBonusSign}</span>
            </div>
        `;
        
        skillListContainer.appendChild(card);
    });
    
    // 4. Update Expertise selection panel (Rogue only)
    const expertiseSection = document.getElementById('expertise-section');
    if (classKey === 'rogue') {
        expertiseSection.classList.remove('hidden');
        const expSelected = state.expertiseSelected.size;
        document.getElementById('expertise-info').innerHTML = t('expertise_info', {n: expSelected}) || `Jako łotrzyk, wybierz <strong>2</strong> umiejętności z zaznaczonych do ekspertyzy (Wybrano: ${expSelected}/2)`;
    } else {
        expertiseSection.classList.add('hidden');
        state.expertiseSelected.clear();
    }

    // 5. Update Spell Selection Section
    const spellSection = document.getElementById('spell-section');
    const limits = getSpellLimits(classKey, level, subclassKey);
    let cantripLimit = limits.cantrips;
    let spellsKnownLimit = limits.spells_known;
    
    let allowedCantripClasses = [];
    if (charClass && charClass.spellcasting) {
        allowedCantripClasses.push(classKey);
    }
    if (raceKey === 'elf_high') {
        cantripLimit += 1;
        allowedCantripClasses.push('wizard');
    }

    const isSpellcaster = (charClass && charClass.spellcasting && (limits.cantrips > 0 || limits.spells1 > 0)) || (raceKey === 'elf_high');
    
    if (!isSpellcaster) {
        spellSection.classList.add('hidden');
        state.selectedCantrips.clear();
        state.selectedSpells1.clear();
    } else {
        spellSection.classList.remove('hidden');
        
        // Render spell stats (only if actual class is spellcaster)
        const statsHeader = document.getElementById('spellcasting-stats-header');
        if (charClass && charClass.spellcasting) {
            statsHeader.classList.remove('invisible');
            const spellcastingStat = charClass.spellcasting_stat;
            const finalStatScore = state.baseStats[spellcastingStat] + getRacialBonus(spellcastingStat, raceKey);
            const spellcastingMod = getModifier(finalStatScore);
            const profBonus = 2; // Level 1
            const spellSaveDC = 8 + profBonus + spellcastingMod;
            const spellAttackBonus = profBonus + spellcastingMod;
            const spellAttackSign = spellAttackBonus >= 0 ? `+${spellAttackBonus}` : spellAttackBonus;
            
            document.getElementById('spell-ability-preview').innerText = spellcastingStat.toUpperCase();
            document.getElementById('spell-dc-preview').innerText = spellSaveDC;
            document.getElementById('spell-attack-preview').innerText = spellAttackSign;
        } else {
            statsHeader.classList.add('invisible');
        }

        // Cantrips population
        const dynamicSpellsContainer = document.getElementById('dynamic-spells-container');
        dynamicSpellsContainer.innerHTML = '';

        if (cantripLimit > 0) {
            const allowedCantrips = (SPELLS_DATA.cantrip || []).filter(s => {
                return s.classes.some(c => allowedCantripClasses.includes(c));
            });

            // Clean outdated
            state.selectedCantrips.forEach(spellId => {
                if (!allowedCantrips.some(s => s.id === spellId)) {
                    state.selectedCantrips.delete(spellId);
                }
            });
            if (state.selectedCantrips.size > cantripLimit) {
                const arr = Array.from(state.selectedCantrips);
                state.selectedCantrips.clear();
                arr.slice(0, cantripLimit).forEach(id => state.selectedCantrips.add(id));
            }

            let cantripsHtml = `
                <div>
                    <h3 class="text-sm font-bold text-amber-400 mb-2 flex items-center gap-2">
                        <span class="bg-amber-500/20 border border-amber-500/30 text-amber-300 px-2 py-0.5 rounded text-[10px] uppercase tracking-wider font-mono">Lvl 0</span>
                        <span data-i18n="lbl_cantrips">${t('lbl_cantrips') || 'Sztuczki (Cantrips)'}</span>
                        <span class="text-gray-500 text-xs ml-auto">${state.selectedCantrips.size} / ${cantripLimit}</span>
                    </h3>
                    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2">
            `;
            
            allowedCantrips.forEach(s => {
                const isChecked = state.selectedCantrips.has(s.id);
                const disabledAttr = (!isChecked && state.selectedCantrips.size >= cantripLimit) ? 'disabled' : '';
                const name = currentLang === 'en' ? s.name_en : s.name_pl;
                const checkedClass = isChecked ? 'bg-amber-950/15 border-amber-500/35 text-amber-300 shadow-[0_2px_8px_rgba(212,175,55,0.02)]' : 'bg-gray-900/30 border-gray-850 text-gray-400 hover:border-gray-800';
                cantripsHtml += `
                    <label class="flex items-center gap-2.5 p-2.5 rounded-xl border text-xs cursor-pointer transition-all duration-200 ${checkedClass}">
                        <input type="checkbox" name="selected_cantrips" value="${s.id}" ${isChecked ? 'checked' : ''} ${disabledAttr}
                            onchange="toggleCantrip('${s.id}', this.checked)"
                            class="w-4 h-4 rounded border-gray-700 text-amber-500 bg-gray-900 focus:ring-amber-500 cursor-pointer disabled:opacity-20 disabled:cursor-not-allowed"
                            style="accent-color: #d4af37;">
                        <span class="font-bold leading-tight">${name}</span>
                    </label>
                `;
            });
            cantripsHtml += `</div></div>`;
            dynamicSpellsContainer.innerHTML += cantripsHtml;
        } else {
            state.selectedCantrips.clear();
        }

        // Higher level spells
        let totalSelectedSpells = 0;
        for (let l = 1; l <= 9; l++) {
            totalSelectedSpells += state[`selectedSpells${l}`].size;
        }

        for (let l = 1; l <= limits.max_spell_level; l++) {
            const allowedSpells = (SPELLS_DATA[`level_${l}`] || []).filter(s => s.classes.includes(classKey));
            
            // Clean outdated
            state[`selectedSpells${l}`].forEach(spellId => {
                if (!allowedSpells.some(s => s.id === spellId)) {
                    state[`selectedSpells${l}`].delete(spellId);
                }
            });

            if (allowedSpells.length > 0) {
                let lvlHtml = `
                    <div>
                        <h3 class="text-sm font-bold text-amber-400 mb-2 flex items-center gap-2">
                            <span class="bg-indigo-500/20 border border-indigo-500/30 text-indigo-300 px-2 py-0.5 rounded text-[10px] uppercase tracking-wider font-mono">Lvl ${l}</span>
                            <span>${t('lbl_spells_' + l) || `Zaklęcia ${l}. poziomu`}</span>
                            <span class="text-gray-500 text-xs ml-auto">${state[`selectedSpells${l}`].size}</span>
                        </h3>
                        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2">
                `;
                
                allowedSpells.forEach(s => {
                    const isChecked = state[`selectedSpells${l}`].has(s.id);
                    // For prepared casters or known casters, the limit applies globally across all levels, except cantrips.
                    const disabledAttr = (!isChecked && totalSelectedSpells >= spellsKnownLimit) ? 'disabled' : '';
                    const name = currentLang === 'en' ? s.name_en : s.name_pl;
                    const checkedClass = isChecked ? 'bg-indigo-950/15 border-indigo-500/35 text-indigo-300 shadow-[0_2px_8px_rgba(99,102,241,0.02)]' : 'bg-gray-900/30 border-gray-850 text-gray-400 hover:border-gray-800';
                    lvlHtml += `
                        <label class="flex items-center gap-2.5 p-2.5 rounded-xl border text-xs cursor-pointer transition-all duration-200 ${checkedClass}">
                            <input type="checkbox" name="selected_spells_${l}" value="${s.id}" ${isChecked ? 'checked' : ''} ${disabledAttr}
                                onchange="toggleSpell(${l}, '${s.id}', this.checked)"
                                class="w-4 h-4 rounded border-gray-700 text-indigo-500 bg-gray-900 focus:ring-indigo-500 cursor-pointer disabled:opacity-20 disabled:cursor-not-allowed"
                                style="accent-color: #6366f1;">
                            <span class="font-bold leading-tight">${name}</span>
                        </label>
                    `;
                });
                lvlHtml += `</div></div>`;
                dynamicSpellsContainer.innerHTML += lvlHtml;
            } else {
                state[`selectedSpells${l}`].clear();
            }
        }
        
        // Clear any spells above max level
        for (let l = limits.max_spell_level + 1; l <= 9; l++) {
            state[`selectedSpells${l}`].clear();
        }
    }
    
    // 6. Validation Check
    let formIsValid = true;
    let errorMessages = [];
    
    if (state.statMode !== 'dice' && remainingPoints !== 0) {
        formIsValid = false;
        errorMessages.push(t('err_points', {n: remainingPoints}) || "Musisz wykorzystać dokładnie 27 punktów w systemie Point Buy (aktualnie pozostało: " + remainingPoints + " pkt).");
    }
    
    if (classSelectedCount < numClassSkills) {
        formIsValid = false;
        errorMessages.push(t('err_class_skills', {need: numClassSkills, have: classSelectedCount}) || `Klasa wymaga wyboru ${numClassSkills} umiejętności (wybrano ${classSelectedCount}).`);
    }
    
    if (isHuman && humanSelectedCount < 1) {
        formIsValid = false;
        errorMessages.push(t('err_human_skill') || "Jako człowiek musisz wybrać 1 dodatkową umiejętność.");
    }
    
    if (classKey === 'rogue' && state.expertiseSelected.size < 2) {
        formIsValid = false;
        errorMessages.push(t('err_expertise') || "Jako łotrzyk musisz wybrać dokładnie 2 umiejętności do ekspertyzy.");
    }

    if (isSpellcaster) {
        if (state.selectedCantrips.size < cantripLimit) {
            formIsValid = false;
            errorMessages.push(t('err_cantrips', {need: cantripLimit, have: state.selectedCantrips.size}) || `Klasa wymaga wyboru dokładnie ${cantripLimit} sztuczek (wybrano ${state.selectedCantrips.size}).`);
        }
        let totalSelectedSpells = 0;
        for (let l = 1; l <= 9; l++) {
            totalSelectedSpells += state[`selectedSpells${l}`].size;
        }
        if (totalSelectedSpells < spellsKnownLimit) {
            formIsValid = false;
            errorMessages.push(t('err_spells1', {need: spellsKnownLimit, have: totalSelectedSpells}) || `Klasa wymaga wyboru dokładnie ${spellsKnownLimit} zaklęć wyższych poziomów (wybrano ${totalSelectedSpells}).`);
        }
    }
    
    const submitBtn = document.getElementById('submit-btn');
    const validationSummary = document.getElementById('validation-summary');
    
    if (formIsValid) {
        submitBtn.disabled = false;
        submitBtn.className = "w-full py-4 rounded-xl bg-gradient-to-r from-amber-600 to-amber-500 hover:from-amber-500 hover:to-amber-400 text-gray-950 font-black text-lg shadow-[0_0_20px_rgba(212,175,55,0.25)] hover:shadow-[0_0_30px_rgba(212,175,55,0.4)] transition duration-300 uppercase tracking-widest cursor-pointer transform hover:-translate-y-0.5 active:translate-y-0";
        validationSummary.innerHTML = `
            <div class="bg-emerald-950/30 border border-emerald-500/30 text-emerald-400 px-4 py-3.5 rounded-xl text-center text-sm font-semibold flex items-center justify-center gap-2 shadow-[0_2px_12px_rgba(16,185,129,0.05)]">
                <svg class="w-5 h-5 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                ${t('valid_ok') || "Wszystkie warunki są spełnione! Karta postaci jest gotowa do pobrania."}
            </div>
        `;
    } else {
        submitBtn.disabled = true;
        submitBtn.className = "w-full py-4 rounded-xl bg-gray-900/60 text-gray-600 border border-gray-850 font-black text-lg uppercase tracking-widest cursor-not-allowed opacity-40 transition duration-300";
        
        let errorsHtml = '<ul class="list-disc list-inside space-y-1">';
        errorMessages.forEach(msg => {
            errorsHtml += `<li>${msg}</li>`;
        });
        errorsHtml += '</ul>';
        
        validationSummary.innerHTML = `
            <div class="bg-rose-950/20 border border-rose-500/25 text-rose-300 px-4 py-3.5 rounded-xl text-xs leading-relaxed shadow-[0_2px_12px_rgba(244,63,94,0.05)]">
                <span class="font-bold block mb-1.5 text-rose-400 uppercase tracking-wider text-[10px]">${t('valid_header') || "Wymagania do spełnienia:"}</span>
                ${errorsHtml}
            </div>
        `;
    }
}

function updateDetailsInfo(raceKey, classKey, bgKey, level = 1, subclassKey = null) {
    const race = RACES[raceKey];
    const charClass = CLASSES[classKey];
    const bg = BACKGROUNDS[bgKey];
    
    // Check current lang for names
    const useEn = (currentLang === 'en');
    
    // Update Subclass Detail Card
    const subclassCard = document.getElementById('subclass-details-card');
    if (subclassKey && PROGRESSION.SUBCLASSES[classKey] && PROGRESSION.SUBCLASSES[classKey][subclassKey]) {
        const sc = PROGRESSION.SUBCLASSES[classKey][subclassKey];
        const scName = useEn && sc.name_en ? sc.name_en : sc.name;
        const scDesc = useEn && sc.description_en ? sc.description_en : sc.description;
        
        let featuresHtml = '';
        if (sc.features) {
            const sortedLvls = Object.keys(sc.features).map(Number).sort((a,b)=>a-b);
            for (const lvl of sortedLvls) {
                const isActive = level >= lvl;
                const opacityClass = isActive ? 'opacity-100' : 'opacity-40';
                const dotColor = isActive ? 'bg-amber-500' : 'bg-gray-700';
                const textColor = isActive ? 'text-amber-300' : 'text-gray-500';
                
                featuresHtml += `<div class="mt-2 ${opacityClass} transition-opacity duration-300">`;
                featuresHtml += `<div class="text-[10px] uppercase font-bold tracking-widest ${textColor} flex items-center gap-1.5 mb-1"><span class="w-1.5 h-1.5 rounded-full ${dotColor}"></span>Poziom ${lvl}</div>`;
                sc.features[lvl].forEach(feat => {
                    featuresHtml += `<div class="text-xs text-gray-400 pl-3 leading-normal border-l border-gray-800 ml-0.5 py-0.5">• ${feat}</div>`;
                });
                featuresHtml += `</div>`;
            }
        }
        
        subclassCard.innerHTML = `
            <div class="space-y-2.5">
                <div class="flex items-center justify-between border-b border-gray-850 pb-1.5">
                    <span class="text-xs font-bold text-amber-500 font-serif">${t('lbl_subclass') || 'Subklasa'}: ${scName}</span>
                </div>
                <p class="text-xs text-gray-400 leading-relaxed italic">${scDesc}</p>
                <div class="pt-1">${featuresHtml}</div>
            </div>
        `;
        subclassCard.classList.remove('hidden');
    } else {
        subclassCard.innerHTML = '';
        subclassCard.classList.add('hidden');
    }
    
    // Update Race Detail Card
    if (race) {
        const raceName = useEn && race.name_en ? race.name_en : race.name;
        const raceDesc = useEn && race.description_en ? race.description_en : race.description;
        let traitsHtml = race.traits.map(t_trait => `<li class="text-xs text-gray-400 leading-normal">• ${t_trait}</li>`).join('');
        let asiHtml = Object.entries(race.asi).map(([s, val]) => 
            `<span class="text-[9px] font-bold bg-amber-500/10 border border-amber-500/25 text-amber-400 px-2 py-0.5 rounded font-mono">${s.toUpperCase()} +${val}</span>`
        ).join(' ');
        
        document.getElementById('race-details-card').innerHTML = `
            <div class="space-y-2.5">
                <div class="flex items-center justify-between border-b border-gray-850 pb-1.5">
                    <span class="text-xs font-bold text-amber-500 font-serif">${t('card_race')}: ${raceName}</span>
                    <span class="text-[9px] text-gray-500 uppercase tracking-widest font-bold">${t('card_race_traits')}</span>
                </div>
                <p class="text-xs text-gray-400 italic">${raceDesc}</p>
                <div class="flex flex-wrap gap-1.5 pt-0.5">
                    ${asiHtml}
                    <span class="text-[9px] font-bold bg-gray-800 text-gray-300 px-2 py-0.5 rounded font-mono">${t('card_speed')}: ${race.speed}m</span>
                    <span class="text-[9px] font-bold bg-gray-800 text-gray-300 px-2 py-0.5 rounded font-mono">${t('card_size')}: ${race.size}</span>
                </div>
                <div class="border-t border-gray-850/80 pt-2 space-y-1.5">
                    <span class="text-[10px] font-bold text-amber-400/90 block uppercase tracking-wider">${t('card_senses')}</span>
                    <ul class="space-y-1">${traitsHtml}</ul>
                </div>
            </div>
        `;
    }
    
    // Update Class Detail Card
    if (charClass) {
        const className = useEn && charClass.name_en ? charClass.name_en : charClass.name;
        const classDesc = useEn && charClass.description_en ? charClass.description_en : charClass.description;
        let featuresHtml = charClass.features_1.map(f => `<li class="text-xs text-gray-400 leading-normal">• ${f}</li>`).join('');
        let savesHtml = charClass.saving_throws.map(s => 
            `<span class="text-[9px] font-bold bg-indigo-500/10 border border-indigo-500/25 text-indigo-400 px-2 py-0.5 rounded font-mono">${s.toUpperCase()}</span>`
        ).join(' ');
        
        document.getElementById('class-details-card').innerHTML = `
            <div class="space-y-2.5">
                <div class="flex items-center justify-between border-b border-gray-850 pb-1.5">
                    <span class="text-xs font-bold text-amber-500 font-serif">${t('card_class')}: ${className}</span>
                    <span class="text-[9px] text-gray-500 uppercase tracking-widest font-bold">${t('card_class_traits')}</span>
                </div>
                <p class="text-xs text-gray-400 italic">${classDesc}</p>
                <div class="flex flex-wrap gap-1.5 pt-0.5">
                    <span class="text-[9px] font-bold bg-rose-500/10 border border-rose-500/25 text-rose-400 px-2 py-0.5 rounded font-mono">${t('card_hit_die')}: d${charClass.hit_die}</span>
                    <span class="text-[9px] font-bold bg-gray-800 text-gray-300 px-2 py-0.5 rounded font-mono">${t('card_saves')}</span>
                    ${savesHtml}
                </div>
                <div class="border-t border-gray-850/80 pt-2 space-y-1.5">
                    <span class="text-[10px] font-bold text-amber-400/90 block uppercase tracking-wider">${t('card_start_feats')}</span>
                    <ul class="space-y-1">${featuresHtml}</ul>
                </div>
            </div>
        `;
    }
    
    // Update Background Detail Card
    if (bg) {
        const bgName = useEn && bg.name_en ? bg.name_en : bg.name;
        const bgDesc = useEn && bg.description_en ? bg.description_en : bg.description;
        let skillsHtml = bg.skills.map(s => 
            `<span class="text-[9px] font-bold bg-purple-500/10 border border-purple-500/25 text-purple-400 px-2 py-0.5 rounded">${SKILLS[s] ? SKILLS[s].name : s}</span>`
        ).join(' ');
        
        document.getElementById('bg-details-card').innerHTML = `
            <div class="space-y-2.5">
                <div class="flex items-center justify-between border-b border-gray-850 pb-1.5">
                    <span class="text-xs font-bold text-amber-500 font-serif">${t('card_bg')}: ${bgName}</span>
                    <span class="text-[9px] text-gray-500 uppercase tracking-widest font-bold">${t('card_bg_traits')}</span>
                </div>
                <p class="text-xs text-gray-400 italic">${bgDesc}</p>
                <div class="flex flex-wrap gap-1.5 pt-0.5">
                    ${skillsHtml}
                </div>
                <div class="border-t border-gray-850/80 pt-2 space-y-1">
                    <span class="text-[10px] font-bold text-amber-400/90 block uppercase tracking-wider">${t('card_bg_feat')}</span>
                    <span class="text-xs text-gray-300 block font-semibold leading-normal">${bg.feature}</span>
                </div>
            </div>
        `;
    }
}

function getHtmlInputId(s) {
    const mapping = { str: 'strength', dex: 'dexterity', con: 'constitution', int: 'intelligence', wis: 'wisdom', cha: 'charisma' };
    return mapping[s];
}

function changeStat(statAbbr, amount) {
    const base = state.baseStats[statAbbr];
    const newVal = base + amount;
    
    if (newVal >= 8 && newVal <= 15) {
        state.baseStats[statAbbr] = newVal;
        updateUI();
    }
}

function toggleSkill(skillKey, isChecked) {
    if (isChecked) {
        state.skillsSelected.add(skillKey);
    } else {
        state.skillsSelected.delete(skillKey);
        state.expertiseSelected.delete(skillKey);
    }
    updateUI();
}

function toggleExpertise(skillKey, isChecked) {
    if (isChecked) {
        state.expertiseSelected.add(skillKey);
    } else {
        state.expertiseSelected.delete(skillKey);
    }
    updateUI();
}

async function loadAutoStats(mode) {
    const char_class = document.getElementById('char_class').value;
    const race = document.getElementById('race').value;

    // Simple loading feedback
    const poolEl = document.getElementById('point-pool');
    poolEl.innerText = "...";

    const response = await fetch('/api/auto-stats', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mode, char_class, race })
    });

    const data = await response.json();
    
    const pyToAbbr = { str: 'str', dex: 'dex', con: 'con', int: 'int', wis: 'wis', cha: 'cha' };
    for (const [pyKey, val] of Object.entries(data.stats)) {
        const abbr = pyToAbbr[pyKey];
        if (abbr) {
            state.baseStats[abbr] = val;
        }
    }
    
    // Clear selections on auto stats load to avoid invalid combinations
    state.skillsSelected.clear();
    state.expertiseSelected.clear();
    state.selectedCantrips.clear();
    state.selectedSpells1.clear();
    state.statMode = 'point_buy';
    document.getElementById('stat_mode').value = 'point_buy';
    
    updateUI();
}

// Initialize App
updateUI();
