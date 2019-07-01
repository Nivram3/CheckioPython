'''
Sort the given iterable so that its elements end up in
the decreasing frequency order, that is, the number of
times they appear in elements. If two elements have
the same frequency, they should end up in the same
order as the first appearance in the iterable.

Input: Iterable

Output: Iterable

Precondition: elements can be ints or strings
'''

def frequency_sort(items):
    print(items)
    unique_set = set(items)
    print(unique_set)
    my_dict = {}
    for i in unique_set:
        my_dict[i] = items.count(i)
    print(my_dict)
    result = []
    #print(my_dict.get(8))

    while len(result) < len(items):
        max_val = 0
        max_key = ''
        for k, v in my_dict.items():
            if v > max_val:
                max_val = v
                max_key = k
        smallest_index = len(items) - 1
        for item in my_dict.items():
            if item[1] == max_val:
                if items.index(item[0]) < smallest_index:
                    smallest_index = items.index(item[0])
                max_key = items[smallest_index]
        my_dict.pop(max_key, None)
        i = 0
        while i < max_val:
            result.append(max_key)
            i+=1
    return result

print(frequency_sort([8, 6, 2, 2, 6,]))
