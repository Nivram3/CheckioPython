'''
4 substring missions
find a length the longest substring that consists of the same char
find the longest substring without repeating chars
find a length the longest substring that repeats more than once.
find first the longest repeating substring

This mission is the first one of the series. Here you
should find the length of the longest substring that
consists of the same letter. For example, line
"aaabbcaaaa" contains four substrings with the same
letters "aaa", "bb","c" and "aaaa". The last substring
is the longest one which makes it an answer.

Input: String.

Output: Int.

'''

def long_repeat(line):
    line = '?' + line
    max_repeat = 0
    current_repeat = 1
    i = 1
    while i < len(line):
        if line[i] == line[i-1]:
            current_repeat += 1
            i+=1
            if current_repeat > max_repeat:
                max_repeat = current_repeat
        else:
            if current_repeat > max_repeat:
                max_repeat = current_repeat
            current_repeat =1
            i+=1
    return max_repeat

print(long_repeat('abvvvvaacccz'))
if __name__ == '__main__':
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')


'''
longest_len = 0
current_len = 0
current = ''
for c in line:
    if c == current:
        current_len += 1
    else:
        current = c
        current_len = 1
    if current_len > longest_len:
        longest_len = current_len
return longest_len'''