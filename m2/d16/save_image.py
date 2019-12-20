import pymysql
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset = 'utf8')
cur = db.cursor()

f = open('./cat.jpg','rb')
data = f.read()
f.close()
try:
    sql = 'update cls set image = %s where id =1;'
    cur.execute(sql,[data])
    db.commit()
    print('commit')
except:
    db.rollback()
    print('rollback')

sql = 'select image from cls where id =1;'
cur.execute(sql)
data = cur.fetchone()
with open('./cat_copy','wb') as f:
    f.write(data[0])

cur.close()
db.close()
