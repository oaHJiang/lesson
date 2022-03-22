#msg=f.read(N)逐个读取字节或字符，有参数时，读取参数个字节或字符
'''
with open('file.txt','r',encoding='UTF-8') as f:
    x=f.read(6)
    print(x)
'''
#readline()逐行读取
'''
with open('file.txt','r',encoding='UTF-8') as f:
    x=f.readline()
    print(x)      #读到一行，包括结果的换行，print又换行，多个换行
    #解决：print(x,end="")
    #或者x.strip() 去掉末尾的'\n'
'''
'''
with open('file.txt','r',encoding='UTF-8') as f:
    x=f.readline()
    print(x,end="") 
#readlines(),一次读取多行
'''
'''
with open('file.txt','r',encoding='UTF-8') as f:
    x=f.readlines()
    print(x)
    for i in x:
        print(i,end="")
'''        
from datetime import datetime
file='file.txt'
with open('file.txt','r',encoding='UTF-8') as f:
    for line
