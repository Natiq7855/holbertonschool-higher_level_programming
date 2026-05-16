document.addEventListener('DOMContentLoaded', () => {
    const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
    const helloElement = document.querySelector('#hello');

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (helloElement) {
                helloElement.innerHTML = data.hello;
            }
        })
        .catch(error => {
            console.error('Error fetching greeting data:', error);
        });
});