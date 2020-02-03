import pymysql.cursors
connect = pymysql.Connect(
    host='192.168.111.138',
    port=3306,
    user='root',
    db='test',
    charset='utf8'
)
# 事务处理
sql_1 = "UPDATE teat SET saving = saving + 1000 WHERE user_id = '1001' "
sql_2 = "UPDATE teat SET expend = expend + 1000 WHERE user_id = '1001' "
sql_3 = "UPDATE teat SET income = income + 2000 WHERE user_id = '1001' "
cur=connect.cursor()
try:
    cur.execute(sql_1)  # 储蓄增加1000
    cur.execute(sql_2)  # 支出增加1000
    cur.execute(sql_3)  # 收入增加2000
except Exception as e:
    connect.rollback()  # 事务回滚
    print('事务处理失败', e)
else:
    connect.commit()  # 事务提交
    print('事务处理成功', cur.rowcount)

# 关闭连接
cur.close()
connect.close()