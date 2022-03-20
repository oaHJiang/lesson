#闭包
def balance(jin,yuan):
    return (jin-0.1)*yuan
banana=balance(5.1,4)
print(banana)
print(balance(2.1,5))
#函数里有函数
#内函数用外函数的变量
#外函数的返回值是内函数
def dianzicheng(danjia):
    def jisuan(maozhong):
        return (maozhong-0.1)*danjia
    return jisuan
pingguo=dianzicheng(3)
#pingguo等价于
# def jisuan(maozhong):
    # return (maozhon-0.1)*3
print(pingguo(10.1))
xiangjiao=dianzicheng(5)
print(xiangjiao(6.1))

def com(n):
    def ji(x):
        if n=='pingfang':
            return x*x
        elif n=='lifang':
            return x*x*x
    return ji
a=com('pingfang')
b=com('lifang')
print(a(3))
print(b(4))