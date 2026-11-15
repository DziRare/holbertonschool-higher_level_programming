#!/usr/bin/node

const { argv } = require('node:process');

let statement;
statement = argv.length <= 2 ? 'No argument' : 'Argument found';
console.log(statement);
