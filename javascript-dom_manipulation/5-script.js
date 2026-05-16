const header = document.querySelector("header");
const new_header = document.querySelector("#update_header");

if (header && new_header){
    new_header.addEventListener('click', () => {
        header.textContent = "New Header!!!";
    })
} else{
    console.warn("wrong")
}