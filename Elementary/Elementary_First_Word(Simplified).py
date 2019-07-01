'''
You are given a string where you have to find its first
word.

This is a simplified version of the First Word mission.

Input string consists of only english letters and
spaces.

There aren’t any spaces at the beginning and the end of
the string.

Input: A string.
Output: A string.

Precondition: Text can contain a-z, A-Z and spaces.
'''

def first_word(text: str) -> str:
    # if split() left empty, split on all whitespace anyways
    return text.split(" ")[0]

input_string = "Hello everyone"
print(first_word(input_string))