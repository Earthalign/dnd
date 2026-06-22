/* ============================================
   Dice Rolling Modal – 5d6 drop 2 lowest
   ============================================ */

const STAT_ORDER = ['str','dex','con','int','wis','cha'];
const STAT_I18N_KEYS = {
    str: 'stat_str', dex: 'stat_dex', con: 'stat_con',
    int: 'stat_int', wis: 'stat_wis', cha: 'stat_cha'
};

const faceRotations = {
    1: { x: 0, y: 0 },
    2: { x: 0, y: -90 },
    3: { x: 0, y: -180 },
    4: { x: 0, y: 90 },
    5: { x: -90, y: 0 },
    6: { x: 90, y: 0 }
};

function setDieRotation(el, result) {
    const SPINS = 720;
    const xRand = Math.floor(Math.random() * 3) * 360 + SPINS;
    const yRand = Math.floor(Math.random() * 3) * 360 + SPINS;
    const r = faceRotations[result];
    el.style.transform = `translateZ(-25px) rotateX(${r.x + xRand}deg) rotateY(${r.y + yRand}deg)`;
}

let diceResults = {};

function rollOneDie() {
    return Math.floor(Math.random() * 6) + 1;
}

function roll5d6() {
    const dice = [];
    for (let i = 0; i < 5; i++) dice.push(rollOneDie());
    return dice;
}

function openDiceModal() {
    const overlay = document.getElementById('dice-overlay');
    overlay.classList.add('active');
    buildDiceModalContent();
    runDiceSequence();
}

function closeDiceModal() {
    document.getElementById('dice-overlay').classList.remove('active');
}

function buildDiceModalContent() {
    const container = document.getElementById('dice-stats-container');
    container.innerHTML = '';

    STAT_ORDER.forEach(stat => {
        const row = document.createElement('div');
        row.className = 'dice-stat-row';
        row.id = `dice-row-${stat}`;
        row.innerHTML = `
            <div class="flex items-center justify-between mb-2">
                <span class="text-sm font-bold text-gray-300 font-serif uppercase tracking-wider">${t(STAT_I18N_KEYS[stat])}</span>
                <span class="dice-stat-result" id="dice-result-${stat}">—</span>
            </div>
            <div class="flex items-center justify-center" id="dice-boxes-${stat}">
                ${[0,1,2,3,4].map(i => `
                    <div class="scene">
                        <div class="cube" id="die-${stat}-${i}">
                            <div class="cube__face cube__face--1">⚀</div>
                            <div class="cube__face cube__face--2">⚁</div>
                            <div class="cube__face cube__face--3">⚂</div>
                            <div class="cube__face cube__face--4">⚃</div>
                            <div class="cube__face cube__face--5">⚄</div>
                            <div class="cube__face cube__face--6">⚅</div>
                        </div>
                    </div>
                `).join('')}
            </div>
            <div class="text-center mt-1.5">
                <span class="text-[10px] text-gray-600 font-semibold uppercase tracking-wider" id="dice-dropped-${stat}"></span>
            </div>
        `;
        container.appendChild(row);
    });

    // Update modal title
    document.getElementById('dice-modal-title').textContent = t('dice_title');
    document.getElementById('dice-modal-subtitle').textContent = t('dice_subtitle');
    // Hide action buttons until done
    document.getElementById('dice-actions').classList.add('hidden');
}

async function runDiceSequence() {
    diceResults = {};
    document.getElementById('dice-actions').classList.add('hidden');

    for (const stat of STAT_ORDER) {
        await rollStatAnimated(stat);
        await sleep(300);
    }

    // Show action buttons
    const actionsEl = document.getElementById('dice-actions');
    actionsEl.classList.remove('hidden');
    document.getElementById('dice-accept-btn').textContent = t('dice_accept');
    document.getElementById('dice-reroll-btn').textContent = t('dice_reroll');
    document.getElementById('dice-close-btn').textContent = t('dice_close');
}

async function rollStatAnimated(stat) {
    const row = document.getElementById(`dice-row-${stat}`);
    row.classList.add('active');

    const dieEls = [];
    for (let i = 0; i < 5; i++) {
        dieEls.push(document.getElementById(`die-${stat}-${i}`));
    }

    // Phase 1: All dice "rolling" animation
    dieEls.forEach(el => {
        el.style.transition = 'none';
        el.classList.add('rolling');
    });

    await sleep(600);

    // Phase 2: Stop dice one by one
    const finalDice = roll5d6();

    for (let i = 0; i < 5; i++) {
        await sleep(150);
        dieEls[i].classList.remove('rolling');
        dieEls[i].style.transition = 'transform 1.5s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
        setDieRotation(dieEls[i], finalDice[i]);
    }

    await sleep(1400); // Wait for the last die to finish its 1.5s transition

    // Phase 3: Mark dropped dice and show result
    const sorted = finalDice.map((v, i) => ({v, i})).sort((a, b) => a.v - b.v);
    const droppedIndices = [sorted[0].i, sorted[1].i];
    const keptValues = [];

    for (let i = 0; i < 5; i++) {
        if (droppedIndices.includes(i)) {
            dieEls[i].classList.add('dropped');
        } else {
            dieEls[i].classList.add('kept');
            keptValues.push(finalDice[i]);
        }
    }

    const total = keptValues.reduce((a, b) => a + b, 0);
    diceResults[stat] = total;

    // Show dropped info
    const droppedVals = droppedIndices.map(i => finalDice[i]).join(', ');
    document.getElementById(`dice-dropped-${stat}`).textContent =
        `${t('dice_dropped')}: ${droppedVals}`;

    // Show result
    row.classList.add('done');
    document.getElementById(`dice-result-${stat}`).textContent = total;
}

function acceptDiceRolls() {
    // Apply dice results to state
    for (const [stat, val] of Object.entries(diceResults)) {
        state.baseStats[stat] = val;
    }
    state.statMode = 'dice';
    document.getElementById('stat_mode').value = 'dice';
    state.skillsSelected.clear();
    state.expertiseSelected.clear();
    state.selectedCantrips.clear();
    state.selectedSpells1.clear();
    closeDiceModal();
    updateUI();
}

function rerollDice() {
    buildDiceModalContent();
    runDiceSequence();
}

function resetToPointBuy() {
    state.statMode = 'point_buy';
    document.getElementById('stat_mode').value = 'point_buy';
    state.baseStats = { str: 10, dex: 10, con: 10, int: 10, wis: 10, cha: 10 };
    state.skillsSelected.clear();
    state.expertiseSelected.clear();
    state.selectedCantrips.clear();
    state.selectedSpells1.clear();
    updateUI();
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
