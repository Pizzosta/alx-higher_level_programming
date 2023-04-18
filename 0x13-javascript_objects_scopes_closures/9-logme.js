#!/usr/bin/node
/* a function that prints the number of arguments already printed
 * and the new argument value.
 */

let ArgsPrinted = 0;

exports.logMe = function (item) {
  console.log(ArgsPrinted + ': ' + item);
  ArgsPrinted++;
};
