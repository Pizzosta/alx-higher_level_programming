#!/usr/bin/node
/* A script that prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 * You have to define a function with this prototype: function add(a, b)
 */

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

add(process.argv[2], process.argv[3]);
