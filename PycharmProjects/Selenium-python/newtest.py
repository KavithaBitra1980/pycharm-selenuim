#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#s= input('enter time')


#print(s1)
def timeConversion(s):

    if 'PM' in s:
        s1 = s.split(":")
        hour = int(s1[0])
        min = s1[1]
        sec = s1[2]
        if hour >=1 and hour <= 12:
            hour24fmt = hour + 12
            newfmt = str(hour24fmt)
            print('%d:%s:%s' % (newfmt, min, sec)

    else:
        print(s)





s = input()

result = timeConversion(s)

print(result )

