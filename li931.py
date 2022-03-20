#列表，元组，集合，字典，字符串等对象被称为可迭代对象
x=['我哦哦','cff','jjf']
print(type(x))
for a in x:
    print(a,end=" ") 
#迭代器
i=iter(x)
print(next(i))
print(next(i))
print(next(i))
#生成器
def gen(n):
    for i in range(n):
        yield i*i
x=gen(6)
for i in x:#遍历
    print(i,end=" ")
print(type(x))
#简化
gen=(i*i for i in range(5))
for i in gen:
    print(i)
from ctypes import sizeof
import sys
import time
a=time.time()
f=[k for k in range(10000000)]
b=time.time()
print(b-a)
print(sys.getsizeof(f))
c=time.time()
j=(k for k in range(10000000))
d=time.time()
print(d-c)
print(sys.getsizeof(j))