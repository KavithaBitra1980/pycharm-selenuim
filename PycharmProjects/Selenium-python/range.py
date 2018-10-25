#range Demo
list1 = []
print(list(range(0,10)))

num = int(input ('enter a number'))
print(type(num))

for i in range(1,10):
   print(num,'*',i,'=',num*i)



"""
RESULTS
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
enter a number10
<class 'int'>
10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
10 * 6 = 60
10 * 7 = 70
10 * 8 = 80
10 * 9 = 90

Process finished with exit code 0
"""