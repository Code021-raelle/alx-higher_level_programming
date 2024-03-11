#!/usr/bin/node
const args = process.argv.slice (2);
const firstArg = args[0];
const size = parseInt(firstArg, 10);
if (isNaN(size) || size < 0) {
    console.log('Missing size');
} else {
    for (let i = 0; i < size; i++) {
        let line = "";
        for (let j = 0; j < size; j++) {
            line += "X";
        }
        console.log(line);
    }
}
