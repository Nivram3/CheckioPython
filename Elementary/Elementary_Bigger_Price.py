'''
You have a table with all available goods in the store.
The data is represented as a list of dicts

Your mission here is to find the TOP most expensive
goods. The amount we are looking for will be given as
a first argument and the whole data as the second one

Input: int and list of dicts. Each dicts has two keys
"name" and "price"

Output: the same as the second Input argument.
'''

'''
def bigger_price(limit: int, data: list) -> list:
    return sorted(data, key=lambda x: -x['price'])[:limit]
    
OR

def bigger_price(limit: int, data: list) -> list:
    return  sorted(data, key=lambda x: x['price'], reverse = True)[:limit]


'''
def bigger_price(limit: int, data: list) -> list:
    prices_List = [dict.get('price') for dict in data]
    # self applies to object no need to assign to copy
    # add reverse=True to sort or sorted
    # sorted for any iterable, can be beyond just lists
    prices_List.sort(reverse=True)
    '''for dict in data:
        num = dict.get('price')
        prices_List.append(num)'''
    dict_List = []
    i = 0
    while len(dict_List) < limit:
        for dict in data:
            for k,v in dict.items():
                if v == prices_List[i]:
                    # check again for prices that are the same
                    if len(dict_List) < limit:
                        dict_List.append(dict)
                        i+=1
    return dict_List

data = [{'name': 'beans', 'price': 5.50},
                 {'name': 'bread', 'price': 3.25},
                 {'name': 'bananas', 'price': 2},
                 {'name': 'bagels', 'price': 3.7},
                 {'name': 'beer', 'price': 6.75},
                 {'name': 'broccoli', 'price': 3.7}]
while True:
    try:
        limit = int(input('How many goods do you want displayed?\n'
                          'The highest priced items will be displayed\n'))
        break
    except ValueError:
        print('Try Again\n')

print(bigger_price(limit,data))