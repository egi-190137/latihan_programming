function countApplesAndOranges(s, t, a, b, apples, oranges) {
    apples = apples.map(item => a +item);
    oranges = oranges.map(item => b +item);

    console.log(apples.filter( item => (item >= s && item <= t) ).length);
    console.log(oranges.filter( item => (item >= s && item <= t) ).length)
}

countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6]);