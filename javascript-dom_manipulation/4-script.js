const addItemButton = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

if (addItemButton && list) {
    addItemButton.addEventListener('click', () => {
        const newItem = document.createElement('li');
        newItem.textContent = 'Item';
        list.appendChild(newItem);
    });
} else {
    console.warn('Required elements were not found in the DOM.');
}