"""
通过程序描述登录、注册过程，将其各封装为一个函数
"""
import pymysql
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'uses')
cur = db.cursor()


def find_name(name):
    sql_name = 'select name from uses where name=%s;'
    cur.execute(sql_name, [name])
    if cur.fetchone():
        return True
    return False


def login(name,passwd):
    if not find_name(name):
        return '用户未注册'
    cur.execute('select passwd from uses where name ="%s";'%name)
    if passwd ==cur.fetchone()[0]:
        return '登录成功'
    return '密码错误，登录失败'


def register(name,passwd):
    if find_name(name):
        return '用户名已存在'
    try :
        sql = 'insert into users(name,passwd) values(%s,%s);'
        cur.execute(sql,[name,passwd])
        db.commit()
        return '注册成功'
    except:
        db.rollback()
        return '注册失败'