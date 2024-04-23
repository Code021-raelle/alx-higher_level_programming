#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
	if (error) {
		console.error(error);
		return;
	}

	if (response.statusCode !== 200) {
		console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
		return;
	}

	const movieData = JSON.parse(body);
	const charactersUrls = movieData.characters;

	charactersUrls.forEach(characterUrl => {
		request(characterUrl, (error, response, body) => {
			if (error) {
				console.error(error);
				return;
			}

			if (response.statusCode !== 200) {
				console.error(`Failed to fetch character data. Status code: ${response.statusCode}`);
				return;
			}

			const characterData = JOSN.parse(body);
			console.log(characterData.name);
		});
	});
});
