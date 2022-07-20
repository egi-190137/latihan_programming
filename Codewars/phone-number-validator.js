function telephoneCheck(str) {
    return /(^\d{3}-\d{3}-\d{4}$|^\(\d{3}\)(| )\d{3}-\d{4}$|^\d{3} \d{3} \d{4}$|^\d{10}$|^1 \d{3} \d{3} \d{4}$|^1 \d{3}-\d{3}-\d{4}$|^1 \(\d{3}\) \d{3}-\d{4}$|^1\(\d{3}\)\d{3}-\d{4}$)/.test(str);
}
  
console.log(telephoneCheck("1 (555) 555-5555"));

console.log(telephoneCheck("(555)555-5555"));
console.log(telephoneCheck("555-555-5555"));
console.log(telephoneCheck("(555)555-5555"));
console.log(telephoneCheck("(555) 555-5555"));

console.log(telephoneCheck("1 555-555-5555"));
console.log(telephoneCheck("1 (555) 555-5555"));
console.log(telephoneCheck("5555555555"));
console.log(telephoneCheck("555-555-5555"));
console.log(telephoneCheck("1(555)555-5555"));
console.log(telephoneCheck("555-5555"));
console.log(telephoneCheck("5555555"));
console.log(telephoneCheck("1 555)555-5555"));
console.log(telephoneCheck("1 555 555 5555"));
console.log(telephoneCheck("1 456 789 4444"));
console.log(telephoneCheck("123**&!!asdf#"));