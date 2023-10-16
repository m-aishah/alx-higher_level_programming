#!/usr/bin/node
const myNumber = Math.floor(Number(process.argv[2]));
console.log(isNaN(myNumber) ? 'Not a number' : `My number: ${myNumber}`);
