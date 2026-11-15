#!/usr/bin/node

const { argv } = require('node:process');

let statement;

if (argv.length <= 2) {
  statement = 'No argument';
} else if (argv.length === 3) {
  statement = 'Argument found';
} else {
  statement = 'Arguments found';
}

console.log(statement);
