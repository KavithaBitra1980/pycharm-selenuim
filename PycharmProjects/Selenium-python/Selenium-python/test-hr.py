#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'


def solveminmax(a,b,c,d,e):
    return a+b+c+d+e
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

max_list = max(a,b,c,d,e)
min_list = min(a,b,c,d,e)


min_sum = (solveminmax(a,b,c,d,e)-max_list)
max_sum = (solveminmax(a,b,c,d,e)-min_list)

print(max_sum)
print(min_sum)

str1 = 'This is So nice KAVITHA '
count = 0
for i in str1:
    if i.isupper() == True:
        count = count +1


print(count)