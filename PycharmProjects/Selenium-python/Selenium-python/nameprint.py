#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

class Person:
    def __init__(self,name):
        self.name = name
        print('my name is',name)


n=int(input('enter how many names'))

for i in range(0,n):
    name=input()
    p = Person(name)
    #p.pname(name)