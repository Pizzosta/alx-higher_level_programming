#!/usr/bin/node
/* A script that prints x times “C is fun”
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer,
 * print “Missing number of occurrences”
 */

const x = process.argv[2];

if (parseInt(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
