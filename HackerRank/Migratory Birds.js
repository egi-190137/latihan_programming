function migratoryBirds(arr) {
    let types = {};
    for (let i = 0; i < arr.length; i++) {
        if ( types.hasOwnProperty(arr[i]) ) {
            types[ arr[i] ]++;
        } else {
            types[ arr[i] ] = 1;
        }
    }

    // console.log(types);

    let result = Object.keys(types)[0];
    for (let key in types) {
        if ( types[result] < types[key] || types[result] == types[key] && parseInt(result) > parseInt(key)) {
            result = key;
        }
    }

    return result;
}

console.log(migratoryBirds( [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4] ));
console.log(migratoryBirds( [1, 4, 4, 4, 5, 3] ));