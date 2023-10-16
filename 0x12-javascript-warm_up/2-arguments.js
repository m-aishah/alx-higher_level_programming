#!/usr/bin/node
const argsLength = process.argv.length;
let outputString;

if (argsLength === 2) {
  outputString = 'No argument';
} else if (argsLength === 3) {
  outputString = 'Argument found';
} else {
  outputString = 'Arguments found';
}

console.log(outputString);
