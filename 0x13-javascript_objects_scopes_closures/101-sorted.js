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

Object.keys(dict).forEach(function (key) {
  const occurrence = dict[key];
  if (newDict[occurrence] === undefined) {
    newDict[occurrence] = [];
  }
  newDict[occurrence].push(key);
});

console.log(newDict);
