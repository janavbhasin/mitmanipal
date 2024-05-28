from old.essentialfruits import Fruits
from old.bmi import stat
from old.Trigger import trigger
from old.User import user
from old.essentialproteins import EssentialProteins
from old.Function import function
import sqlite3
class Database:
    def __init__(self,db_file):
        self.db_file=db_file
        self.conn=sqlite3.connect(self.db_file)
        self.cur=self.conn.cursor()
        self.fruits=Fruits(self.cur,self.conn)
        self.bmi=stat(self.cur,self.conn)
        self.User=user(self.cur,self.conn)
        self.func=function(self.cur,self.conn)
        self.proteins=EssentialProteins(self.cur,self.conn)
        self.trig=trigger(self.cur,self.conn)
    def create_database(self):
        self.User.create_table()
        self.bmi.create_table()
        self.trig.create_trigger()
        self.fruits.create_table()
        #self.fruits.fill_fruits(self.fruits.read_bmi_from_database())
        self.proteins.create_table()
        self.func.create_function()
        self.func.create_trigger()
        self.conn.commit()
    def delete_database(self):
        #self.cur.execute("DROP FUNCTION IF EXISTS assign_proteins;")
        self.trig.drop_trigger()
        self.cur.execute("DROP TABLE IF EXISTS user;")
        self.cur.execute("DROP TABLE IF EXISTS bmi;")
        self.cur.execute("DROP TABLE IF EXISTS essential_fruits;")
        self.cur.execute("DROP TABLE IF EXISTS essential_protein;")
        self.cur.execute("DROP TABLE IF EXISTS logs;")
        self.conn.commit()