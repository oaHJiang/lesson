#改进，能够适应不同格式参数
def funx(*args,**kwargs):
    print(args,kwargs)
funx(1,2,3,kj=99,我我我=666)
funx(1)
funx(jh=8)
def decorator(func):
    def wrapper(*args,**kwargs):
        print('========')
        x=func(*args,**kwargs)
        print(x)
        print('---------')
        return x
    return wrapper
@decorator #调用装饰器，相当于decorator(myadd)
def myadd(a,b):
    return a+b
@decorator 
def mysubstract(a,b):
    return a-b
@decorator    
def mymultiply(a,b):
    return a*b
@decorator     
def mydivide(a,b):
    return a/b
@decorator
def myadd3(a,b,c):
    return a+b+c
myadd(3,4)
print(myadd(3,4))
print(myadd3(3,4,5))
print(mysubstract(3,4))
print(mymultiply(3,4))
print(mydivide(3,4))
''''''