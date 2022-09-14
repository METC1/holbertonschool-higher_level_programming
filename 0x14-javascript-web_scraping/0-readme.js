#!/usr/bin/node
// reads and prints the content of a file

const fs = require('fs');
const nameFile = process.argv[2];

fs.readFile(nameFile, 'utf8', function (error, data) {
  if (error) {
    return console.error(error);
  } else {
    console.log(data.toString());
  }
});
