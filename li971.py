#假修饰器
#每次调用必须调用假修饰器的名称
#将实际函数作为参数
#无法直接使用实际函数完成计算
def show(fun,a,b):
    print('=========')
    x=fun(a,b)
    print(x)
def myadd(a,b):
    return a+b
def mysubstract(a,b):
    return a-b
def mymultiply(a,b):
    return a*b
def mydivide(a,b):
    return a/b
show(myadd,3,4)
show(mysubstract,3,4)
show(mymultiply,3,4)
show(mydivide,3,4)
#修饰器
#实际函数名=修饰器函数名
def Show(func):
    def temp(x,y):
        print('========')
        z=func(x,y)
        return z
    return temp
myadd=Show(myadd)
mysubstract=Show(mysubstract)
mymultiply=Show(mymultiply)
mydivide=Show(mydivide)
print(myadd(3,4))
print(mysubstract(3,4))
print(mymultiply(3,4))
print(mydivide(3,4))

