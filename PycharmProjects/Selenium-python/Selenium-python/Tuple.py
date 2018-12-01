# Demo OF Tuple

tuple1 = (1, 2, 3)
print(tuple1)

# tuple[0]=0  ==>doesn't support
print(tuple1[0:2])

# Tuple with string and number
tstr = ('kavitha', 'ann', 'chad', 90, 89, 70,'kavihta70')
list1 = ['kavitha', 'ann', 'chad', 90, 89, 70]
print(tstr[-1])

print(tstr[::-1])
print(list1)
print(list1.pop())
print(tstr.index(90))
print(tstr.count(70))

#print(tstr.pop)====>no pop

"""
************************************Results************************

(1, 2, 3)
(1, 2)
kavihta70
('kavihta70', 70, 89, 90, 'chad', 'ann', 'kavitha')
['kavitha', 'ann', 'chad', 90, 89, 70]
70
3
1

"""
