#!/usr/bin/node

const { argv } = require('node:process');

function add(a, b) {
  if (Number.isNaN(parseInt(a)) || Number.isNaN(parseInt(b))) {
    return NaN;
  }
    return parseInt(a) + parseInt(b);
}

console.log(add(argv[2], argv[3]))
