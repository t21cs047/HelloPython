'''
Created on 2023/10/13

@author: t21cs047
'''
print("Hello, Python world")

a = 10
b = 0.000001
c = 'string'
print(a,b,c)

for x in {1,2,3}:
    print(x)
    
if 0 < x < 10:
    print ('0<x<10')
else:
    print('x<=0,x>=10')

p = 0
while p<10:
    print('p=',p)
    p += 1

import math

print(type(math))
print(math)
print (math.pi)

from fibonacci import fibo

print(fibo(20))


from quicksort import quick_sort

data = [5,3,1,2,8,6,7,9,4,10]

print( quick_sort(data))


