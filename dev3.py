# 3. Isogram Checker
# Description:
#  An isogram is a word with no repeating letters. Write a function to check if a string is an isogram (case insensitive).
# Example Test Cases:

#! is_isogram("machine") → True


#! is_isogram("letter") → False


#! is_isogram("") → True

def isogram(email):
    count=0
    for i in email:
        if email=="":
            return True
        elif email.count(i) >= 2:
            count+= 1
    if count>1:
        return False
    else:
        return True
    
print(isogram("machine"))
