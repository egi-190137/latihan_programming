function addZeroBeforeNum(number, length) {
    let result = number.toString();
    while (result.length < length) {
        result = '0' + result;
    }
    return result;
}

function dayOfProgrammer(year) {
    let months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    if (year >= 1700 && year <= 1917) {
        if (year % 4 == 0) {
            months[1] = 29;
        }
    } else if (year == 1918) {
        months[1] = 14;
    } else if (year >= 1919) {
        if (year % 400 == 0 || ( (year % 4 == 0) && (year % 100 > 0) ) ) {
            months[1] = 29;
        }
    }

    let idxMonth = 0;
    let date = 256;
    while (date > months[idxMonth]) {
        date -= months[idxMonth];
        idxMonth++; 
    }
    return `${addZeroBeforeNum(date, 2)}.${addZeroBeforeNum(idxMonth+1, 2)}.${year}`;
}
// console.log(addZeroBeforeNum(2, 2));
// console.log(dayOfProgrammer(2017));
// console.log(dayOfProgrammer(2016));
console.log(dayOfProgrammer(2700));

// toString