#继承
class guaishou:#父类
    def shout(self):
        print('嗷嗷嗷嗷嗷')
class fei(guaishou):#子类,继承shout
    def fly(self):
        print('飞飞飞飞')
class you(guaishou):
    def swim(self):
        print('游游游游')
class pao(guaishou):
    def run(self):
        print('跑跑跑跑')

jiatannie=guaishou()#省略self
jiatannie.shout()

feishou=fei()
feishou.shout()
feishou.fly()

youshou=you()
youshou.shout()
youshou.swim()

paoshou=pao()
paoshou.shout()
paoshou.run()




