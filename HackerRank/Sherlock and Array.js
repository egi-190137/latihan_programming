function balancedSums(arr) {
    let sumLeft = 0;
    let sumRight = 0;

    for (let i = 1; i < arr.length; i++) {
        sumRight += arr[i] 
    }
    if (sumRight == sumLeft) {
        return 'YES';
    }
    for (let i = 1; i < arr.length; i++) {
        sumLeft += arr[i-1];
        sumRight -= arr[i];

        if (sumRight == sumLeft) {
            return 'YES';
        }
    }    
    return 'NO';
}

console.log(balancedSums([1, 1, 4, 1, 1]));
console.log(balancedSums([2, 0, 0, 0]));
console.log(balancedSums([0, 0, 2, 0]));