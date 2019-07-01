'''
after each consonant letter the bird appends a random
vowel letter (l ⇒ la or le);
after each vowel letter the bird appends two of the
same letter (a ⇒ aaa); Vowels letters == "aeiouy"

words separated by letters
'''

vowels = 'aeiouy'
def translate(phrase):
    phrase = phrase.split()
    final = []
    for word in phrase:
        final.append(translation(word))
    return ' '.join(final)
def translation(phrase):
    i = 0
    while i < len(phrase):
        if phrase[i].isalpha() and phrase[i] not in vowels:
            #phrase = phrase.replace(phrase[index+1],'')
                #replaces all instances of the char
            phrase = phrase[:i+1] + phrase[i+2:]
            i+=1
        elif phrase[i].isalpha() and phrase[i] in vowels:
            phrase = phrase[:i+1] + phrase[i+3:]
            i+=1
            continue
    return phrase

print(translate("hoooowe yyyooouuu duoooiiine"))

# while cur < len(word):
#             letter = word[cur]
#             cur += 3 if letter in VOWELS else 2
#             acc.append(letter)