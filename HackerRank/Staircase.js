function staircase(n) {
    let result = '';
    for (let i = 0; i < n; i++) {
        result = '';
        for (let j = 0; j < n - i - 1; j++) {
            result += ' ';
        }

        for (let j = 0; j < i+1; j++) {
            result += '#';
        }
        console.log(result)
    }
}

staircase(6);