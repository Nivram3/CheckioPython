# You are given an array of integers. You should find
# the sum of the integers with even indexes
# (0th, 2nd, 4th...).
# Then multiply this summed number
# and the final element of the array together.
#
# For an empty array, the result is 0(zero).
#
# Input: A list of integers.
#
# Output: The number as an integer.
#
# Precondition: 0 ≤ len(array) ≤ 20
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)

def checkio(array):
    evenIndexList = []
    i = 0
    if len(array) >= 1:
        while i < len(array):
            evenIndexList.append(array[i])
            i +=2
        indexSum = sum(evenIndexList)
        product = indexSum*array[-1]
        return product
    else:
        return 0
array = [2,3,4,5]
print(checkio(array))
    # empty sequences are False
    # Yes:
    #if not seq:
    #    if seq:

    #No:
    #if len(seq):
    #    if not len(seq):

    # def is_empty(any_structure):
    #     if any_structure:
    #         print('Structure is not empty.')
    #         return False
    #     else:
    #         print('Structure is empty.')
    #         return True