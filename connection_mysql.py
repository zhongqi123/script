import pymysql
#连接数据库
conn=pymysql.connect(host="192.168.111.138",user='root',password='',port=3306,db='zabbix',charset='utf8')
#对数据库进行操作
cur = conn.cursor()   #生成游标

sql="select * from users;"     #执行操作语句，若多行可用''' '''隔开
cur.execute(sql)  #执行SQL语句
for i in cur.fetchall():
    print(i[:])

cur.close    #关闭游标
conn1=pymysql.connect(host="192.168.111.138",user='root',password='',port=3306,charset='utf8')
cur1=conn1.cursor()
cur1.execute("create database zq;")    #多条执行命令
cur1.execute("show databases;")

print(cur1.fetchall())
cur1.close