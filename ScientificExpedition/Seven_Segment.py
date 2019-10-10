'''
Link: https://py.checkio.org/en/mission/seven-segment/

Background:

You have a device that uses a Seven-segment display to display 2 digit numbers. However, some of the segments aren't working and can't be displayed.

You will be given information on the lit and broken segments. You won't know whether the broken segment is lit or not. You have to count and return the total number that the device may be displaying.

The input is a set of lit segments (the first argument) and broken segments (the second argument).

Uppercase letters represent the segments of the first out two digit number.
Lowercase letters represent the segments of the second out two digit number.
topmost: 'A(a)', top right: 'B(b)', bottom right: 'C(c)', bottommost: 'D(d)', bottom left: 'E(e)', top left: 'F(f)', middle: 'G(g)'

Input: Two arguments. The first one contains the lit
segments as a set of letters representing segments.
The second one contains the broken segments as a set
of letters representing segments.

Output: The total number that the device may be displaying.
'''

num_letter_configs = {
    '1': ('b','c'),
    '2': ('a','b','g','e','d'),
    '3': ('a','b','g','c','d'),
    '4': ('f','g','b','c'),
    '5': ('a','f','g','c','d'),
    '6': ('a','f','g','c','d','e'),
    '7': ('a','b','c'),
    '8': ('a','b','c','d','e','f','g'),
    '9': ('a','b','c','d','f','g'),
    '0': ('a','b','c','d','e','f')
}
# .items returns iterable of dictionary k,v pairs or just v

def seven_segment(lit_seg, broken_seg):
    # SOLUTION DONE WITH POSSIBILITIES FROM HAVING ALL LIT BROKEN SEGMENTS - IMPOSSIBILITIES FROM LIT SEGMENTS
    lit_first_impossibilities = set()
    lit_second_impossibilities = set()
    broken_ON_first_possibilities = set()
    broken_ON_second_possibilities = set()
    broken_OFF_first_impossibilities = set()
    broken_OFF_second_impossibilities = set()
    num_letter_configs_list = [x for x in num_letter_configs.items()]


    # determine impossibilities because of lit segments
    # if a lit segment not in a config, then that config is impossible
    for seg in lit_seg:
        for config in num_letter_configs_list:
            if not(seg.lower() in config[1]):
                if seg.isupper():
                    lit_first_impossibilities.add(config[0])
                else:
                    lit_second_impossibilities.add(config[0])
    # guaranteed impossible since if this segment is lit but not in the config, the config cannot occur
    # print('lit first IMPOSSIBLE',lit_first_impossibilities)
    # print('lit second IMPOSSIBLE',lit_second_impossibilities)

    # determine possibilities because of LIT broken segments
    # "all broken segments are on"
    for config in num_letter_configs_list:
        upper = list(set([x for x in broken_seg if x.isupper()] + [x for x in lit_seg if x.isupper()]))
        lower = list(set([x for x in broken_seg if x.islower()] + [x for x in lit_seg if x.islower()]))

        upper_result = all(elem.upper() in upper for elem in config[1])
        lower_result = all(elem in lower for elem in config[1])
        # print('upper',upper_result,config[0])
        # print('lower',lower_result,config[0])
        if upper_result:
            broken_ON_first_possibilities.add(config[0])
        if lower_result:
            broken_ON_second_possibilities.add(config[0])
    # print('broken on first POSSIBLE', [x[0] for x in broken_ON_first_possibilities])
    # print('broken on second POSSIBLE', [x[0] for x in broken_ON_second_possibilities])

    final_possibilities_first = [x for x in broken_ON_first_possibilities if x not in list(lit_first_impossibilities)]
    # print(final_possibilities_first)
    final_possibilities_second = [x for x in broken_ON_second_possibilities if x not in list(lit_second_impossibilities)]
    # print(final_possibilities_second)
    return len(final_possibilities_first)*len(final_possibilities_second)

if __name__ == '__main__':
    print(seven_segment({'B', 'C', 'a', 'c', 'd', 'f', 'g'}, {'A', 'D', 'G', 'e'}))
    print(seven_segment({'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'}, {'G', 'g'}))
    print(seven_segment({'B', 'C', 'b', 'c'}, {'A'}))