# 6. Duplicate Encoder
# Description:
#  Convert each character in a string to '(' if it appears only once or to ')' if it appears more than once in the string (case insensitive).
# Example Test Cases:

#! duplicate_encode("din") → "((("


#! duplicate_encode("recede") → "()()()"


#! duplicate_encode("Success") → ")())())"


def duplicate_encode(word):
    word_lower = word.lower()
    result = []
    for char in word_lower:
        if word_lower.count(char) == 1:
            result.append('(')
        else:
            result.append(')')
    return ''.join(result)


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))