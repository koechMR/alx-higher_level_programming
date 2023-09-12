#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let a = 0; a < this.height; a++) {
      let b = '';
      for (let e = 0; e < this.width; e++) {
        b += c;
      }
      console.log(b);
    }
  }
}

module.exports = Square;
