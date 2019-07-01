'''
Given a non-empty list of integers (X)
Return a list consisting of only the non-unique elements
in this list.
Do not change the order of the list.
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements
and result will be [1, 3, 1, 3]

Input: A list of integers.

Output: An iterable of integers.
'''
# tests = [[1,2,4,5,4,2],[3,2,1],[],[2,2,2],[10, 9, 10, 10, 9, 8]]
def checkio(data: list) -> list:
    #data = [num for num in data if num not in (2,3)]
    unique_nums = []
    for num in data:
        if data.count(num) == 1:
            unique_nums.append(num)
    for num in unique_nums:
        data.remove(num)
    return data

# for my_list in tests:
#     print((checkio(my_list)))
print(checkio([1,2,3,4,5,6]))
print(checkio([5,4,3,2,1]))
print(checkio([1,2,3,4]))
print(checkio([4,1,2,3]))

'''
new_data = list()
    for i in data:
        if data.count(i) > 1:
            new_data.append(i)
'''