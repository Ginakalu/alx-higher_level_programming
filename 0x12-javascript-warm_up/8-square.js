#!/usr/bin/node
const size = Math.trunc(process.argv[2]);

if (isNaN(size)) console.log('Missing size');

for (let i = 0; i < size; i++) {
  const temp = [];
  for (let j = 0; j < size; j++) temp.push('X');
  console.log(temp.join(''));
}
