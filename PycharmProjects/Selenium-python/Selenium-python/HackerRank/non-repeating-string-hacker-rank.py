#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'
# First Non- repeating string

str1 = 'tthis is my first string'
print(str1.count('i'))

print(str1[0])
if str1[0] != str1[1]:
    print('the first non repeating string is',str1[0])
else:
    print('the string is repeated')

print ('print non repeated........................')

str2 = 'geek of the greks'
for i in str2:
    countstr2 = str2.count(i)
    if countstr2 == 1:
        print(i)
        break
#print('non_repeat is',non_repeat)
print('the first non repeated one is',i)




