#!/usr/bin/node
const firstNum = Math.trunc(process.argv[2]);
const secondNum = Math.trunc(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}
add(firstNum, secondNum);
