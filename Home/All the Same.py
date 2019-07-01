'''
In this mission you should check if all elements in
the given list are equal.

Input: List.

Output: Bool.

all_the_same([1, 1, 1]) == True
all_the_same([1, 2, 1]) == False
all_the_same(['a', 'a', 'a']) == True
all_the_same([]) == True
'''
# can also convert to set for unique element number

def all_the_same(l):
    try:
        num = l.count(l[0])
        if num == len(l):
            return True
        else:
            return False
    except IndexError:
        return True

l_sample = ['a','A']
print(all_the_same(l_sample))