'''
Given a text which contains different english letters
and punctuation symbols, find the most frequent letter
in the text. The letter returned must be in lower case.

While checking for the most wanted letter, casing does
not matter, so for the purpose of your search,
"A" == "a".

Make sure you do not count punctuation symbols, digits
and whitespaces, only letters.

If you have two or more letters with the same
frequency, then return the letter which comes first
in the latin alphabet. For example -- "one" contains
"o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a
string.
'''

# alt can all letters using ascii and char or import
# string >>> string.ascii_lowercase
# and append value to list then find index of highest
# value in list and then add 97 to it ,convert to chr
def checkio(text: str) -> str:
    alpha_set = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            alpha_set[char] = text.count(char)
    max_value = 0
    for k,v in alpha_set.items():
        if v > max_value:
            max_value = v
    most_common_letter = []
    for k, v in alpha_set.items():
        if v == max_value:
            most_common_letter.append(k)
    return sorted(most_common_letter)[0]

# sort prints out capital before lower case
print(checkio('abc DOZ'))