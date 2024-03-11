#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = args[0];
const number = parseInt(firstArg, 10);
if (isNaN(number) || number < 0) {
    console.log('Missing number of occurences');
} else {
    for (let i = 0; i < number; i++) {
        console.log('C is fun');
    }
}
