#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.log('Please provide a Movie ID as an argument');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve movie with ID ${movieId}`);
    return;
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  // Function to fetch and display character names in order
  const fetchCharacterNames = (urls, index = 0) => {
    if (index >= urls.length) return;

    request(urls[index], (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);

      // Call next character
      fetchCharacterNames(urls, index + 1);
    });
  };

  fetchCharacterNames(characterUrls);
});
