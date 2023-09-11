#!/usr/bin/node
const num = parseInt(process.argv[2]);

if (!isNaN(num) && num > 0) {
  for (let f = 0; f < num; f++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
