#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

# DEMo of Exception Handling
def exceptionHandling():
    try:
        a = 10
        b = 20
        c = 0
        d = a * b / c
        print('the division is',d)

    #except ZeroDivisionError:
     #   print("this is demo of exception handling for divison by ZERO ")
    #except TypeError :
     #   print("string Type error")

    except:
        print("this is exception handling demo")
exceptionHandling()