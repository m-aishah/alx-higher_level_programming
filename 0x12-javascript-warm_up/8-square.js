#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let row = size; row > 0; row--) {
    let output = '';
    for (let col = size; col > 0; col--) {
      output += 'X';
    } console.log(output);
  }
}
