def index_Power(array,n):
    try:
        return (array[n])**n
    except IndexError:
        return -1

print(index_Power([0,9,11,14],3))