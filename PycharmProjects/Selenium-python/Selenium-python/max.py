#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'


#list = [2,3,3,3,1]

#max = max(list)
#print(list.count(max))

#print(max)

#for i in list:
    #if  count(i) >1:
       # print(i)

def birthdayCakeCandles(ar):
    #max_num=0
    print(ar)
    max_num = max(ar)
    #max_count = ar.count(max_num)
    return (ar.count(max_num))



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('Birthday.txt',"w")

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()