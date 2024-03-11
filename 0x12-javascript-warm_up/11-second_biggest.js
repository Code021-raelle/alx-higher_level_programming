#!/usr/bin/node
const args = process.argv.slice(2).map(number);
if (args.length <= 1) {
    console.log("0");
} else {
    args.sort((a, b) => b - a);
    console.log(args[1]);
}
