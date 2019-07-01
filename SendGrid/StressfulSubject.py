# The function should recognise if a subject line is stressful.
# A stressful subject line means that all letters are in uppercase,
# and/or ends by at least 3 exclamation marks,
# and/or contains at least one of the following “red” words:
# "help", "asap", "urgent". Any of those "red" words can be spelled
# in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P",
# even in a very loooong way "HHHEEEEEEEEELLP"

# Precondition: Subject can be up to 100 letters

# import regular expressions
import re
def is_stressful(subj):
    subjCharList = list(subj)
    subjCharListNoSpaces = subjCharList.copy()
    redWords = ['help', 'asap', 'urgent']
    if len(subj) <= 100:
        # use \ for continuing code on next line (escape character)
        upCounter = 0
        while ' ' in subjCharListNoSpaces:
            subjCharListNoSpaces.remove(' ')
        while True:
            if str.isupper(subjCharListNoSpaces[upCounter]) is True:
                upCounter+=1
                if upCounter >= len(subjCharListNoSpaces):
                    return True
                else:
                    break
        exclamCounter = 0
        for char in subjCharList[-3:]:
            if char == '!':
                exclamCounter +=1
            if exclamCounter == 3:
                return True
        subjLower = subj.lower()
        subjLowerEdit = subjLower.translate({ord(i): None for i in '+-!'})
        redWordCheckSet = set(redWords).intersection(subjLowerEdit.split())
        print(redWordCheckSet)
        # data structures detected as empty if treated as boolean in if statement
        if redWordCheckSet:     # if it has anything in it, return True
            return True
        # or can use length check of set
        #re.split('\++', subjLower)
        #re.split('\-+', subjLower)
        #re.split('!+', subjLower)
        #splitNonWords = re.split('\W+', subjLower)
    return False

print(is_stressful('help'))
