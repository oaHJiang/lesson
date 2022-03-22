#访问控制
#类型，__xxx__,(系统)
#_xxx(保护)
#__xxx(私有)
class people:
    def __init__(self,name,age):
        self.name=name
        self.__age=age#加入__使self.age无法在外部直接使用，只能使用setage
    def show(self):
        print('我的名字是',self.name)
        print('我的年龄是',self.__age)
    def setage(self,age):
        if age<=0:
            print('请重新设置')
        else:
            self.__age=age
    def getage(self):
        print('我的年龄是',self.__age)

zhangsan=people('张三',18)
zhangsan.show()

zhangsan.setage(24)
zhangsan.show()

zhangsan.age=-42#此时age和__age无关
zhangsan.show()
print(zhangsan.age)

zhangsan.__age=-42
zhangsan.show()
print(zhangsan.__age)

#__age私有变量，实现了隐蔽
#无论是age访问还是__age访问，都无法访问类内部的__age
#实现了高级封装
#若一定要访问，方式为：对象._类名__属性，如：
#zhangsan._people__age
#访问类内部的私有成员是非常不建议的

zhangsan._people__age=-42
zhangsan.show()