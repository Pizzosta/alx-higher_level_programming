#!/usr/bin/node
/* A script that searches the second biggest integer
 * in the list of argument
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
 */

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  const integers = args.map(Number);
  const sortedIntegers = integers.sort((a, b) => b - a);
  console.log(sortedIntegers[1]);
}
