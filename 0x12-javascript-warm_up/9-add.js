#!/usr/bin/node
function add(a, b) {
    return a + b;
}
const args = process.argv.slice(2);
const firstArg = parseInt(args[0], 10);
const secondArg = parseInt(args[1], 10);
if (isNaN(firstArg) || isNaN(secondArg)) {
    console.log("NaN");
} else {
    console.log(add(firstArg, secondArg));
}
