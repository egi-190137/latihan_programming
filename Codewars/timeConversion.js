function timeConversion(s) {
    let time = s.split(/:|[A-Z]{2}/).slice(0, 3);
    const format = s.slice(-2, s.length);

    if (format === 'PM' && time[0] != '12') {
        time[0] = parseInt(time[0]) + 12;   
    } else if (format === 'AM' && time[0] == '12') {
        time[0] = '00'; 
    }

    return time.join(':');
}

console.log(timeConversion('07:05:45PM'));
console.log(timeConversion('12:40:22AM'));