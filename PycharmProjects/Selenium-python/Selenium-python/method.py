#### Methods


def sum_num():
    print(3 + 2)

sum_num()

print('............................................')
""""def mulplication_table(num):
    for i in range(1,10):
        print(i,'*',num,'=',i*num)

num =  (input('enter a number'))

mulplication_table(num)
"""
print('................................')

def sum_nums(n1,n2):
    print(n1+n2)

sum_nums(5,6)

def largest2(a,b):
    if a > b:
        print(a, 'is the largest')
        print(b,'is smallest')
    else:
        print(b, 'is the largest')
        print(a, 'is smallest')

largest2(21,29)

def arithmetic(a,b):
    print('performing operation on',a,b)
    print('addition',a+b)
    print('subtraction',a-b)
    print('multiplicaion',a*b)
    print('division',a/b)
    print('remainder',a%b)
    print('quotient',a//b)
    print('power',a**b)

for i in range (1,4):
    a=int(input('enter a\n'))
    b=int(input('enter b\n'))
    arithmetic(a,b)

print('=================================methods with return')




