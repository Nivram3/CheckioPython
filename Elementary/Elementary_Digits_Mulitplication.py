# You are given a positive integer.
# Your function should calculate the product of the
# digits excluding any zeroes.
#
# For example: The number given is 123405.
# The result will be 1*2*3*4*5=120
# (don't forget to exclude zeroes).
from functools import reduce

def checkio(number: int) -> int:
    numberString = str(number)
    # use list not split if only one string
    numList = list(numberString)
    # use to remove all elements of a certain type
    while '0' in numList:
        numList.remove('0')
    intNumList =[]
    for i in numList:
        intNumList.append(int(i))
    # reduce takes function and list as argument
    # reduce applies a function to all list elements
    # for element y, change to product of x and y

    # f = lambda x, y: y*x
    # is equivalent to:
    # def f(x, y):
    #     return y * x

    return reduce(lambda x, y: x*y, intNumList)

print(checkio(100))

# alternate
# result = 1
# for x in myList:
#     result = result * x
# return result :