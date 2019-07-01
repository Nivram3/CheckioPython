'''
You are given an array of numbers (floats).
You should find the difference between the maximum
and minimum element. Your function should be able to
handle an undefined amount of arguments.
For an empty argument list, the function should
return 0.

Floating-point numbers are represented in computer
hardware as base 2 (binary) fractions. So we should
check the result with ±0.001 precision.

Think about how to work with an arbitrary number of
arguments.

Input: An arbitrary number of arguments as numbers
(int, float).

Output: The difference between maximum and minimum
as a number (int, float).

Precondition: 0 ≤ len(args) ≤ 20
all(-100 < x < 100 for x in args)
all(isinstance(x, (int, float)) for x in args)
'''

# check if it is float or is integer.

def checkio(*args):
    # if it has elements
    if args:
        max_num = max(args)
        min_num = min(args)
        if max_num >= 0 and min_num < 0:
            dif = abs(max_num) + abs(min_num)
            if max_num and min_num == int:
                return int(dif)
            else:
                return dif
        else:
            # need extra abs for max and min are -
            dif = abs(abs(max_num) - abs(min_num))
            return dif
    else:
        return 0

# * for arbitrary num of arguments
print(checkio(-0.036,-0.11,-0.55,-64))