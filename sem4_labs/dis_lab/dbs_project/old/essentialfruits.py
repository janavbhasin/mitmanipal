import sqlite3

class Fruits:
    def __init__(self, cur, conn):
        self.cur = cur
        self.conn = conn
    
    def create_table(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS essential_fruits(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fruit1 VARCHAR(10) NOT NULL,
            fruit2 VARCHAR(10) NOT NULL,
            fruit3 VARCHAR(10) NOT NULL,
            fruit4 VARCHAR(10) NOT NULL,
            fruit5 VARCHAR(10) NOT NULL,
            fruit6 VARCHAR(10) NOT NULL
        );
        ''')

    def fill_fruits(self, bmi_value):
        fruits_mapping = {
            '<25': ['avocado', 'orange', 'pumpkin', 'watermelon', 'kiwi', 'apple'],
            '25-30': ['mango', 'strawberry', 'dragon-fruit', 'guava', 'blueberry', 'raspberry'],
            '>30': ['litchi', 'pineapple', 'prunes', 'dates', 'grape', 'banana']
        }

        for a in bmi_value:
            if a < 25:
                bmi_category = '<25'
            elif a >= 25 and a <= 30:
                bmi_category = '25-30'
            else:
                bmi_category = '>30'

            fruits = fruits_mapping.get(bmi_category, [])
            if fruits:
                self.cur.execute('INSERT INTO essential_fruits (fruit1, fruit2, fruit3, fruit4, fruit5, fruit6) VALUES (?, ?, ?, ?, ?, ?)', fruits)
                self.conn.commit()

    def read_bmi_from_database(self):
        self.cur.execute("SELECT bmi FROM stat")
        bmi_values = self.cur.fetchall()
        print('hi')
        print(bmi_values)
        return bmi_values