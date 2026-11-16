async function getMovies () {
  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
    if (response.ok) {
      const data = await response.json();
      console.log(data);

      const movieList = document.getElementById('list_movies');
      let listElement;
      
      for (const film of data.results) {
        listElement = document.createElement('li');
        listElement.innerHTML = film.title;
        movieList.appendChild(listElement);
      }
    } else {
      throw new Error('Failed to fetch data');
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

getMovies();
