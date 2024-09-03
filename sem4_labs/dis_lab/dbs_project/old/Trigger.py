import sqlite3

class trigger:
    def __init__(self, cur, conn):
        self.conn = conn
        self.cur = cur

    def create_trigger(self):
        self.cur.execute('''
            CREATE TRIGGER IF NOT EXISTS calculate_bmi_trigger
            AFTER INSERT ON user
            FOR EACH ROW
            BEGIN
                INSERT INTO bmi (username, bmi) VALUES (NEW.username, NEW.weight / ((NEW.height / 100) * (NEW.height / 100)));
            END;
        ''')
        self.conn.commit()

    def drop_trigger(self):
        self.cur.execute("DROP TRIGGER IF EXISTS calculate_bmi_trigger;")
        self.conn.commit()
