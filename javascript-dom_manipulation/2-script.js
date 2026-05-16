// Select the header element and the tag with the ID 'red_header'
const header = document.querySelector('header');
const redHeaderButton = document.querySelector('#red_header');

// Ensure both elements exist before adding the event listener
if (redHeaderButton && header) {
    redHeaderButton.addEventListener('click', () => {
        header.classList.add('red');
    });
} else {
    console.warn('Required DOM elements were not found.');
}