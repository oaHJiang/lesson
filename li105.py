#多态
'''
class people:
    def talk(self):
        print('Hello,大家好！！！')
class teacher(people):
    def talk(self):
        print('同学们好！！！')
class student(people):
    pass
zhangsan=people()
lisi=teacher()
zhangsan.talk()
lisi.talk()
'''

class people:
    def talk(self):
        print('Hello,大家好！！！')
class teacher(people):
    def talk(self):
        print('同学们好！！！')
class student(people):
    def talk(self):
        print('老师好！！！')        
def starttalk(people):
    print('====准备====')
    people.talk()#这里teacher和student也属于people类
    print('====结束====')
#isinstance(x,type)判断x是否为type，返回TRUE or FALSE
lisi=teacher()#lisi创建为teacher类
lisi.talk()
starttalk(lisi)

zhangsan=people()
starttalk(zhangsan)

#新加类
class doctor(people):
    def talk(self):
        print('你怎么了？')

wangwu=doctor()
starttalk(wangwu)