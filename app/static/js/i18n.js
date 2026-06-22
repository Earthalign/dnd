/* ============================================
   i18n – Polish / English translations
   ============================================ */
const TRANSLATIONS = {
    pl: {
        page_title: 'Kreator Postaci D&D 5e',
        page_subtitle: 'Zbuduj swojego bohatera zgodnie z oficjalnymi zasadami Player\'s Handbook',
        section_identity: 'Kim jesteś?',
        lbl_name: 'Imię Postaci',
        lbl_class: 'Klasa',
        lbl_level: 'Poziom',
        lbl_race: 'Rasa',
        lbl_background: 'Pochodzenie (Background)',
        lbl_alignment: 'Charakter (Alignment)',
        section_stats: 'Atrybuty i Statystyki',
        btn_try_harder: 'Auto: Try Harder 💪',
        btn_balanced: 'Auto: Balanced ⚖️',
        btn_roll_dice: '🎲 Losuj Kości',
        point_buy_title: 'System Kupowania Punktów',
        point_buy_desc: 'Bazowy zakres: 8 - 15. Koszt rośnie nieliniowo (14: 7pkt, 15: 9pkt). Musisz rozdać <strong>dokładnie wszystkie 27 punktów</strong>!',
        pool_remaining: 'Pozostało',
        pool_spent: 'Wykorzystane!',
        pool_over: 'Za dużo!',
        lbl_base: 'Bazowa',
        lbl_race_bonus: 'Rasa',
        lbl_total: 'Wynik',
        lbl_mod: 'Mod.',
        hint_key_stat: 'Kluczowa statystyka',
        hint_rec_stat: 'Zalecana statystyka',
        section_skills: 'Biegłości i Umiejętności',
        lbl_prof_bonus: 'Premia z biegłości:',
        lbl_initiative: 'Inicjatywa:',
        lbl_passive_perc: 'Pasywna percepcja:',
        lbl_ac: 'Pancerz (KP):',
        expertise_title: 'Wiedza Eksperta (Expertise)',
        expertise_info: 'Jako łotrzyk, wybierz <strong>2</strong> umiejętności z zaznaczonych do ekspertyzy (Wybrano: {n}/2)',
        skill_banner_class: 'Klasa <strong>{cls}</strong> wymaga wyboru <strong>{num}</strong> biegłości (Wybrano: {sel}/{num}).',
        skill_banner_human: ' Jako <strong>człowiek</strong> wybierasz dodatkowo <strong>1 dowolną</strong> biegłość (Wybrano: {sel}/1).',
        badge_background: 'Pochodzenie',
        badge_race: 'Rasa',
        badge_class: 'Klasa',
        badge_human: 'Człowiek',
        btn_generate: 'Wygeneruj Gotową Kartę Postaci PDF 📥',
        btn_spellbook: '📖 Wirtualna Księga Zaklęć (Otwórz generator kart)',
        valid_ok: 'Wszystkie warunki są spełnione! Karta postaci jest gotowa do pobrania.',
        valid_header: 'Wymagania do spełnienia:',
        err_points: 'Musisz wykorzystać dokładnie 27 punktów w systemie Point Buy (aktualnie pozostało: {n} pkt).',
        err_class_skills: 'Klasa wymaga wyboru {need} umiejętności (wybrano {have}).',
        err_human_skill: 'Jako człowiek musisz wybrać 1 dodatkową umiejętność.',
        err_expertise: 'Jako łotrzyk musisz wybrać dokładnie 2 umiejętności do ekspertyzy.',
        // Detail cards
        card_race: 'Rasa',
        card_class: 'Klasa',
        card_bg: 'Pochodzenie',
        card_race_traits: 'Cechy rasy',
        card_class_traits: 'Cechy klasy',
        card_bg_traits: 'Cechy pochodzenia',
        card_senses: 'Cechy i zmysły:',
        card_start_feats: 'Cechy startowe:',
        card_bg_feat: 'Zdolność pochodzenia:',
        card_speed: 'BIEG',
        card_size: 'WMR',
        card_hit_die: 'KOŚĆ HP',
        card_saves: 'RZUTY OBRONNE:',
        // Dice modal
        dice_title: '🎲 Losowanie Statystyk',
        dice_subtitle: 'Rzut 5k6 – odrzuć 2 najniższe, sumuj 3 najwyższe',
        dice_rolling: 'Losowanie...',
        dice_accept: '✅ Zaakceptuj wyniki',
        dice_reroll: '🔄 Losuj ponownie',
        dice_close: 'Anuluj',
        dice_dropped: 'odrzucone',
        // Stat mode
        mode_dice: 'Tryb losowania kośćmi',
        mode_dice_desc: 'Statystyki wylosowane kośćmi (5k6, odrzuć 2 najniższe). Zakres: 3-18.',
        btn_back_pointbuy: '↩ Powrót do Point Buy',
        // PDF note
        pdf_note: '📜 Karta postaci jest zawsze generowana w języku polskim.',
        // Stat names
        stat_str: 'Siła (STR)',
        stat_dex: 'Zręczność (DEX)',
        stat_con: 'Kondycja (CON)',
        stat_int: 'Inteligencja (INT)',
        stat_wis: 'Mądrość (WIS)',
        stat_cha: 'Charyzma (CHA)',
        // Spells translation
        section_spells: 'Zaklęcia i Magia',
        lbl_spell_ability: 'Zdolność czarowania:',
        lbl_spell_dc: 'ST Rzutu Obronnego:',
        lbl_spell_attack: 'Atak zaklęciem:',
        lbl_cantrips: 'Sztuczki (Cantrips)',
        lbl_spells_1: 'Zaklęcia 1. poziomu',
        err_cantrips: 'Klasa wymaga wyboru dokładnie {need} sztuczek (wybrano {have}).',
        err_spells1: 'Klasa wymaga wyboru dokładnie {need} zaklęć 1. poziomu (wybrano {have}).',
    },
    en: {
        page_title: 'D&D 5e Character Creator',
        page_subtitle: 'Build your hero according to the official Player\'s Handbook rules',
        section_identity: 'Who are you?',
        lbl_name: 'Character Name',
        lbl_class: 'Class',
        lbl_level: 'Level',
        lbl_race: 'Race',
        lbl_background: 'Background',
        lbl_alignment: 'Alignment',
        section_stats: 'Attributes & Statistics',
        btn_try_harder: 'Auto: Try Harder 💪',
        btn_balanced: 'Auto: Balanced ⚖️',
        btn_roll_dice: '🎲 Roll Dice',
        point_buy_title: 'Point Buy System',
        point_buy_desc: 'Base range: 8 - 15. Cost increases non-linearly (14: 7pts, 15: 9pts). You must spend <strong>exactly all 27 points</strong>!',
        pool_remaining: 'Remaining',
        pool_spent: 'All spent!',
        pool_over: 'Over budget!',
        lbl_base: 'Base',
        lbl_race_bonus: 'Race',
        lbl_total: 'Total',
        lbl_mod: 'Mod.',
        hint_key_stat: 'Key stat',
        hint_rec_stat: 'Recommended stat',
        section_skills: 'Proficiencies & Skills',
        lbl_prof_bonus: 'Proficiency Bonus:',
        lbl_initiative: 'Initiative:',
        lbl_passive_perc: 'Passive Perception:',
        lbl_ac: 'Armor Class (AC):',
        expertise_title: 'Expertise',
        expertise_info: 'As a rogue, choose <strong>2</strong> proficient skills for expertise (Chosen: {n}/2)',
        skill_banner_class: 'Class <strong>{cls}</strong> requires <strong>{num}</strong> skill proficiencies (Chosen: {sel}/{num}).',
        skill_banner_human: ' As a <strong>human</strong> you choose <strong>1 additional</strong> proficiency (Chosen: {sel}/1).',
        badge_background: 'Background',
        badge_race: 'Race',
        badge_class: 'Class',
        badge_human: 'Human',
        btn_generate: 'Generate Character Sheet PDF 📥',
        btn_spellbook: '📖 Virtual Spellbook (Open Cards Generator)',
        valid_ok: 'All requirements met! Character sheet is ready to download.',
        valid_header: 'Requirements to fulfill:',
        err_points: 'You must spend exactly 27 points in Point Buy (remaining: {n} pts).',
        err_class_skills: 'Class requires {need} skill proficiencies (chosen {have}).',
        err_human_skill: 'As a human you must choose 1 additional skill.',
        err_expertise: 'As a rogue you must choose exactly 2 skills for expertise.',
        card_race: 'Race',
        card_class: 'Class',
        card_bg: 'Background',
        card_race_traits: 'Racial traits',
        card_class_traits: 'Class features',
        card_bg_traits: 'Background traits',
        card_senses: 'Traits & senses:',
        card_start_feats: 'Starting features:',
        card_bg_feat: 'Background feature:',
        card_speed: 'SPEED',
        card_size: 'SIZE',
        card_hit_die: 'HIT DIE',
        card_saves: 'SAVING THROWS:',
        dice_title: '🎲 Rolling Statistics',
        dice_subtitle: 'Roll 5d6 – drop 2 lowest, sum 3 highest',
        dice_rolling: 'Rolling...',
        dice_accept: '✅ Accept results',
        dice_reroll: '🔄 Roll again',
        dice_close: 'Cancel',
        dice_dropped: 'dropped',
        mode_dice: 'Dice Rolling Mode',
        mode_dice_desc: 'Stats rolled with dice (5d6, drop 2 lowest). Range: 3-18.',
        btn_back_pointbuy: '↩ Back to Point Buy',
        pdf_note: '📜 The character sheet is always generated in Polish.',
        stat_str: 'Strength (STR)',
        stat_dex: 'Dexterity (DEX)',
        stat_con: 'Constitution (CON)',
        stat_int: 'Intelligence (INT)',
        stat_wis: 'Wisdom (WIS)',
        stat_cha: 'Charisma (CHA)',
        // Spells translation
        section_spells: 'Spells & Magic',
        lbl_spell_ability: 'Spellcasting Ability:',
        lbl_spell_dc: 'Spell Save DC:',
        lbl_spell_attack: 'Spell Attack Bonus:',
        lbl_cantrips: 'Cantrips (Lvl 0)',
        lbl_spells_1: '1st Level Spells',
        err_cantrips: 'Class requires exactly {need} cantrips (chosen {have}).',
        err_spells1: 'Class requires exactly {need} 1st level spells (chosen {have}).',
    }
};

let currentLang = localStorage.getItem('dnd_lang') || 'pl';

function t(key, replacements) {
    let text = (TRANSLATIONS[currentLang] && TRANSLATIONS[currentLang][key]) || (TRANSLATIONS['pl'][key]) || key;
    if (replacements) {
        for (const [k, v] of Object.entries(replacements)) {
            text = text.replaceAll(`{${k}}`, v);
        }
    }
    return text;
}

function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('dnd_lang', lang);
    document.documentElement.lang = lang;
    // Update toggle buttons
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.lang === lang);
    });
    // Update all elements with data-i18n attribute
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.dataset.i18n;
        const translated = t(key);
        if (el.dataset.i18nAttr) {
            el.setAttribute(el.dataset.i18nAttr, translated);
        } else if (el.dataset.i18nHtml) {
            el.innerHTML = translated;
        } else {
            el.textContent = translated;
        }
    });
    // Refresh dynamic UI
    if (typeof updateUI === 'function') updateUI();
}

document.addEventListener('DOMContentLoaded', () => {
    setLanguage(currentLang);
});
