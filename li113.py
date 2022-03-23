#f.write('Hello,world!')
'''
file='lesson.txt'
with open(file,mode='w',encoding='utf-8') as f:
    f.write('张三66')
'''
'''
file='lesson2.txt'
with open(file,mode='r+',encoding='utf-8') as f:
    f.write('222') #r+,打开文件，在文件开头写，完成替换
'''
file='lesson2.txt'
with open(file,mode='w+',encoding='utf-8') as f:
    f.write('3333') #w+,打开文件，删除原内容，从头开始写
'''
#writelines() 向文件写入一序列的字符串或字节串，序列可以是列表，元组，字典，集合等
x=open('lesson.txt','r')
y=open('lesson3.txt','w')
y.writelines(x.readlines())
x.close
y.close
'''
from datetime import datetime
file='lesson4.txt'
with open(file,'w') as f:
    dt=datetime.strptime('2022/3/22','%Y/%m/%d')
    print(dt)
    result=str('time:'+str(dt.date()))
    f.write(result)