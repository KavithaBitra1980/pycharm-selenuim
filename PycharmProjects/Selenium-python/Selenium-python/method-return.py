#demo of Method-return

def sum_nums(n1,n2):
    return n1+n2

def evenorodd(n1):
    if n1 % 2 == 0:
        return 'even'
    else:
        return 'odd'

def isMetro(city):
    city_list = ['DC','NewYork','SFO','Greater Huston']
    if city in city_list:
        return 'yes Its a metro'
    else:
        return 'Sorry not in the list'


"""def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2


def arithmetic(n1,n2):

    add(n1,n2)
    sub(n1,n2)
    mul(n1,n2)
print('executing arithmetic', arithmetic(n1, n2))
"""


#sum1 = sum_nums(5,6)
n1 = int(input('enter n1\n'))
n2 = int(input('enter n2\n'))

print( 'executing sum_nums method',sum_nums(n1,n2))

print( 'executing sum_nums method',sum_nums('one','two'))

print('.........even or odd...........')
print('the number is', evenorodd(n1))

for i in range(1,3):
    city = input('enter a city name\n')
    print('is my city in the list?...let me check....',isMetro(city))


""" 
enter n1
23
enter n2
34
executing sum_nums method 57
executing sum_nums method onetwo
.........even or odd...........
the number is odd
enter a city name
DC
is my city in the list?...let me check.... yes Its a metro
enter a city name
boaton
is my city in the list?...let me check.... Sorry not in the list
"""

