#!/usr/bin/node
const args = process.argv;
const myNumber = parseInt(args[2]);

if (isNaN(myNumber)) {
  console.log('Not a number');
} else {
  console.log('My number: ', myNumber);
}
