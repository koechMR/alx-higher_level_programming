#!/usr/bin/node
let name = 0;

exports.logMe = function (item) {
  console.log(name + ': ' + item);
  name++;
};
