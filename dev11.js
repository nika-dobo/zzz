// 11. Return Negative
// Description:
//  Given a number, return it as a negative value. If it's already negative, return it as is. Zero should remain zero.
// Example Test Cases:

//! makeNegative(1) → -1


//! makeNegative(-5) → -5


//! makeNegative(0) → 0


function makeNegative(x){
    if (x > 0){
        return x * -1
    }
    else if (x <= 0){
        return x
    }
}

console.log(makeNegative(1))
console.log(makeNegative(-5))
console.log(makeNegative(0))