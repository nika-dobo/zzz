# 2. Convert String to Camel Case
# Description:
#  Convert a string with hyphens or underscores to camel case. The first word should retain its case.
# Example Test Cases:

#! to_camel_case("the_stealth_warrior") → "theStealthWarrior"


#! to_camel_case("The-Stealth-Warrior") → "TheStealthWarrior"


#! to_camel_case("") → ""


def to_camel_case(text):
    if not text:
        return text
    words = text.replace('-', ' ').replace('_', ' ').split()
    return words[0] + ''.join(word.capitalize() for word in words[1:])

print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case(""))