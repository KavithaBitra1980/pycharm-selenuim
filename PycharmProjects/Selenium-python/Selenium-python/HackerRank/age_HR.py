#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'
"""
Objective 
In this challenge, we're going to learn about the difference between a class and an instance; because this is an Object Oriented concept, it's only enabled in certain languages. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Write a Person class with an instance variable, , and a constructor that takes an integer, , as a parameter. The constructor must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as , the constructor should set  to  and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:

yearPasses() should increase the  instance variable by .
amIOld() should perform the following conditional actions:
If , print You are young..
If  and , print You are a teenager..
Otherwise, print You are old..
To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing everything in the future. The code that creates each instance of your Person class is in the main method. Don't worry if you don't understand it all quite yet!

Note: Do not remove or alter the stub code in the editor.

Input Format

Input is handled for you by the stub code in the editor.

The first line contains an integer,  (the number of test cases), and the  subsequent lines each contain an integer denoting the  of a Person instance.
"""

class Person:

    def __init__(self, initialAge):
        self.initialAge = initialAge
        if initialAge  > 0:
            age = initialAge
        else:
            age = 0
            print('Age is not valid, setting age to 0.')


    def amIOld(self):
        if age < 13:
            print('You are young..')
        elif age >= 13 and age < 18:
            print('You are a teenager..')
        else:
            print('You are old..')
        return age


    def yearPasses(self):
        global age
        age = age +1
        return age





t = int(input('enter how many times\n'))
for i in range(0,t) :
    age = int(input('enter age\n'))
    p = Person(age)
    p.amIOld()
    for j in range(0,3):
       p.yearPasses()
    p.amIOld()
    print(" ")
"""
4
-1
10
16
18
Sample Output

Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.

"""