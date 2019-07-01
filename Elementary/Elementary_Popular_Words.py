'''
At the input of your function are given 2 arguments:
the text and the array of words the popularity of
which you need to determine.

When solving this task pay attention to the
following points:

The words should be sought in all registers.
This means that if you need to find a word "one"
then words like "one", "One", "oNe", "ONE" etc.
will do.

The search words are always indicated in the
lowercase.
If the word wasn’t found even once, it has to be
returned in the dictionary with 0 (zero) value.

Input: The text and the search words array.

Output: The dictionary where the search words are the keys and values are the number of times when those words are occurring in a given text.
'''
import re

def popular_words(text: str, words: list) -> dict:
    word_dictionary = {}
    for word in words:
        matches = re.findall(r'\b'+word+r'\b', text.lower())
        word_dictionary[word] = len(matches)
    return word_dictionary

text = 'When I was One\
        I had just begun\
        When I was Two\
        I was nearly new near'
words = ['i', 'was', 'three', 'two','near']
print(popular_words(text, words))

# for word in words:
#         dict[word] = text.count(word)
#also a .count option