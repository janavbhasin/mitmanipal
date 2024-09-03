import sqlite3
class user:
    def __init__(self,cur,conn):
        self.conn=conn
        self.cur=cur


    def create_table(self):
        self.cur.execute('''
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        name VARCHAR(100) NOT NULL,
        age INTEGER NOT NULL,
        height NUMERIC(3,1) NOT NULL,
        weight NUMERIC(5,2) NOT NULL,
        mealpref VARCHAR(50) NOT NULL,
        sex VARCHAR(10) NOT NULL,
        mobile_no INTEGER NOT NULL,
        CONSTRAINT valid_sex CHECK(sex IN ('Male','Female')),
        CONSTRAINT PW_len check(length(password)>=8),
        CONSTRAINT valid_mealpref CHECK(mealpref IN ('Veg','Non-Veg','Vegan')))
    ''')


    def insert(self,username,password,email,name,age,height,weight,mealpref,sex,mobile_no):
        self.cur.execute('''INSERT INTO user (username,password,email,name,age,height,weight,mealpref,sex,mobile_no)VALUES(?,?,?,?,?,?,?,?,?,?);'''(username,password,email,name,age,height,weight,mealpref,sex,mobile_no))
        self.conn.commit()


    def delete(self,username):
        self.cur.execute('''DELETE FROM user WHERE username=?;'''(username))
        self.conn.commit()


    def updateweight(self,username,weight):
        self.cur.execute('''UPDATE user SET weight=? WHERE username=?;'''(weight,username))
        self.conn.comit()


    def updateheight(self,username,height):
        self.cur.execute('''UPDATE user SET height=? WHERE username=?;'''(height,username))
        self.conn.comit() 

        
    def authenticate(self, username, password):
        self.cur.execute('''
            SELECT * FROM REGISTER WHERE username=? and password=?;''', (username, password))

        if self.cur.fetchone():
            return True
        else:
            return False


    def select(self, username):
        self.cur.execute('''
            SELECT * FROM REGISTER WHERE username=?;''', (username,))

        if self.cur.fetchone():
            return True
        else:
            return False