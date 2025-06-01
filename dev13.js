// 13. Convert Boolean Values to Strings 'Yes' or 'No'
// Description:
//  Complete a function that returns 'Yes' for true and 'No' for false.
// Example Test Cases:

//! boolToWord(true) → "Yes"

//! boolToWord(false) → "No"

//! boolToWord(!!0) → "No"

function boolToWord(bool) {
  if (bool == true) {
    return "Yes";
  } else {
    return "No";
  }
}

console.log(boolToWord(true));
console.log(boolToWord(false));
console.log(boolToWord(!!0));
