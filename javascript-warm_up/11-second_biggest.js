#!/usr/bin/node

const { argv } = require('node:process');

const numberArray = argv.slice(2);
numberArray.sort((a, b) => b - a);

if (numberArray.length <= 1) {
  console.log(0);
} else {
  console.log(numberArray[1]);
}
