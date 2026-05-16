const header = document.querySelector("header");
const button = document.querySelector("#red_header");

if (button && header){
    button.addEventListener('click', () => {
        header.style.color = '#FF0000';
    })
} else{
    console.warn("something worng")
}