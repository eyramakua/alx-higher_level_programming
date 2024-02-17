#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2);
  numbers.sort((i, j) => (i - j));
  console.log(numbers[numbers.length - 2]);
}
