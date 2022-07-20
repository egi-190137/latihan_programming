function birthdayCakeCandles(candles) {
    candles.sort( (a, b) => b - a );

    let count = 1;
    for (let i = 1; i < candles.length; i++) {
        if (candles[i] == candles[0]) {
            count++;
        }
    }
    return count;
}
console.log(birthdayCakeCandles([3, 2, 1, 3]));
