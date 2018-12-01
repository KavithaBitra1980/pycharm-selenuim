# while ,break Demo

x=1
while x<=10:
    print(x)
    x=x+1
print('while done')

l = [1,2,3]
l.append(10)
print(l)
print('.....................append while............')

list1 = [1,2]
num = 0
while num <=10:
    num = num + 1
    list1.append(num)
    #print('the last number is',list1[-1])

print(list1)
"""
#####Results
1
2
3
4
5
6
7
8
9
10
while done
[1, 2, 3, 10]
.....................append while............
[1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
"""

#Break

num = 1
while num <10 :
    print(num)
    num+=1
    if (num==5):
        print('*'*20)
        break

print('the break number is' ,num)

print('....................................')
num = 1
while num <=10:
    print(num * '*')
    num+=1
print(num)

print('**************************')

num = 1
while num<10:
    print(num * '*')
    num+=1
    if num==5:
        print(num * '..')
        print('its a break')
        break

#..............Continue
print('now with continue')
num = 1
while num<10:
    print(num * '*')
    num+=1
    if num==5:
        print('its awesome')
        continue

"""
1
2
3
4
5
6
7
8
9
10
while done
[1, 2, 3, 10]
.....................append while............
[1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
1
2
3
4
********************
the break number is 5
....................................
*
**
***
****
*****
******
*******
********
*********
**********
11
**************************
*
**
***
****
..........
its a break
now with continue
*
**
***
****
its awesome
*****
******
*******
********
*********

Process finished with exit code 0

"""