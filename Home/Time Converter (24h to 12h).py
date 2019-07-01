'''
the output format should be 'hh:mm a.m.'
(for hours before midday) or 'hh:mm p.m.'
(for hours after midday)
if hours is less than 10 - don't write a '0' before it.
For example: '9:05 a.m.'

Input: Time in a 24-hour format (as a string).

Output: Time in a 12-hour format (as a string).

Precondition:
'00:00' <= time <= '23:59'
'''

def time_converter(time):
    time = time.split(':')
    time = [int(x) for x in time]
    if 0 <= time[0] <= 23 and 0 <= time[1] <= 59:
        if time[1] < 10:
            time[1] = '0' + str(time[1])
        if time[0] == 0:
            return ('12:{} a.m.').format(time[1])
        elif 1 <= time[0] < 12:
            return ('{1}:{0} a.m.').format(time[1],time[0])
        elif time[0] == 12:
            return ('{}:{} p.m.').format(time[0],time[1])
        else:
            time[0] = time[0] - 12
            return ('{}:{} p.m.').format(time[0],time[1])
    else:
        return 'Invalid 24h Time'



my_time = '0:00'
print(time_converter(my_time))


