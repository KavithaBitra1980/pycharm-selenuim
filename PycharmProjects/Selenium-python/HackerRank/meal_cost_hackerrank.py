#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

#Hackersrank day 3 meal cost
#mealCost = 12.0
#tipPercent = 20
#taxPercent = 8



mealCost = float(input('enter mealcost'))
tipPercent = int(input('enter tip percent'))
taxPercent = int(input('enter tax pecent'))

totalCost = mealCost + tipPercent * (mealCost/100) + taxPercent *(mealCost/100)
print('the total Cost is',round(totalCost))