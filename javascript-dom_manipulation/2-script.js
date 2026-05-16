const header = document.querySelector('header');
const redHeaderButton = document.querySelector('#red_header');

if (redHeaderButton && header) {
    redHeaderButton.addEventListener('click', () => {
        header.classList.add('red');
    });
} else {
    console.warn('Required DOM elements were not found.');
}