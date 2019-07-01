'''
Find the angle of the sun above the horizon knowing
the time of the day.

The sun rises in the East at 6:00 AM, which
corresponds to the angle of 0 degrees.
At 12:00 PM the sun reaches its zenith, which
means that the angle equals 90 degrees.
6:00 PM is the time of the sunset so the angle is
180 degrees.

If the input will be the time of the night (before 6:00 AM or
after 6:00 PM), your function should return -
"I don't see the sun!".

Input: The time of the day.

Output: The angle of the sun, rounded to 2 decimal
places.

Precondition:
00:00 <= time <= 23:59
'''

def sun_angle(time):
    h,m = time.split(':')
    h = int(h)
    m = int(m)
    if 18 > h >= 6 and 59 >= m >= 0:
        return(h-6)*15 + m*0.25
    if h == 18 and m == 0:
        return round(180,2)
    else:
        return "I don't see the sun!"
print(sun_angle('6:01'))
# 6:00 = 0
# 12:00 = 90
# 18:00 = 180

# 6 hours = 90 deg
# 1 hour = 15 deg
# 1 min = 0.25 deg
