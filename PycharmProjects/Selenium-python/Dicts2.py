#Dictionary Define Dictionary,Nested Dicts,Dicts Method
print('kavihta')
print(2+3)

#Describing Normal Dicts
studentRecord = {"name": "kavihta","sub1":"maths","grade":"A","sub2":"Social","Marks":89}

print(studentRecord)
print(studentRecord.keys())
studentRecord ["totalMarks"] = 450

print(studentRecord)

#Describing Nested Dicts

MarksOfKavitha = [85,90,78,89,90]
print('marks in hindi is ', MarksOfKavitha[-1])

print('..........................................')

MarksinDetail = {"Std1" : {"Maths" : 90,"Science" : 87,"english" : 88, "Social":92}, "Std2" : {"Maths" : 80,"Science" : 87,"english" : 78, "Social":82}}
desired = MarksinDetail["Std1"]["Maths"]
print(desired)
print(MarksinDetail["Std2"]["Maths"])

#Describing Dicts Methods
print('..................................................')

cars = {'benz':{'Model':'ML350','year':2015,'price':55000,'condition':'precertified'},
        'bmw': {'Model': '750i', 'year': 2010, 'price': 35000, 'condition': 'not-certified'},
        'Honda': {'Model': 'civic', 'year': 2007, 'price': 5000, 'condition': 'precertified'}}

print(cars.keys())
print(cars.values())
print(cars.items())
print(MarksinDetail.items())

cars_copy = cars.copy()
print('just cars',cars)
print('copied cars dict',cars_copy)

print('the poped item from cars',cars_copy.pop('Honda'))

list1 = [1,2,3,4,5,6,78]
print('the poped itsm is',list1.pop())

"""
#############RESULTS
kavihta
5
{'name': 'kavihta', 'sub1': 'maths', 'grade': 'A', 'sub2': 'Social', 'Marks': 89}
dict_keys(['name', 'sub1', 'grade', 'sub2', 'Marks'])
{'name': 'kavihta', 'sub1': 'maths', 'grade': 'A', 'sub2': 'Social', 'Marks': 89, 'totalMarks': 450}
marks in hindi is  90
..........................................
90
80
..................................................
dict_keys(['benz', 'bmw', 'Honda'])
dict_values([{'Model': 'ML350', 'year': 2015, 'price': 55000, 'condition': 'precertified'}, {'Model': '750i', 'year': 2010, 'price': 35000, 'condition': 'not-certified'}, {'Model': 'civic'
, 'year': 2007, 'price': 5000, 'condition': 'precertified'}])
dict_items([('benz', {'Model': 'ML350', 'year': 2015, 'price': 55000, 'condition': 'precertified'}), ('bmw', {'Model': '750i', 'year': 2010, 'price': 35000, 'condition': 'not-certified'}),
 ('Honda', {'Model': 'civic', 'year': 2007, 'price': 5000, 'condition': 'precertified'})])
dict_items([('Std1', {'Maths': 90, 'Science': 87, 'english': 88, 'Social': 92}), ('Std2', {'Maths': 80, 'Science': 87, 'english': 78, 'Social': 82})])
just cars {'benz': {'Model': 'ML350', 'year': 2015, 'price': 55000, 'condition': 'precertified'}, 'bmw': {'Model': '750i', 'year': 2010, 'price': 35000, 'condition': 'not-certified'}, 'Hon
da': {'Model': 'civic', 'year': 2007, 'price': 5000, 'condition': 'precertified'}}

copied cars dict {'benz': {'Model': 'ML350', 'year': 2015, 'price': 55000, 'condition': 'precertified'}, 'bmw': {'Model': '750i', 'year': 2010, 'price': 35000, 'condition': 'not-certified'
}, 'Honda': {'Model': 'civic', 'year': 2007, 'price': 5000, 'condition': 'precertified'}}
the poped item from cars {'Model': 'civic', 'year': 2007, 'price': 5000, 'condition': 'precertified'}
the poped itsm is 78
"""