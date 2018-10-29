#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'
#Modules


import math
from math import sqrt as s
class Module_demo():
    def mathModule(self,x):
        print(math.sqrt(x))
        print(s(x))

m = Module_demo()

x=10
m.mathModule(x)

from math import  factorial as f

class math_modules():
    def fact_module(self,x):
        print(f(x))

m = math_modules()
m.fact_module(x)

