'''
You are given a string with words and numbers
separated by whitespaces (one space). The words
contains only letters. You should check if the string
contains three words in succession. For example, the
string "start 5 one two three 7 end" contains three
words in succession.

Input: A string with words.

Output: The answer as a boolean.

Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
0 < len(words) < 100
'''

def checkio(words: str) -> bool:
    # check which are strings, find 3 in a row
    bool_list = []
    words = words.split(' ')
    for item in words:
        try:
            item = int(item)
            bool_list.append('False')
            #print(isinstance(item,str))
        except ValueError:
            bool_list.append('True')

    print(bool_list)

    i = 0
    while i <= len(bool_list)-3:
        if bool_list[i] == 'True':
            if bool_list[i+1] == 'True':
                if bool_list[i+2] == 'True':
                    return True
                else:
                    i+=1
            else:
                i+=1
        else:
            i+=1
    return False






string = '2 4 a b 1 c d 2 9 2 a k o'
print(checkio(string))