#!/usr/bin/node

const { argv } = require('node:process');

function factorial (integer) {
  if (integer === 1) {
    return 1;
  }

  if (Number.isNaN(integer)) {
    return 1;
  }

  return integer * factorial(integer - 1);
}

console.log(factorial(parseInt(argv[2])));
