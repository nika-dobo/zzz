// 15. Even or Odd
// Description:
//  Create a function that takes a number as an argument and returns 'Even' for even numbers or 'Odd' for odd numbers.
// Example Test Cases:

//! evenOrOdd(2) → "Even"

//! evenOrOdd(7) → "Odd"

//! evenOrOdd(0) → "Even"

function evenOrOdd(x) {
  if (x % 2 == 0 || x == 0) {
    return "Even";
  } else {
    return "Odd";
  }
}

console.log(evenOrOdd(2));
console.log(evenOrOdd(7));
console.log(evenOrOdd(0));
