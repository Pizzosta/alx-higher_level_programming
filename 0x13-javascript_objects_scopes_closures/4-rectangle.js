#!/usr/bin/node
/* a class Rectangle that defines a rectangle
 * Create an instance method called print()
 * that prints the rectangle using the character X
 * Create an instance method called rotate()
 * that exchanges the width and the height of the rectangle
 * Create an instance method called double() that multiples
 * the width and the height of the rectangle by 2
 */

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
