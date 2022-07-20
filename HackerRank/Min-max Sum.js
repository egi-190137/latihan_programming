function miniMaxSum(arr) {
    arr.sort( (a, b) => a - b );

    console.log(`${arr.slice(0, 4).reduce( (total, item) => total + item)} ${arr.slice(arr.length-4, arr.length).reduce( (total, item) => total + item)}`)
}
let a = null;
if (!a) {
    console.log('yes');
} else {
    console.log('no');
}
miniMaxSum([5, 2, 3, 4, 5]);