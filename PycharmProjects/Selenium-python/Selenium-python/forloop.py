# for loop demo

str1 = 'kavitha is a good girl'

for i in str1:
    print(i, end=" ")
print('\n')
for x in str1:
    if x=='a':
        print('@',end=" ")
    else:
        print(x,end=' ')

cars = ['Honda','bmw','benz']
print('\n',cars)

for car in cars:
    print(car)

num1 = [1,2,3,4,5]
for n in num1:
    print((n*10))

#################MULTIPLICATION TABLE
number = int(input('enter a number '))
i = 1
mul = 1
print('the %dS table is'%(number))
while i <= 10:
#
    mul = i * number
    print(i ,'*' ,number ,'=',mul)
   # print(mul)
    i+=1

######With dicts
d = {'one':1,'two':2,'three':3}
for k in d:
    print(k + ' ' + str(d[k]))
print('......')
for m,n in d.items():
    print(m,n)
    #print(n)

print('......cars....')

cars = {'benz':{'Model':'ML350','year':2015,'price':55000,'condition':'precertified'},
        'bmw': {'Model': '750i', 'year': 2010, 'price': 35000, 'condition': 'not-certified'},
        'Honda': {'Model': 'civic', 'year': 2007, 'price': 5000, 'condition': 'precertified'}}

for style1,style2 in cars.items():
    print('the car company is ',style1 + 'All details ',style2)

"""
RESULTS
k a v i t h a   i s   a   g o o d   g i r l 

k @ v i t h @   i s   @   g o o d   g i r l 
 ['Honda', 'bmw', 'benz']
Honda
bmw
benz
10
20
30
40
50

"""