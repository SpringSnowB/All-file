import pymysql

#连接数据库
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset = 'utf8')

#产生游标对象
cur = db.cursor()

#利用游标对象执行各种SQL语句
#读操作 -->fetch系列函数    select语句
sql = "select name from cls where sex='m';"
cur.execute(sql)

#遍历游标对象，获取查询记录
# for i in cur:
#     print(i)

print(cur.fetchone())#获取一个查询结果
# print(cur.fetchmany(4))#获取若干个查询结果，如果输入参数大于所有结果数，会返回所有结果
# print(cur.fetchall())#获取所有结果


#写操作 -->commit   rollbakc系列操作
# try:
#     # sql = "insert into cls values(7,'xd',17,'w',57);"
#     # cur.execute(sql)
#
#     # sql = 'insert into cls values(%s,%s,%s,%s,%s)'
#     # cur.execute(sql,[8,'ou',19,'m',84])
#
#     # sql = 'update cls set name =%s where name=%s;'
#     # cur.execute(sql,['pc','pp'])
#
#     # sql = 'delete from cls where id =8;'
#     # cur.execute(sql)
#
#     #通过executemany执行大量的sql语句
#     list_ = [('ui',5),('pi',6),('oi',7)]
#     sql = 'update cls set score =score+3,name=%s where id =%s;'
#     cur.executemany(sql,list_)
#     db.commit() #提交结果，立即刷新缓冲区，将数据写入数据库

# except Exception as e:
#     print(e)
#     db.rollback()#回滚，没有写入数据库的操作召回

#关闭游标和数据库
cur.close()
db.close()