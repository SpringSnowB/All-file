import pymysql
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset = 'utf8')
cur = db.cursor()

# 组合SQL语句
# name = input("请输入你要查询的姓名：")
# sql = 'select name,hobby from interest where name = "%s";'%name
# cur.execute(sql)

sql = 'select name,age,sex from cls where age >%s and sex =%s;'
cur.execute(sql,[18,'m'])
print(cur.fetchall())