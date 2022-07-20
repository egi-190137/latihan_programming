function plusMinus(arr) {
    const positive = arr.filter(item => item > 0).length / arr.length;
    const negative = arr.filter(item => item < 0).length / arr.length;
    const zero = arr.filter(item => item == 0).length / arr.length;
    console.log(positive.toFixed(6)); 
    console.log(negative.toFixed(6));
    console.log(zero.toFixed(6));
}

plusMinus([-4, 3, -9, 0, 4, 1]);