#demo for multiplelists using ZIP

l1 = [1,2,3]
l2 = [3,4,5,10,20,30]
l3 = [5,10,15,20,25]

for a,b in zip(l1,l2):
    print('the multiplication of both matrixes is',2*(a*b))

for a,b,c in zip(l1,l2,l3):

    print(a,b,c)
    if a < b and a <c and b < c:
        print(a ,'is the smallest')
        print(c, 'is the largest')
        print(b, 'is larger than ', a)




"""
RESULTS
the multiplication of both matrixes is 6
the multiplication of both matrixes is 16
the multiplication of both matrixes is 30
1 3 5
1 is the smallest
5 is the largest
3 is larger than  1
2 4 10
2 is the smallest
10 is the largest
4 is larger than  2
3 5 15
3 is the smallest
15 is the largest
5 is larger than  3

"""