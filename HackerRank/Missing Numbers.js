function missingNumbers(arr, brr) {
    let result = [];
    for (let i = 0; i < brr.length; i++) {
        if (result.indexOf(brr[i]) < 0) {
            if (brr.filter(item => item == brr[i]).length > arr.filter(item => item == brr[i]).length) {
                result.push(brr[i]);
            }
        }
    }

    return result.sort();
}

console.log(missingNumbers([203, 204, 205, 206, 207, 208, 203, 204, 205, 206], [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]))