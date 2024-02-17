#!/usr/bin/node
const process = require('process');
function add (i, j) {
  return i + j;
}
console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
