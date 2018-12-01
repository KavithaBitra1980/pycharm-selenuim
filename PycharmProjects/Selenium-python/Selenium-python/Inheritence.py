#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'


class Cars(object):
    def __init__(self,model,year,price,condition):
        self.model = model
        self.year = year
        self.price = price
        self.condition = condition

    def status(self):
        print('the year of manufaction is',self.year)
        print('the condition of the car is',self.condition)

    def model_price(self):
        print('the model of the car',self.model)
        print('the price of the car is',self.price)
##Inheritence..........
class bmw(Cars):
    def __init__(self):
        # inheritence applied
        Cars.__init__(self,model='750i',year=1999,price=20000,condition='ok')
        print("this is an instance for BMW car")

class Benz(Cars):
    def __init__(self):
        Cars.__init__(self,model='ML250',year=1989,price=2000,condition='GOOD')
        print("this is an instance for BMW car")



car1 = Cars('550i','2015',90000,'good')
car2 = Cars('ml350',2010,9000,'ok')

#calling
brand1 = bmw()
brand2 = Benz()

print(car1.model)
print(car2.price)

car1.status()
car2.status()
car1.model_price()
brand1.status()
brand1.model_price()
brand2.status()
"""
RESULTS
this is an instance for BMW car
this is an instance for BMW car
550i
9000
the year of manufaction is 2015
the condition of the car is good
the year of manufaction is 2010
the condition of the car is ok
the model of the car 550i
the price of the car is 90000
the year of manufaction is 1999
the condition of the car is ok
the model of the car 750i
the price of the car is 20000
the year of manufaction is 1989
the condition of the car is GOOD

"""
