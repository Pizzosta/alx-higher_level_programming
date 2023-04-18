#!/usr/bin/node
/* a script that imports an array and computes a new array
 * Your script must import list from the file 100-data.js
 */

const list = require('./100-data.js').list;
const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
