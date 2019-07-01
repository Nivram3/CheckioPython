# You are given a sequence of strings. You should join
# these strings into chunk of text where the initial
# strings are separated by commas. As a joke on the
# right handed robots, you should replace all cases of
# the words "right" with the word "left", even if it's
# a part of another word. All strings are given in
# lowercase.
#
# Input: A sequence of strings as a tuple of strings
#
# Output: The text as a string.
#
# Precondition:
# 0 < len(phrases) < 42
import re

def left_join(phrases):
    phrases = str(phrases)
    new_String = re.sub(r'right', r'left', phrases)
    new_String = new_String.strip(",()")
    # can .replace and .replace after if needed, since
    # replace only takes 2 args not more
    new_String = new_String.replace("', '",',')
    new_String = new_String.strip("'")
    return new_String

strings = ("brightness wright",)
print(left_join(strings))