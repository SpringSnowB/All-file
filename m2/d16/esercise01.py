"""
创建数据库 dict
数据库中创建数据表 words
包含 id word mean
将dict.txt中的单词插入到这个数据库中，
插入结果必须在98%以上为成功
"""

import pymysql
import re
db = pymysql.connect(user = 'root',
                     password ='123456',
                     database = 'dict')

cur = db.cursor()

f = open('./dict.txt')
data_list =[]
for line in f:
    data = re.findall(r'(\S+)\s+(.*)',line)
    print(data)
    data_list.extend(data)

f.close()
sql = 'insert into words(word,mean) values(%s,%s);'

try:
    cur.executemany(sql,data_list)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()

