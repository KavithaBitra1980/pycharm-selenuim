#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'
#Demo of even or odd hacrrank
"""
Objective 
In this challenge, we're getting started with conditional statements. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.
"""

for i in range(8):
    n = int(input('enter a number\n'))
    if n % 2 == 1:
        print('Weird')
    if n%2 ==0 and n >=2 and n <=5 and n:
        print('2,5Not Weird')
    elif n%2 ==0 and n >=6 and n <20:
        print('6Weird')
    elif n%2 ==0 and n %2 == 0 and n>20:
        print('20Not Weird')
        continue


