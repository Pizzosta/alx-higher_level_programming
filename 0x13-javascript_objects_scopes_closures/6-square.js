#!/usr/bin/node
/* a class Square that defines a square and inherits from Square of 5-square.js
 * Create an instance method called charPrint(c)
 * that prints the rectangle using the character c
 * If c is undefined, use the character X
 */

const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
