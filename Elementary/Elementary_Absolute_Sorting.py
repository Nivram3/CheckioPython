'''
The array (a tuple) has various numbers.
You should sort it, but sort it by absolute value in
ascending order.

For example, the sequence (-20, -5, 10, 15) will be
sorted like so: (-5, 10, 15, -20). Your function
should return the sorted list or tuple.

Precondition: The numbers in the array are unique by
their absolute values.

Input: An array of numbers , a tuple..

Output: The list or tuple (but not a generator)
sorted by absolute values in ascending order.

Addition: The results of your function will be shown
as a list in the tests explanation panel.

Precondition: len(set(abs(x) for x in array)) == len(array)
0 < len(array) < 100
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
'''

def checkio(numbers_array: tuple) -> list:
    try:
        pos_num_lst = []
        neg_num_lst = []
        for num in numbers_array:
            if num <= 0:
                neg_num_lst.append(num)
            else:
                pos_num_lst.append(num)
        # equal to sort then reverse methods
        pos_num_lst.sort()
        neg_num_lst.sort(reverse=True)
        print(neg_num_lst)
        print(pos_num_lst)
        final_list = neg_num_lst
        if len(neg_num_lst) > 0 and len(pos_num_lst) > 0:
            i = 0
            j = 0
            while len(final_list) < len(numbers_array):
                if pos_num_lst[i] > abs(final_list[-1]):
                    # cannot insert at -1, last num will be wrong
                    final_list.insert(len(final_list), pos_num_lst[i])
                    i+=1
                elif pos_num_lst[i] > abs(final_list[j]):
                    j+=1
                else:
                    final_list.insert(j,pos_num_lst[i])
                    j = 0
                    i += 1
            return final_list
        elif len(neg_num_lst) > 0:
            return neg_num_lst
        elif len(pos_num_lst) > 0:
            return pos_num_lst
    except TypeError:
        single_num=[]
        single_num.append(numbers_array)
        return single_num
'''
WORKSS!! try keys??

def checkio(numbers_array: tuple) -> list:
    return sorted(numbers_array, key=abs)
'''

numbers_array = (-2,1)
print(checkio(numbers_array))

