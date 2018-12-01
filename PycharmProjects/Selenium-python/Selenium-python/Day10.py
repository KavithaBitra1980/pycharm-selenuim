#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

phone_book = {}
n = int(input())
for i in range(n):
    name_number = input()
    name,number = name_number.split()
    #print(name,number)
    phone_book[name] = number

print(phone_book)
for i in range(n):
    check_name = input()
    if check_name in phone_book:
        print(check_name+'=',phone_book.get(check_name))
    else:
        print('Not found')
