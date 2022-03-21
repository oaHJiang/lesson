#封装
class person:
    def __init__(self,name,age):
        print('===初始化开始===')
        self.name=name
        self.age=age
        print('===初始化结束===')
    def show(self):
        print('我的名字是:',self.name)
        print('我的年龄是:',self.age)  #封装
zhangsan=person('张三',18)
zhangsan.show()
