function breakingRecords(scores) {
    let lowest = scores[0];
    let highest = scores[0];
    let result = [0, 0];
    console.log(scores);
    for (let i = 1; i < scores.length; i++) {
        if (scores[i] < lowest) {
            lowest = scores[i];
            result[1] += 1;
        } else if (scores[i] > highest) {
            highest = scores[i];
            result[0] += 1;
        }
    }
    return result;
}

console.log(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]));