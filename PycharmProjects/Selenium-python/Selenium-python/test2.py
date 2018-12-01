def oddNumbers(l,r):

    while l<=r:
        if l %2 == 1:
            print(l)
            l=l+1


print('the odd numbers between 2 and 5 are')
l=2
r=5
oddNumbers(l,r)