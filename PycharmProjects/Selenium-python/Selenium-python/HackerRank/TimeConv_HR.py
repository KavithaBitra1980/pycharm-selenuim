#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo of time ocnversion
def timeConversion(s):
    for i in s:
        if i == 'PM':
            hour1 = s[0,1]
            if hour1 >=1 and hour1 <=12:
                time = hour1 + 12
                print(time)
        else:





s = input()

result = timeConversion(s)
print(result + '\n')
