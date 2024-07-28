fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const listMovies = document.getElementById('list_movies');
    data.results.forEach(film => {
      const listItem = document.createElement('li');
      listItem.textContent = film.title;
      listMovies.appendChild(listItem);
    });
  });
