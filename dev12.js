//String Repeat
// Description:
//  Write a function that repeats a given string n times.
// Example Test Cases:

//! repeatStr(3, "abc") → "abcabcabc"

//! repeatStr(5, "") → "**"

//!  repeatStr(0, "#") → ""

function repeatStr(n, str) {
  return str.repeat(n);
}

console.log(repeatStr(3, "abc"));
console.log(repeatStr(5, ""));
console.log(repeatStr(0, "#"));
