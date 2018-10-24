'''
# arthimetic operators

num1 = 10
num2 = 20
num3 = 30
print(" Addition of two number Num1 + Num2=", num1+num2)
print(" Subtraction of two number Num1 - Num2=", num1-num2)
print(" multiplication of twu number Num1 + Num2=", num1*num2)
print(" Division of twu number Num1 + Num2=", num1/num2)

#num1 = 5
#num2 = 2
print(" modulous of twu number Num1 + Num2=", num1 % num2)
print('5 exponent of 4', 5 ** 4)
print(" 22//7", 22//7)
print("4.2//2", 4.2//2.0)


#Assignment Operators

num3= num1 + num2
print(num3)
num3+=num1
print(num3)
#print(num4)
print(num3)
print(num2)


#Comparison Operators
print("num3 > num2", num3 > num2)
print("num2 == num3", num2 == num3)
print("num1 != num2", num1 != num2)


#Logical Operators
x=True
y=False

print((x and y))
print(x and x)
print(x or y)

#Bitwise operators
num4 = 6 #110
num5 = 7 #111

print('bitwise', num4 & num5)
print('bitwise',num4 | num5)
print('bitwise',num4 ^ num5)


print(num4 >> 2)
print(num5 << 2)

# List operators

x=[1,2,3,4,5]
y=[10,20,30,40]
#y=[1 to 100]

print(1 in (x and y))
#print(99 in y)

print(9.8 - 8.777)

x=["k","a","vi","tha"]

print("k" in x)

'''
s1="Python"
s2="learner"

#Contactination

print(s1+s2)

#Repetitation

print(s1*3)

#Slicing
print("newone")
print(s1[2:7])
print(s2[:4])
print(s1[0:-4])
print(s2[0:-2])
print(s2[2:-4])
