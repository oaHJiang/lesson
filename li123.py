
from sqlalchemy import Column, create_engine,String,INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#表连接
Base=declarative_base()#基类
class math(Base):
    __tablename__='math'
    id=Column(String(20),primary_key=True)
    name=Column(String(20))
    ms=Column(INTEGER)
#数据库连接
engine=create_engine('mysql+mysqlconnector://root:password@localhost:3306/score')
DBSession=sessionmaker(bind=engine)
session=DBSession()
'''
zhangsan=math(id='001',name='张三',ms=88)
lisi=math(id='002',name='李四',ms=66)
wangwu=math(id='003',name='王五',ms=99)

session.add(zhangsan)
session.add(lisi)
session.add(wangwu)

session.commit()
session.close()
'''
#查询

x=session.query(math.id,math.name,math.ms)
for i in x:   #x类型为列表，其元素为元组
    print(i)
session.close()



