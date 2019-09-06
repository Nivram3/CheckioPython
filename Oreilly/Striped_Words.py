'''
Link: https://py.checkio.org/en/mission/striped-words/

Background:
You are given a block of text with different words.
These words are separated by white-spaces and
punctuation marks. Numbers are not considered words in
this mission (a mix of letters and digits is not a
word either). You should count the number of words
(striped words) where the vowels with consonants are
alternating, that is; words that you count cannot have
two consecutive vowels or consonants. The words
consisting of a single letter are not striped -- do not
count those. Casing is not significant for this mission.

Input: A text as a string (unicode)

Output: A quantity of striped words as an integer.

Precondition:The text contains only ASCII symbols.
0 < len(text) < 105
'''
import string
import re

consonants = string.ascii_lowercase
vowels = 'aeiouy'
for letter in consonants:
    if letter in vowels:
        # strings are immutable so they create a new instance using .replace()
        consonants = consonants.replace(letter,'')

def checkio(text):
    matches = re.findall(r'[\w]+',text)
    criteria_counter = 0
    for match in matches:
        alternating_counter = 1
        # DO NOT USE .INDEX() AS THAT GIVES FIRST CASE OF ELEMENT IN ITERATOR
        for index, letter in enumerate(match):
            if len(match) > 1:
                if letter.lower() in consonants:
                    try:
                        if match[index+1].lower() in vowels:
                            alternating_counter += 1
                        else:
                            break
                    except IndexError:
                        continue
                elif letter.lower() in vowels:
                    try:
                        if match[index+1].lower() in consonants:
                            alternating_counter += 1
                        else:
                            break
                    except IndexError:
                        continue
                print(match, alternating_counter)
        if alternating_counter == len(match) and len(match) > 1:
            criteria_counter += 1
            print(match)
    return criteria_counter


if __name__ == '__main__':
    print(checkio('nunc ata ta nun'))
