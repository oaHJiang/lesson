from venv import create
import mysql.connector

#print(mysql.connector.apilevel)
#print(mysql.connector.paramstyle)

conn=mysql.connector.connect(user='root',password='password',database='jianghao')
cursor=conn.cursor()
cursor.execute('create table lesson(\
    id varchar(20) PRIMARY KEY, \
    name varchar(20) )')
cursor.close()
conn.close()