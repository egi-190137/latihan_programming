function compareTriplets(a, b) {
    let points = [0, 0];
    for (let i = 0; i < a.length; i++) {
        if ( a[i] > b[i] ) {
            points[0]++;
        } else if ( a[i] < b[i] ) {
            points[1]++;
        }
    }
    return points;
}

console.log(compareTriplets([5, 6, 7], [3, 6, 10]));
console.log(compareTriplets([17, 28, 30], [99, 16, 8]));