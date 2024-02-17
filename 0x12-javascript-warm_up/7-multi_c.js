#!/usr/bin/node
const process = require('process');
const num = parseInt(process.argv[2]);
let j = 0;
if (num) {
  while (j < num) {
    console.log('C is fun');
    j++;
  }
} else {
  console.log('Missing number occurrences');
}
