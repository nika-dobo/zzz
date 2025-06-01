# 7. Find the Odd Int
# Description:
#  Given an array of integers, find the one that appears an odd number of times.
# Example Test Cases:

#! find_odd([20, 1, 1, 2, 2, 3, 3, 20, 4, 4, 5, 5, 5]) → 5


#! find_odd([10, 10, 10]) → 10


#! find_odd([1, 2, 3, 1, 2, 3, 1]) → 1


def find_odd(arr):
    for num in arr:
        if arr.count(num) % 2 == 1:
            return num

# Example Test Cases:
print(find_odd([20, 1, 1, 2, 2, 3, 3, 20, 4, 4, 5, 5, 5]))  # 5
print(find_odd([10, 10, 10]))  # 10
print(find_odd([1, 2, 3, 1, 2, 3, 1]))  # 1