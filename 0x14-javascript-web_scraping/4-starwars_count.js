#!/usr/bin/node
/**
* The first argument is the API URL of the
* Star wars API: https://swapi-api.alx-tools.com/api/films/
* Wedge Antilles is character ID 18 -
* your script must use this ID for filtering the result of the API
* usage: ./4-starwars_count.js <starWarsUri>
*/

const request = require('request');
const starWarsUri = process.argv[2];
let nFilms = 0;

request(starWarsUri, function (err, response, body) {
  if (err == null) {
    const resp = JSON.parse(body);
    const results = resp.results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          nFilms++;
        }
      }
    }
  }
  console.log(nFilms);
});
