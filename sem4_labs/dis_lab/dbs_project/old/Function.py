import sqlite3

class function:
    def __init__(self, cur,conn):
        self.conn = conn
        self.cur = cur

    def create_function(self):
        self.cur.execute('''CREATE FUNCTION IF NOT EXISTS assign_proteins(mealpref TEXT) RETURNS TEXT
            BEGIN
                DECLARE protein1 TEXT;
                DECLARE protein2 TEXT;
                DECLARE protein3 TEXT;

                IF mealpref = 'Non-Veg' THEN
                    SET protein1 = 'chicken';
                    SET protein2 = 'fish';
                    SET protein3 = 'egg';
                ELSEIF mealpref = 'Veg' THEN
                    SET protein1 = 'paneer';
                    SET protein2 = 'soya';
                    SET protein3 = 'chia seeds';
                ELSE
                    SET protein1 = 'tofu';
                    SET protein2 = 'quinoa';
                    SET protein3 = 'hemp seeds';
                END IF;

                RETURN protein1 || ',' || protein2 || ',' || protein3;
            END;
        ''')
        self.conn.commit()

    def create_trigger(self):
        self.cur.execute('''
            CREATE TRIGGER IF NOT EXISTS insert_proteins
            AFTER INSERT ON user
            FOR EACH ROW
            BEGIN
                UPDATE user SET proteins = assign_proteins(NEW.mealpref) WHERE id = NEW.id;
            END;
        ''')
        self.conn.commit()

    def close(self):
        self.conn.close()