#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Hackersrank day 3 meal cost
#mealCost = 12.0
#tipPercent = 20
#taxPercent = 8
"""Objective 
In this challenge, you'll work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

Input Format

There are  lines of numeric input: 
The first line has a double,  (the cost of the meal before tax and tip). 
The second line has an integer,  (the percentage of  being added as tip). 
The third line has an integer,  (the percentage of  being added as tax).

Output Format

Print the total meal cost, where  is the rounded integer result of the entire bill ( with added tax and tip).

"""

mealCost = float(input('enter mealcost'))
tipPercent = int(input('enter tip percent'))
taxPercent = int(input('enter tax pecent'))

totalCost = mealCost + tipPercent * (mealCost/100) + taxPercent *(mealCost/100)
print('the total Cost is',round(totalCost))