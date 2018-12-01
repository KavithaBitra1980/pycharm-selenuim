#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Demo of Phone Book_Hacker Rank


#name,number = name_number.split()

n = int(input())

my_dict1 = {}
for i in range(n):
    name_number = input()
    name,number = name_number.split()
    my_dict1[name] = number

print(my_dict1)

check_name = input()

if check_name in my_dict1.keys():
    print(check_name,'=',my_dict1.get(check_name))
else:
    print('Not Found')






