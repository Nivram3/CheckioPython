'''
You are given a string and two markers
(the initial one and final).
You have to find a substring enclosed between
these two markers. But there are a few important
conditions.

The initial and final markers are always
different.
The initial and final markers are always 1 char
size.
The initial and final markers always exist in a
string and go one after another.

Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.
'''
# DONE POORLY
import re
def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # for char in text:
        # print(text.index(char))
    if len(begin) ==1 and len(end) == 1:
        if begin != end:
            try:
                if begin == "[" and end == "]":
                    match = re.findall(r'\[' + r'[\w\s]+' + r'\]', text)
                    print(match)
                    match = match[0]
                    match = match.strip(begin)
                    match = match.strip(end)
                    return match
                else:
                    match = re.findall(begin + r'\w+' + end, text)
                    match = match[0]
                    match = match.strip(begin)
                    match = match.strip(end)
                    #match = re.sub('[][\']', '', match)
                    #match = match.strip(begin)
                    #match = match.strip(end)
                    return match
            except IndexError:
                return ""
        else:
            return 'Error in Input'
    else:
        return 'Error in Input'

print(between_markers("[an apple]", '[', ']'))

'''
BETTER SOLUTIONS

def between_markers(text, begin, end):
    begin = text.find(begin) + 1 if begin in text else None
    end = text.find(end) if end in text else None
    return text[begin:end]
    
def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.index(begin) + 1:text.rindex(end)]
'''