#!/usr/bin/node

const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(err);
    return;
  }

  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(err);
      return;
    }

    const concatenatedData = data1.trim() + '\n' + data.trim();

    fs.writeFile(destinationFile, concatenatedData, (err) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(`Files ${sourceFile1} and ${sourceFile2} have been concatenated into ${destinationFile}`);
    });
  });
});
