#!/usr/bin/node

const { argv } = require('node:process');

const size = parseInt(argv[2], 10);

if (Number.isNaN(size)) {
  console.log('Missing size');
}

for (let i = 0; i < size; i++) {
  console.log('X'.repeat(size));
}
