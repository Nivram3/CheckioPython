# You are given a chunk of text. Gather all capital
# letters in one word in the order that they appear
# in the text.
#
# For example: text = "How are you? Eh, ok. Low or
# Lower? Ohhh.", if we collect all of the capital
# letters, we get the message "HELLO".
import re
def find_message(text: str) -> str:
    # re.findall returns all matches in a list
    matches = re.findall(r'[A-Z]',text)
    return ''.join(matches)
# join for strings to strings 
# append means add item to end of list


print(find_message('How are you? Eh, ok. Lr Lower? Ohhh.'))