# 1. Sum of Odd Numbers
# Description:
# You are given an array of integers. Return the sum of only the odd numbers.
# Example Test Cases:

#! sum_odds([1, 2, 3, 4, 5]) → 9


#! sum_odds([2, 4, 6, 8]) → 0


#! sum_odds([11, 21, 32, 43]) → 75



def sum_odds(arr):
    sum = 0
    for i in arr:
        if i % 2 != 0:
            sum += i
    return sum


print(sum_odds([1, 2, 3, 4, 5]))
print(sum_odds([2, 4, 6, 8]))
print(sum_odds([11, 21, 32, 43]))