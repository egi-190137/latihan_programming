function kangaroo(x1, v1, x2, v2) {
    if (v2 >= v1) {
        return 'NO';
    } else {
        while (x2 > x1) {
            x1 += v1;
            x2 += v2;
        }

        if (x1 == x2) {
            return 'YES';
        } else {
            return 'NO';
        }
    }
}

console.log(kangaroo(0, 3, 4, 2));
console.log(kangaroo(0, 2, 5, 3));