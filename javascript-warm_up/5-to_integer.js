#!/usr/bin/node

const { argv } = require('node:process');

const intArgument = parseInt(argv[2], 10);

if (Number.isNaN(intArgument)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${intArgument}`);
}
