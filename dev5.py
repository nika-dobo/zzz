# 5. Count by X
# Description:
#  Create a function that returns a list of the first n multiples of x.
# Example Test Cases:

#! count_by(1, 5) → [1, 2, 3, 4, 5]


#! count_by(2, 5) → [2, 4, 6, 8, 10]


#! count_by(3, 4) → [3, 6, 9, 12]

def count_by(x,y):
    arr = []
    for i in range(x,y*x +1,x):
        arr.append(i)
    return arr

print(count_by(1, 5))
print(count_by(2, 5))
print(count_by(3, 4))