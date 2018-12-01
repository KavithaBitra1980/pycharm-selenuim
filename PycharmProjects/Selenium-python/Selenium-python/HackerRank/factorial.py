#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'


def FirstFactorial(num):
    i=1
    fact = 1
    while i <= num :
        fact = fact * i
        i = i + 1
    num = fact
    return num


# keep this function call here
print (FirstFactorial(int(input())))

5
