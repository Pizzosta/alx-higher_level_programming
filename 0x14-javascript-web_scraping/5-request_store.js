#!/usr/bin/node
/**
* The first argument is the URL to request
* The second argument the file path to store the body response
* usage: ./3-starwars_title.js <ID>
*/

const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
