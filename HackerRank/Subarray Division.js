function birthday(s, d, m) {
    let count = 0;    
    for (let i = 0; i < s.length - m + 1; i++) {
        if ( s.slice(i, m + i).reduce((a, b) => a + b) === d) {
            count++;
        }
    }
    return count;
}

console.log(birthday([1, 2, 1, 3, 2], 3, 2));
console.log(birthday([1, 1, 1, 1, 1, 1], 3, 2));
console.log(birthday([4], 4, 1));
