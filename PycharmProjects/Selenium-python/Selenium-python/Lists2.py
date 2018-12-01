# Learning lists with for loop range,Pop

number = [88,89]
for i in range (90,100):
    number.append(i)
print(number)

#Demo of pop()

print('the poped number is',number.pop())
print('the number basket or list is',number)


print('the poped number is',number.pop())
print('the number basket or list is',number)

print(len(number))

number2 = [70,71]
for i in range (72,79):
    number2.append(i)
print(number2)

#List concatination

print('the concatinationof two numbers is')
number3 = (number+number2)
print(number3.pop())
print(len(number+number2))
print(len(number3))

###To check an item exists in IN key words

teams1 = ["VAteam","Marylandteam","NCteam","DCteam","SCteam"]
print(teams1)

print("SCteam" in teams1)
print("ACteam" in teams1)


teams2 = ["MAteam","Maineteam","CTteam","WVteam","NJteam"]
print(teams2)

print("SCteam" in teams2)
print("ACteam" in teams2)

print("AZteam" in teams1+teams2)
print("AZteam" not in teams1+teams2)

teams3 = teams1 + teams2
print('all teams are',teams3)

teams3[0] = 'NJteam'
print('all teams are',teams3)

######GUESS A NUMBER GAME

picklist = [1,2]
for i in range(3,20):
    picklist.append(i)
print('the pick list is',picklist)
guess = int(input("enter a number from 1 to 20:"))

if guess in picklist :
    print('wow...awesome u have entered %s is in the list %s' %(guess,picklist))
else:
    print('SORRY you didnt WIN.. u have entered %s is NOT in the list %s' % (guess, picklist))


a='this is mylife'
print(a.split())


a="am"

b="language"

print("I" + a +"love" +b)

l=[1, 2, 3, 2, 1, 2]

print(l.count(2))

list1 = ['k','l','k','o','p','k']
print(list1.count('k'))

print(l[4:6])
