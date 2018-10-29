#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#list from standard in
readfile = open('list1.txt',"r")
print(readfile.read())
#print(max(readfile))

for i in range(10):
    if not i%2 == 0:
        print(i+1)

list1 = {1,2,3,1,2,67,90}
print(max(list1))
readfile.close()