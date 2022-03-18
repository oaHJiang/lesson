import re


def fun(x):
    return x*x
x=[0,1,55,312,4,5,6,774,85,9]
y=map(fun,x)
print(list(y))
print(type(y))
from functools import reduce
def max(x,y):
    return x if x>y else y
y=reduce(max,x)
print(y)
z=[1,2,3,4,5,6]
def jiecheng(x,y):
    return x*y
c=reduce(jiecheng,z)
print(c)

