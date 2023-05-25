#!/usr/bin/node
/**
* The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
* Only print users with completed task
* usage: ./6-completed_tasks.js <URL>
*/

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err == null) {
    const resp = {};
    const json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      if (json[i].completed === true) {
        if (resp[json[i].userId] === undefined) {
          resp[json[i].userId] = 0;
        }
        resp[json[i].userId]++;
      }
    }
    console.log(resp);
  }
});
