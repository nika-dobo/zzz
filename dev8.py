# 8. Format Phone Number
# Description:
#  Given a list of 10 integers, return a string in the form of a phone number: (123) 456-7890.
# Example Test Cases:

#! create_phone_number([1,2,3,4,5,6,7,8,9,0]) → "(123) 456-7890"


#! create_phone_number([0,0,0,0,0,0,0,0,0,0]) → "(000) 000-0000"


#! create_phone_number([9,8,7,6,5,4,3,2,1,0]) → "(987) 654-3210"


def find_odd(arr):
    for num in arr:
        if arr.count(num) % 2 == 1:
            return num

# Example Test Cases:
print(find_odd([20, 1, 1, 2, 2, 3, 3, 20, 4, 4, 5, 5, 5]))  # 5
print(find_odd([10, 10, 10]))  # 10
print(find_odd([1, 2, 3, 1, 2, 3, 1]))  # 1