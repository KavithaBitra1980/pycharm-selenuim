# Learning LISTS

Fruit1 = 'Apple'
Fruit2 = 'Banana'
Fruit3 = 'Orange'


print('My favorite Fruit1 is ',Fruit1)
print('My favorite Fruit2 is',Fruit2)
print('My favorite Fruit3 is',Fruit3)

#Using Lists

print('----------------------------------')
FruitBasket = ['Apple','Orange','Banana','Cherries',10,20,2.567,True,False]

print('My favorite Fruits are ',FruitBasket[3])
print('My favorite Fruits are ',FruitBasket[-1])


#Adding or appending the list
FruitBasket.append('Grapes')
print(len(FruitBasket))
print('My favorite Fruits are in the list ',FruitBasket)
#Display's last item in the list
print('My favorite Fruits are ',FruitBasket[-1])
#Displays list in reverse order
print('My favorite Fruits are ',FruitBasket[::-1])

print('My favorite Fruits are ',FruitBasket[1:-1])

#displays string in reverse order
string1='this is my firs program'
print(string1[::-1])

#Palyndrome
str='manam'
print(str[::-1])

"""
RESULTS===========================>
My favorite Fruits are  Cherries
My favorite Fruits are  False
10
My favorite Fruits are in the list  ['Apple', 'Orange', 'Banana', 'Cherries', 10, 20, 2.567, True, False, 'Grapes']
My favorite Fruits are  Grapes
My favorite Fruits are  ['Grapes', False, True, 2.567, 20, 10, 'Cherries', 'Banana', 'Orange', 'Apple']
My favorite Fruits are  ['Orange', 'Banana', 'Cherries', 10, 20, 2.567, True, False]
margorp srif ym si siht
manam

"""