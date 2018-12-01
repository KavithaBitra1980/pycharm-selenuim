#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo of Binary

n = int(input('enter number\n'))
r = 0
count1= 0
count0 = 0
listnum=[]
while n > 0:
    r = n % 2
    n =  n // 2
    listnum.append(r)

print(listnum)
new_list = listnum[::-1]
print(new_list)

for i in new_list:
    if i == 1:
        count1 = count1 + 1
    else:
        if count1 > count0:
            count0 = count1
        count1 = 0
#print(count0)
#print(count1)
if count1 > count0:
   count0 = count1
print(count0)













