#!/usr/bin/node
/* A script that prints a message depending of the number of 
 * arguments passed
 * If no arguments are passed to the script, print “No argument”
 * If no arguments are passed to the script, print “No argument”
 * Otherwise, print “Arguments found”
 */

if (process.argv.length <= 2) {
	console.log('No argument');
} else if (process.argv.length === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
