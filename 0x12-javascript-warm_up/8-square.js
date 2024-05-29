#!/usr/bin/node

const number = parseInt(process.argv[2]);
let square = '';

if (number) {
  for (let i = 0; i < process.argv[2]; i++) {
    for (let i = 0; i < process.argv[2]; i++) {
      square += 'X';
    }
    square += '\n';
  }
  console.log(square);
} else {
  console.log('Missing size');
}
