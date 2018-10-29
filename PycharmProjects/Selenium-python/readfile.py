#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo for reading a file

readfile1 = open("filename1.txt","r")
print(str(readfile1.read()))

print('this to read line by line')
readfile2 = open("filename1.txt","r")

print('print line by line',str(readfile2.readline()))


readfile1.close()
readfile2.close()