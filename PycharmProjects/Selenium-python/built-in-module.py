#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

# Demo of built in modules...

#import car_module_package.car as car
#import car_module_package.car_brands as carbrand
from car_module_package.car import  car_sale,car_info
from car_module_package.car_brands import car_brands_info



class ourOwnModule():
    def car_description(self):
        car_brands_info(brand1='bmw', brand2='benz', brand3='toyota', brand4='Honda')

        make = 'bmw'
        model = '550i'
        price = 55000
        condition = 'good'

        print('the car details are')
        car_info(make, model,price,condition)
        car_sale(discount=5.5)


m = ourOwnModule()

m.car_description()

"""
RESULTS
the brands 1 is bmw
the brands 2 is benz
the brands 3 is toyota
the brands 4 is Honda
the car details are
The make of the car is bmw
the Model of the car is 550i
the price of the car is 55000
the condition of the car is good
the discount is  5.5

"""
