#!/usr/bin/node
function factorial(n) {
    if (n === 0 || n === 1) {
        return 1;
    } else if (n < 0) {
        return "Infinity";
    } else {
        return n * factorial(n - 1);
    }
}
const args = process.argv.slice(2);
const firstArg = parseInt(args[0], 10);
if (isNaN(firstArg)) {
    console.log("1");
} else {
    console.log(factorial(firstArg));
}
