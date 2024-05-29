#!/usr/bin/node

const number = parseInt(process.argv[2]);

if (number) {
  for (let i = 0; i < process.argv[2]; i++) {
    let line = '';
    for (let i = 0; i < process.argv[2]; i++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
