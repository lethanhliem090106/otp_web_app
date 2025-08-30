document.addEventListener('DOMContentLoaded', () => {
    const modeSelect = document.getElementById('mode');
    const counterField = document.getElementById('counter-field');

    modeSelect.addEventListener('change', () => {
        counterField.style.display = modeSelect.value === 'HOTP' ? 'block' : 'none';
    });
});