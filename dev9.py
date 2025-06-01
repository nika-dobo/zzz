# Counting Duplicates
# Description:
#  Count the number of distinct case-insensitive characters that occur more than once in a string.
# Example Test Cases:

#! duplicate_count("abcde") → 0

#! duplicate_count("aabbcde") → 2

#! duplicate_count("aA11") → 2


def duplicate_count(arr):
    arr=arr.lower()
    for char in arr:
        if arr.count(char) >= 2 :
            return arr.count(char)
        if arr.count(char) <= 2:
            return 0 


print(duplicate_count("abcde"))
print(duplicate_count("aabbcde"))
print(duplicate_count("aA11"))