#!/usr/bin/node
add(Number(process.argv[2]), Number(process.argv[3]));
function add (a, b) {
  const c = a + b;
  console.log(c);
}
