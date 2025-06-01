# 8. Format Phone Number
# Description:
#  Given a list of 10 integers, return a string in the form of a phone number: (123) 456-7890.
# Example Test Cases:

#! create_phone_number([1,2,3,4,5,6,7,8,9,0]) → "(123) 456-7890"


#! create_phone_number([0,0,0,0,0,0,0,0,0,0]) → "(000) 000-0000"


#! create_phone_number([9,8,7,6,5,4,3,2,1,0]) → "(987) 654-3210"


def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))
print(create_phone_number([0,0,0,0,0,0,0,0,0,0]))
print(create_phone_number([9,8,7,6,5,4,3,2,1,0]))

