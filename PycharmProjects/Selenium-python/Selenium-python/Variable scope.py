#Demo of Variable Scope

a= 50

def demo_variable():
    global a
    print('the local demo value is',a)
    a= 25
    print('the value in method is',a)

print('the global variable value is',a)
demo_variable()

num = 50

def evenorodd():
    global num
    if num % 2== 0:
        return 'Even'
    else:
        return 'Odd'

print(evenorodd())