#!/usr/bin/node
/* a script that prints My number: <first argument converted in integer>
 *  if the first argument can be converted to an integer
 *  If the argument can’t be converted to an integer, print “Not a number”
 */

if (parseInt(process.argv[2])) {
  console.log('My number: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
