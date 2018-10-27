# Built in Functions max(),min(),abs(),type()
args = [-0.001,2,3,1,2,5,8,9,90,67,45.9889,7.567,-9.9980]
num1= -19.890

#print(max(list1),min(list1))

def largest_num(args):
    return(max(args))

def smallest_num(args):
    return (min(args))

def abs_num(num1):
    return abs(num1)

def Type_value(num1):
    return type(num1)


print(largest_num(args))
print(smallest_num(args))
print(abs_num(num1))
print(Type_value(num1))

