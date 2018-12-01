#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo of file handling for writing
#file1 = [1,2,3,4]

my_file1 = open('filename1.txt',"a")
my_file2 = open('filename2.txt',"a")

for item in range(50,100):
    if item % 2 == 0:
        my_file1.write(str(item) + " ")


    else:
        my_file2.write(str(item) +" ")

my_file1.close()
my_file2.close()

