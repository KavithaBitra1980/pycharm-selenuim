# Learning strings indexing

string1 = "this is my new program is to learn is indexing"
string2 = 'thisamitgonnacoolguy'
number1 = '128.10.11.11'
print(string1[0])
print(string1[0:15])
print(string1[0:-7])
print(string1[0:-7:2])
print(string2[0::4])
print(string1[::-1])
print(len(number1))
split1 = number1.split('.')
print(split1[2])
if split1[3] > '10':
    print(split1[3],split1[2])

#Find
print('using find')
print(number1.find('.'))
print(number1[3])
print(number1[::-1])

print(string1.find('is',6))
print(string1.index("in"))
print(string1[38])

"""
RESULTS======>
t
this is my new
this is my new program is to learn is i
ti sm e rga st er si
tagal
gnixedni si nrael ot si margorp wen ym si siht \\\\\\reverse of a string
11
11 11
using find
3
.
11.11.01.821
23
38
i

"""
