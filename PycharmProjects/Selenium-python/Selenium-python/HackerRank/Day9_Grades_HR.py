#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'



def gradingStudents(grades):
    result=[]
    for i in grades:
        if i >= 38:
            if i % 5 >= 3:
                i = i +(5-(i % 5))
        result.append(i)

    return result



f = open("some.txt","w")
n = int(input())
grades = []
for grades_item in range(n):
    grades_item = int(input())
    grades.append(grades_item)
result = gradingStudents(grades)
f.write('\n'.join(map(str,result)))
f.write('\n')
f.close()
