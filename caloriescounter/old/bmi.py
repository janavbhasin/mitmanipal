import sqlite3
class stat:
    def __init__(self,cur,conn):
        self.conn=conn
        self.cur=cur
    def create_table(self):
        self.cur.execute('''
            CREATE TABLE  if not exists stat(
            id INTEGER not null primary key autoincrement,
            username VARCHAR(10)not null,
            bmi NUMERIC(3,1)not null,
            CONSTRAINT universal_id FOREIGN KEY(id) REFERENCES user(id) on delete cascade on update cascade);
            ''')
    def insert(self,username, bmi):
        self.cur.execute('''INSERT INTO stat (username,bmi) VALUES(?);''',(username, bmi))
        self.conn.commit()
    def delete(self, username):
        self.cur.execute('''DELETE FROM stat WHERE username=?;''', (username))
        self.conn.commit()
    def select(self, name):
        self.cur.execute('''SELECT user.username,bmi from stat WHERE username=?;''', (name))
        return self.cur.fetchone()