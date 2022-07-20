function sortChange(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        let terbesar = i;
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[terbesar][1] < arr[j][1]) {
                terbesar = j;
            }
        }
        [arr[i], arr[terbesar]] = [arr[terbesar], arr[i]];
    }
    return arr;
}

function arraysEqual(x, y) {
    var pre = ['string' , 'number' , 'bool']
    if(typeof x!== typeof y )return pre.indexOf(typeof y) - pre.indexOf(typeof x);

    if(x === y)return 0;
    else return (x > y)?1:-1;
}

function checkCashRegister(price, cash, cid) {
    let kembalian = Math.round((cash - price) * 100) / 100;
    let change = [];
    const temp = [...cid];
    // console.log(realCid);
    const pecahan = {
        "TWENTY":20,
        "TEN":10,
        "FIVE":5,
        "ONE":1,
        "QUARTER":0.25,
        "DIME":0.1,
        "NICKEL":0.05,
        "PENNY":0.01,
    };
    // const keyPecahan = Object.keys(pecahan); 
    for (let i = temp.length-1; i >= 0; i--) {
        kembalian = Math.round(kembalian * 100) / 100
        if (kembalian >= pecahan[temp[i][0]]) {
            if (kembalian < temp[i][1]) {
                const jumlahLembar = Math.floor(kembalian / pecahan[temp[i][0]]);
                const total = jumlahLembar * pecahan[temp[i][0]];
                
                temp[i][1] -= total;
                kembalian -= total;

                change.push([temp[i][0], total]);
            } else {
                kembalian -= temp[i][1];
                change.push([temp[i][0], temp[i][1]]);
                temp[i][1] = 0;

            }
        }
    }
    console.log(cid);

    if (kembalian > 0) {
        return {status: "INSUFFICIENT_FUNDS", change: []};
    }

    change = sortChange(change);    
    if (arraysEqual(temp.filter(item => item[1] === 0), temp)) {
        return {status: "CLOSED", change: cid};
    } else {
        return {status: "OPEN", change: change};
    }
}

console.log(checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));

// {status: "CLOSED", change: [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]}

console.log(checkCashRegister(3.26, 100, [
    ["PENNY", 1.01],
    ["NICKEL", 2.05],
    ["DIME", 3.1],
    ["QUARTER", 4.25],
    ["ONE", 90],
    ["FIVE", 55],
    ["TEN", 20],
    ["TWENTY", 60],
    ["ONE HUNDRED", 100]
]));
// {status: "OPEN", change: [["TWENTY", 60], ["TEN", 20], ["FIVE", 15], ["ONE", 1], ["QUARTER", 0.5], ["DIME", 0.2], ["PENNY", 0.04]]}

console.log(checkCashRegister(19.5, 20, [
    ["PENNY", 1.01],
    ["NICKEL", 2.05],
    ["DIME", 3.1],
    ["QUARTER", 4.25],
    ["ONE", 90],
    ["FIVE", 55],
    ["TEN", 20],
    ["TWENTY", 60],
    ["ONE HUNDRED", 100]
]));
// {status: "OPEN", change:[["QUARTER", 0.5]]}


console.log(checkCashRegister(19.5, 20, [
    ["PENNY", 0.01],
    ["NICKEL", 0],
    ["DIME", 0],
    ["QUARTER", 0],
    ["ONE", 0],
    ["FIVE", 0],
    ["TEN", 0],
    ["TWENTY", 0],
    ["ONE HUNDRED", 0]
]));
// {status: "INSUFFICIENT_FUNDS", change: []}

console.log(checkCashRegister(19.5, 20, [
    ["PENNY", 0.01],
    ["NICKEL", 0],
    ["DIME", 0],
    ["QUARTER", 0],
    ["ONE", 1],
    ["FIVE", 0],
    ["TEN", 0],
    ["TWENTY", 0],
    ["ONE HUNDRED", 0]
]));
// {status: "INSUFFICIENT_FUNDS", change: []}

console.log(checkCashRegister(19.5, 20, [
    ["PENNY", 0.5],
    ["NICKEL", 0],
    ["DIME", 0],
    ["QUARTER", 0],
    ["ONE", 0],
    ["FIVE", 0],
    ["TEN", 0],
    ["TWENTY", 0],
    ["ONE HUNDRED", 0]
]));
// {status: "CLOSED", change: [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]}