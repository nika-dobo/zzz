# 10. Find the Parity Outlier
# Description:
#  Given an array of integers, where all but one are even or odd, find the outlier.
# Example Test Cases:

#! find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) → 11


#! find_outlier([160, 3, 1719, 19, 11, 13, -21]) → 160


#! find_outlier([2, 6, 8, -10, 3]) → 3


def nums(s):
    num = []
    num1 = []

    for i in range(len(s)):
        if s[i]%2 == 0:
            num.append(s[i])
        elif s[i]%2 != 0:
            num1.append(s[i])
    return num,num1
print(nums([2, 4, 0, 100, 4, 11, 2602, 36]))   
print(nums([2, 4, 0, 100, 4, 12, 2602, 26, 3, 14]))   