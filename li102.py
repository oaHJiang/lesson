#object oriented progamming,面向对象
class people:
    def __init__(selff,name,height):#selff为对象,可以无初始化函数
        print('初始化')
        selff.name=name
        selff.height=height
    def cry(selff):#方法
        print('呜呜呜呜呜o(╥﹏╥)o')   
#创建对象
zhangsan=people('张三','70kg')#zhangsan为变量名(对象)，张三为属性(name),省略self
print(zhangsan.name)
print(zhangsan.height)
zhangsan.cry()

lisi=people('李四','60kg')
print(lisi.name)
print(lisi.height)
lisi.cry()
