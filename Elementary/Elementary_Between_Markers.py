'''
You are given a string and two markers (the initial
and final). You have to find a substring enclosed
between these two markers. But there are a few
important conditions:

The initial and final markers are always different.
If there is no initial marker, then the first
character should be considered the beginning of a
string.
If there is no final marker, then the last character
should be considered the ending of a string.
If the initial and final markers are missing then
simply return the whole string.
If the final marker comes before the initial marker,
then return an empty string.

Input: Three arguments. All of them are strings.
The second and third arguments are the initial and final markers.

Output: A string.
'''

def between_markers(text, begin, end):
    begin_index = text.find(begin) + len(begin) -1 #index of begin
    end_index = text.find(end) #index of end

    if begin != end:
        if begin in text:
            if end in text:
                if end_index > begin_index:
                    return text[begin_index+1:end_index]
                else:
                    return ''
            else:
                return text[begin_index+1:]
        elif end in text:
            return text[0:end_index]
        else:
            return text
    else:
        return None

print(between_markers('No <hi>', '>', '<'))

