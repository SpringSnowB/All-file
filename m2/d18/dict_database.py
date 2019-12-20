import pymysql


class DictDatabase:
    def __init__(self,host='localhost',port=3306,database=None,user=None,password=None,charset='utf8'):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.charset = charset
        self.connect_db()

    def connect_db(self):
        self.db = pymysql.connect(host = self.host,
                     port = self.port,
                     database = self.database,
                     user = self.user,
                     password = self.password,
                     charset = self.charset
                     )

    def create_cur(self):
        self.cur = self.db.cursor()

    def search_user(self,name):
        sql = "select name from users where name =%s;"
        self.cur.execute(sql, [name])
        result = self.cur.fetchone()
        if result:
            return True
        return False

    def search_passwd(self,name,passwd):
        sql = "select passwd from users where name = %s;"
        self.cur.execute(sql,[name])
        result = self.cur.fetchone()
        if result:
            return True
        return False


    def insert_user(self,name, passwd):
        try:
            sql = "insert into users(name,passwd) values(%s,%s);"
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def insert_search(self,name,word):
        try:
            sql = "insert into search(name,word) values(%s,%s);"
            self.cur.execute(sql, [name, word])
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False

    def search_word(self,word):
        sql = "select mean from words where word =%s;"
        self.cur.execute(sql, [word])
        result = self.cur.fetchone()
        if result:
            return result[0]


    def search_history(self,name):
        sql = "select name,word,search_time from search where name = %s order by search_time desc limit 10;"
        self.cur.execute(sql, [name])
        return self.cur.fetchall()
