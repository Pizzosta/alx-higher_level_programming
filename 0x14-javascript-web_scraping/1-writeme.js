#!/usr/bin/node
/**
* A script that writes a string to a file
* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in utf-8
* usage: ./1-writeme.js <my_file.txt> "String"
*/

const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
