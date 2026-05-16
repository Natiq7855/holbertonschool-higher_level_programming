const url = "https://swapi-api.hbtn.io/api/films/?format=json";
const list = document.querySelector("#list_movies");

fetch(url)
    .then(response => {
        if(!response.ok){
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })

    .then(data => {
        if(list){
            const movies = data.results;

            movies.forEach(movie => {
                const listItem = document.createElement('li');
                listItem.textContent = movie.title;
                list.appendChild(listItem);
            })
        }
    })

    .catch(error => {
        console.error('Error fetching character data:', error);
    })