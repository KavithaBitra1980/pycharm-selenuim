#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'
#DEmo to read a file and print or write out to another file

readfile1 = open("read-write-textfile.txt","r")
print(str(readfile1.read()))
readfile1.close()

readfile1 = open("read-write-textfile.txt","r")

writefile1 = open("writefile-text.txt","w")
for item in readfile1:
    writefile1.write(str(item) +" ")
    writefile1.write(" \n iam adding kavitha,annanya and chandra\n")

writefile1.close()
print('..............................................................\n')
print('this is to read and prints file from write file\n')

openread = open('writefile-text.txt','r')
print(str(openread.read()))

"""
RESULT

this is akvitha
this is to test read and write a file
first it will read the file and it will write to writefile
..............................................................

this is to read and prints file from write file

this is akvitha
  
 iam adding kavitha,annanya and chandra
this is to test read and write a file
  
 iam adding kavitha,annanya and chandra
first it will read the file and it will write to writefile  
 iam adding kavitha,annanya and chandra


Process finished with exit code 0

"""
