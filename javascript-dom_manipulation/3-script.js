const header = document.querySelector('header');
const redHeaderButton = document.querySelector('#toggle_header');

if (toggleButton && header) {
    toggleButton.addEventListener('click', () => {
        if (header.classList.contains('green')){
            header.classList.remove('green');
            header.classList.add('red');
        } else{
            header.classList.remove('red')
            header.classList.add('green')
        }
    })
} else{
    console.warn("wrong")
}