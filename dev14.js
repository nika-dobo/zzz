// 14. Opposite Number
// Description:
//  Very simple — given a number, return its opposite.
// Example Test Cases:

//! opposite(1) → -1


//! opposite(-10) → 10


//! opposite(0) → 0

function opposite(x){
      if (x < 0){
        return x * -1
    }
    else if (x => 0){
        return x
    }
}


console.log(opposite(1))
console.log(opposite(-10))
console.log(opposite(0))