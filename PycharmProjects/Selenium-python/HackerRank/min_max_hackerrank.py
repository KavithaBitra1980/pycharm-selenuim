#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#HACKER RANK SAMPLES ----->MIN_max_sum

list1 = [1,2,3,4,5]


max_of_list = max(list1)
min_of_list = min(list1)

print(max_of_list)
print(min_of_list)

print((max_of_list))

sum = 0

for i in list1:
    i1= i
    sum = sum + i1
    print(i1)


print(sum)


print('print number\n')
def solveminmax(a,b,c,d,e):
    return a + b+c+d+e
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

max_list = max(a,b,c,d,e)
print('the max is =',max(a,b,c,d,e))

min_list = min(a,b,c,d,e)
print('the min is = ',min(a,b,c,d,e))

min_sum = solveminmax(a,b,c,d,e)-max_list
max_sum = solveminmax(a,b,c,d,e)-min_list

print('the maximum sum of the list is',max_sum)
print('the minimum sum of the list is',min_sum)
