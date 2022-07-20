function shortPalindrome(s) {
    let count = 0;
    for (let a = 0; a < s.length - 3; a++) {
        for (let b = a + 1; b < s.length - 2; b++) {
            for (let c = b + 1; c < s.length - 1; c++) {
                for (let d = c + 1; d < s.length; d++) {
                    if (s[a] == s[d] && s[b] == s[c]) {
                        count++;
                    } 
                }
            }
        }
    }
    return count
}

console.log(shortPalindrome('ghhggh'))
console.log(shortPalindrome('kkkkkkz'))
