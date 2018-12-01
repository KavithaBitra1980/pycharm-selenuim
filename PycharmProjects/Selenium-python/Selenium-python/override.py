#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'


class Cars(object):
    def __init__(self,model,year,price,condition,review,decision):
        self.model = model
        self.year = year
        self.price = price
        self.condition = condition
        self.review = review
        self.decision = decision

    def status(self):
        print('the year of manufaction is %s',self.year)



    def model_price(self):
        print('the model of the car',self.model)
        print('the price of the car is',self.price)
##Inheritence..........
class bmw(Cars):
    def __init__(self):
        # inheritence applied
        Cars.__init__(self,model='750i',year=1999,price=20000,condition='ok',review='4star',decision='go')
        print("this is an instance for BMW car")

class Benz(Cars):
    def __init__(self):
        Cars.__init__(self,model='ML250',year=1989,price=2000,condition='GOOD',review='3star',decision='no-go')
        print("this is an instance for Benz car")

            #over riding the methods

    def status(self):
        super(Benz,self).status()
        print('the reviews says',self.review)

    def model_price(self):
        super().model_price()
        print('to go not to go decision',self.decision)

    def display(self):
        print('the price is unique',self.price)


#calling
brand1 = bmw()
brand2 = Benz()


brand1.status()
brand1.model_price()
brand2.status()
brand2.display()
brand2.model_price()

"""
RESULTS
this is an instance for BMW car
this is an instance for Benz car
the year of manufaction is %s 1999
the model of the car 750i
the price of the car is 20000
the year of manufaction is %s 1989
the reviews says 3star
the price is unique 2000
the model of the car ML250
the price of the car is 2000
to go not to go decision no-go


"""


