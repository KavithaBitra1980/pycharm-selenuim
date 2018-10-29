#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'


#Demo of read write file using with as
"""
print('this is normal write start')
write_text = open("write-file.txt","w")
write_text.write(" today is sunday")
write_text.close()

print('this is read')
read_text = open("write-file.txt","r")
print(str(read_text.read()))

"""
print('with As write start')
with open('write-file.txt',"w") as writefile:
    writefile.write("This is an example for using with and AS")

print('this is to read')
with open('write-file.txt','r') as readfile:
    print(str(readfile.read()))



"""
RESULTS
with As write start
this is to read
This is an example for using with and AS

"""

