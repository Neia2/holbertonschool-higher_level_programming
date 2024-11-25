fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((response) => response.json())
  .then((data) => {
    console.log('Character data:', data);
    document.getElementById('character').textContent = data.name;
  })
  .catch((error) => console.error('Fetch error:', error));
