import sqlite3

class EssentialProteins:
    def __init__(self,cur,conn):
        self.conn = conn
        self.cur = cur

    def create_table(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS essential_proteins(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                p1 VARCHAR(10) NOT NULL,
                p2 VARCHAR(10) NOT NULL,
                p3 VARCHAR(10) NOT NULL,
                CONSTRAINT universal FOREIGN KEY(id) REFERENCES user(id) ON DELETE CASCADE ON UPDATE CASCADE
            )
        ''')
        self.conn.commit()