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


    except:
        print("this is exception handling demo")
        #raise Exception('this is an excpetion')
    else:
        print('there is no excpetion so this statement is executed')
    finally:             #"this is usefull to close all opend files,drivers"
        print('this FINALLY is exceuting')
exceptionHandling()