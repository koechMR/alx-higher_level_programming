#!/usr/bin/node
function secondBiggest (args) {
  if (args.length <= 1) {
    console.log(0);
  } else {
    args = args.map(Number).filter(Number.isInteger);
    if (args.length <= 1) {
      console.log(0);
    } else {
      args.sort((a, b) => b - a);
      console.log(args[1]);
    }
  }
}
const args = process.argv.slice(2);
secondBiggest(args);
