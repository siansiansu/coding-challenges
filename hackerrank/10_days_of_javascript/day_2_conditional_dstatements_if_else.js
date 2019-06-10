'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function getGrade(score) {
    let grade;
    // Write your code here
    if (score <= 5) {
        return 'F';
    } else if (score <= 10) {
        return 'E';
    } else if (score <= 15) {
        return 'D';
    } else if (score <= 20) {
        return 'C';
    } else if (score <= 25) {
        return 'B';
    } else
        return 'A';

    return grade;
}


function main() {
    const score = +(readLine());

    console.log(getGrade(score));
}