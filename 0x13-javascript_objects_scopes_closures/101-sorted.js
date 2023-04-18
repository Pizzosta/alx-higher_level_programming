#!/usr/bin/node
/* a script that imports a dictionary of occurrences by user id and
 * computes a dictionary of user ids by occurrence
 * Your script must import dict from the file 101-data.js
 * In the new dictionary:
 * A key is a number of occurrences
 * A value is the list of user ids
 * Print the new dictionary at the end
 */

const dict = require('./101-data').dict;
const newDict = {};

Object.keys(dict).map(function (key, index) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
  return null;
});

console.log(newDict);
