const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
const name = document.querySelector("#character");

fetch(url)
    .then(respone => {
        if(!respone.ok){
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return respone.json();
    })

    .then(data => {
        if (name) {
            name.textContent = data.name;
        }
    })

    .catch(error => {
        console.error('Error fetching character data:', error);
    })
