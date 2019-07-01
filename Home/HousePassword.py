import random

# random.choice(seq)
# Return a random element from the non-empty sequence seq.

# random.sample(population, k)
# Return a k length list of unique elements chosen from the
# population sequence.

# the password will be considered strong enough if its length
# is greater than or equal to 10 symbols, it has at least one digit,
# as well as containing one uppercase letter and one lowercase letter.
'''
numList = [0,1,2,3,4,5,6,7,8,9]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
passLength = random.randint(10,15) # includes 15
numNum = passLength - random.randint(1, passLength-2)
numLet = passLength - numNum
numletUpper = range(numLet-numLet+1,numLet-1)
print('Password Length is ' + str(passLength))
print('Number of Numbers in password is ' + str(numNum))
print('Number of Letters in password is ' + str(numLet))
passLetters = 0
while passLetters <= numLet:
    
    numLetrandom.choice(alphabet)
    passLetters +=
'''

# oops not password generator, password checker
def strongPasswordChecker (password):
    if len(password) >= 10:
        listPassChar = list(password)
        # password.split()only for multiple strings
        numIndex = 0
        while True:
            if str.isdigit(listPassChar[numIndex]) is False:
                numIndex+=1
                if numIndex >= len(listPassChar):
                    return False
                continue # not needed but basically skips current iteration
            elif str.isdigit(listPassChar[numIndex]) is True:
                break
        lowIndex = 0
        while True:
            if str.islower(listPassChar[lowIndex]) is False:
                lowIndex+=1
                if lowIndex >= len(listPassChar):
                    return False
                continue
            elif str.islower(listPassChar[lowIndex]) is True:
                break
        upIndex = 0
        while True:
            if str.isupper(listPassChar[upIndex]) is False:
                upIndex+=1
                if upIndex >= len(listPassChar):
                    return False
                continue
            elif str.isupper(listPassChar[upIndex]) is True:
                break
        return True
    return False

password = input('Check if your password is strong!'
                 '\nTrue = Strong' 
                 '\nInput Password: '
                )
print(strongPasswordChecker(password))

