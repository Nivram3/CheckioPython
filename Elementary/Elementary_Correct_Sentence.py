# For the input of your function, you will be given one
# sentence. You have to return a corrected version,
# that starts with a capital letter and ends with a
# period (dot).
#
# Pay attention to the fact that not all of the fixes
# are necessary. If a sentence already ends with a
# period (dot), then adding another one will be a
# mistake.
#
# Input: A string.
#
# Output: A string.
#
# Precondition: No leading and trailing spaces,
# text contains only spaces, a-z A-Z , and .


# string.capitalize() makes first letter capital,
# rest lower
word = 'hELlo'
print(word.capitalize())
def correct_sentence(text: str) -> str:
    # string.replace(old, new, count)
    # count – the number of times you want to replace
    # the old substring with the new substring.
    # (Optional ). If count not specified, will do it
    # at all occurrences
    firstUppercase =''
    if text[0].islower():
        firstUppercase = text[0].upper()
        text = text.replace(text[0],firstUppercase,1)
    if text[-1] != '.':
        text = text + '.'
    return text




text = 'greetings, friends'
print(correct_sentence(text))