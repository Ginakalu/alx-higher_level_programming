#!/usr/bin/node
const argv = process.argv;

const arrNum = argv.filter((cur) => !isNaN(cur)).map((cur) => parseInt(cur));
if (!arrNum[0] || arrNum.length === 1) console.log(0);
else {
  const secondBiggest = arrNum.sort((a, b) => a - b);
  console.log(secondBiggest[secondBiggest.length - 2]);
}
