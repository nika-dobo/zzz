# 4. Remove Vowels
# Description:
#  Write a function that removes all vowels from a given string. Only lowercase and uppercase English vowels are considered.
# Example Test Cases:

#! remove_vowels("hello") → "hll"


#! remove_vowels("aeiou") → ""


#! remove_vowels("python") → "pythn"


def remove_vowels(str):
    vowels = "aeiouAEIOU"
    x = ""
    for char in str:
        if char not in vowels:
            x += char
    return x

print(remove_vowels("hello"))
print(remove_vowels("aeiou"))  
print(remove_vowels("python"))
