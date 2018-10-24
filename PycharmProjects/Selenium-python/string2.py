# learing string functins len(),lower(0,upper(),capitalize,split,replace string

str1 = "Hi, Welcome to the world of python. Good luck Kavitha"
str2 = "THIS IS TO TREST STRING IN LOWER CASE---->SEE ALL LOWER"

print(len(str1))
print('the Length of the string %s is' % (len(str2)))
print('the Lower case of the string %s is' % (str2.lower()))
print('the upper case of the string {} is'.format(str1.upper()))

print(len(str1))
print('the Length of the string %s is %s' % (str1, len(str2)))
print('the Lower case of the string %s is %s' % (str2, str2.lower()))
print('the upper case of the string {} is  {}'.format(str1, str1.upper()))
print('.............')

"""
RESULTS--->
53
the Length of the string Hi, Welcome to the world of python. Good luck Kavitha is 55
the Lower case of the string THIS IS TO TREST STRING IN LOWER CASE---->SEE ALL LOWER is this is to trest string in lower case---->see all lower
the upper case of the string Hi, Welcome to the world of python. Good luck Kavitha is  HI, WELCOME TO THE WORLD OF PYTHON. GOOD LUCK KAVITHA

"""

print('capitalication')
print(str1.capitalize() , str2.capitalize())

"""
Results-->
.............
capitalication
Hi, welcome to the world of python. good luck kavitha This is to trest string in lower case---->see all lower

"""

str3 = 'this is my 2nd python class, i am glad i am doing good, hope this works for me'
print('split example')
print(str3.split("."))
print(str3.split())
IPAdress = '10.10.10.10'
print(IPAdress.split('.'))

"""
This will creates a list
RESULT-->['this is my 2nd python class, i am glad i am doing good, hope this works for me']
['this', 'is', 'my', '2nd', 'python', 'class,', 'i', 'am', 'glad', 'i', 'am', 'doing', 'good,', 'hope', 'this', 'works', 'for', 'me']
['10', '10', '10', '10']
"""

print(str3.replace('a','@'))


