'''
There is a list which contains integers or other nested
lists which may contain yet more lists and integers
which then… you get the idea.

You should put all of the integer values into one flat
list. The order should be as it was in the original
list with string representation from left to right.

We need to hide this program from Nikola by keeping it
small and easy to hide. Because of this, your code
should be shorter than 140 characters
(with whitespaces).

Input data: A nested list with integers.

Output data: The one-dimensional list with integers.

eg. flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
'''

# def flat_list(array):
#     final_list = []
#     for i in array:
#         try:
#             if len(i) >= 1:
#                 for j in i:
#                     try:
#                         if len(j) >= 1:
#                             for k in j:
#                                 try:
#                                     if len(k) >= 1:
#                                         for l in k:
#                                             final_list.append(l)
#                                 except TypeError:
#                                     final_list.append(k)
#                     except TypeError:
#                         final_list.append(j)
#         except TypeError:
#             final_list.append(i)
#     return final_list
#
# my_list = [1,[2,[3,[4,5],6,[7,8]]]]
# print(flat_list(my_list))

def flat_list(array):
    final_list = []
    array = str(array).replace('[','').replace(']','').replace(',','').split()
    print(array)
    for char in array:
        final_list.append(int(char))
    return final_list


my_list = [1,[-2,[3,[4,5],6,[7,8]]]]
print(flat_list(my_list))

'''
BETTER
def flat_list(array):
    ret_list = []
    for e in array:
        if type(e) == list:
            tmp_list = flat_list(e)
            ret_list.extend(tmp_list)
        else:
            ret_list.append(e)
    return ret_list
    
def flat_list(array):
    if type(array) is int:
        return [array]
    result = []
    for subarray in array:
        result.extend(flat_list(subarray))
        .extend adds all items of a list to the end
    return result
'''