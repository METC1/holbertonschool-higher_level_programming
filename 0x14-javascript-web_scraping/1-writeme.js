#!/usr/bin/node
//writes a string to a file

const fs = require('fs');
const nameFile = process.argv[2];
const str = process.argv[3];

fs.writeFile(nameFile, str, 'utf8', function(error, data){
  if (error) {
    return console.error(error);
  }
});
