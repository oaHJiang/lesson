import mysql.connector
conn=mysql.connector.connect(user='root',password='password',database='jianghao')
cursor=conn.cursor()
'''#构造表
cursor.execute('create table lesson(\
    id varchar(20) PRIMARY KEY, \
    name varchar(20) )') 
'''
#主键不能重复
'''
cursor.execute('insert into lesson(id,name) values(%s,%s)', ['001','张三'])#插入
cursor.execute('insert into lesson(id,name) values(%s,%s)', ['002','李四'])
cursor.execute('insert into lesson(id,name) values(%s,%s)', ['003','王五'])

conn.commit()#提交
'''
#查询

cursor.execute('select * from lesson')
values=cursor.fetchall()
for x in values:
    print(x)

cursor.close()
conn.close()


