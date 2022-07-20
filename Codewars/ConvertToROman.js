// const Math = include('Math');
// import 'Math';

function convertToRoman(num) {
  const roman = {
    'M':1000,
    'CM':900,
    'D':500,
    'CD':400,
    'C':100,
    'XC':90,
    'L':50,
    'XL':40,
    'X':10,
    'IX':9,
    'V':5,
    'IV':4,
    'I':1,
  };
  const romanKey = Object.keys(roman);
  let result = '';
  let idx = 0;
  while (num > 0) {
    const hasilBagi = Math.floor(num / roman[romanKey[idx]]);
    for (let i = 0; i < hasilBagi; i++) {
      result += romanKey[idx];
    }
    // console.log(romanKey[idx]);
    num %= roman[romanKey[idx]];
    idx++;
  }
  // for (let i = 0; i < romanKey.length; i++) {
  //   // console.log(romanKey[i]);
  //   const hasilBagi = num / roman[romanKey[i]];
  //   // console.log(hasilBagi);
  //   if (hasilBagi === 4) {
  //     result += `${romanKey[i]}${romanKey[i-1]}`;
  //   } else if (Math.floor(hasilBagi) > 0) {
  //     for (let j = 0; j < Math.floor(hasilBagi); j++) {
  //       result += `${romanKey[i]}`;
  //     }
  //     if ( (Math.ceil(hasilBagi) * roman[romanKey[i]]) % num == roman[romanKey[i+2]]) {
  //       result += `${romanKey[i+2]}${romanKey[i]}`;
  //       num = 0;
  //     }
  //   } else if (Math.floor(hasilBagi) == 0) {
  //     if ( (Math.ceil(hasilBagi) * roman[romanKey[i]]) - num == roman[romanKey[i+2]]) {
  //       result += `${romanKey[i+2]}${romanKey[i]}`;
  //       num = 0;
  //     }
  //   }
  //   num = num % roman[romanKey[i]]; 
  // }45console.log(convertToRoman(45) should return the string XCIX

  return result;
}

console.log(convertToRoman(2)); // should return the string II.
console.log(convertToRoman(3)); // should return the string III.
console.log(convertToRoman(4)); // should return the string IV.
console.log(convertToRoman(5)); // should return the string V.
console.log(convertToRoman(9)); // should return the string IX.
console.log(convertToRoman(12)); // should return the string XII.
console.log(convertToRoman(16)); // should return the string XVI.
console.log(convertToRoman(29)); // should return the string XXIX.
console.log(convertToRoman(44)); // should return the string XLIV.
console.log(convertToRoman(45)); // should return the string XLV.
console.log(convertToRoman(68)); // should return the string LXVIII
console.log(convertToRoman(83)); // should return the string LXXXIII
console.log(convertToRoman(97)); // should return the string XCVII
console.log(convertToRoman(99)); // should return the string XCIX
console.log(convertToRoman(400)); // should return the string CD
console.log(convertToRoman(500)); // should return the string D
console.log(convertToRoman(501)); // should return the string DI
console.log(convertToRoman(649)); // should return the string DCXLIX
console.log(convertToRoman(798)); // should return the string DCCXCVIII
console.log(convertToRoman(891)); // should return the string DCCCXCI
console.log(convertToRoman(1004)); // should return the string MIV
console.log(convertToRoman(1006)); // should return the string MVI
console.log(convertToRoman(1023)); // should return the string MXXIII
console.log(convertToRoman(2014)); // should return the string MMXIV
console.log(convertToRoman(3999)); // should return the string MMMCMXCIX