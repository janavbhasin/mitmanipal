import sqlite3
import time
import os
from datetime import datetime
import random
import string
from rich import print

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cur = self.conn.cursor()
        self.create()
        self.this = []
        self.options()

    def create_food_calories_table(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS food_calories (
                food_name VARCHAR(50) PRIMARY KEY,
                calorie_count INTEGER NOT NULL
            );
        ''')
        self.conn.commit()

    def insert_2_user(self, user_data):
        username, password, email, name, age, height, weight, mealpref, sex, mobile_no = user_data
        self.cur.execute('''
            INSERT INTO user (username, password, email, name, age, height, weight, mealpref, sex, mobile_no)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', (username, password, email, name, age, height, weight, mealpref, sex, mobile_no))
        self.conn.commit()
        print(f"User '{username}'and '{password}' inserted successfully.")
        self.read_bmi_from_database(username)

    def generate_random_data(self, num_tuples):
        random_data = []
        for _ in range(num_tuples):
            username = ''.join(random.choices(string.ascii_lowercase, k=5))  
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))  
            email = username + "@example.com"  
            name = ''.join(random.choices(string.ascii_lowercase, k=8))  
            age = random.randint(18, 60)  
            height = random.randint(150, 200) 
            weight = random.randint(50, 100)  
            mealpref = random.choice(['Veg', 'Non-Veg', 'Vegan'])
            sex = random.choice(['Male', 'Female'])  
            mobile_no = ''.join(random.choices(string.digits, k=10))  
            random_data.append((username, password, email, name, age, height, weight, mealpref, sex, mobile_no))
        return random_data

    def insert_random_users(self, num_users):
        random_data = self.generate_random_data(num_users)
        for user_data in random_data:
            self.insert_2_user(user_data)

    def insert_food_calories(self):
        food_calories = [
            ('RAJMA', 120),
            ('KADHI', 250),
            ('PANEER', 265),
            ('POTATO', 87),
            ('CHICKEN', 165),
            ('OMLETE', 78),
            ('FISH', 206),
            ('ROTI', 71),
            ('WHITE_BREAD', 70),
            ('BROWN_BREAD', 55),
            ('RICE', 130)
        ]
        self.cur.executemany('INSERT INTO food_calories (food_name, calorie_count) VALUES (?, ?)', food_calories)
        self.conn.commit()
    
    def create_calories_consumed_table(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS calories_consumed (
                username VARCHAR(20) NOT NULL,
                log_date DATE NOT NULL,
                total_calories INTEGER,
                PRIMARY KEY (username, log_date),
                FOREIGN KEY (username) REFERENCES logs(username),
                FOREIGN KEY (log_date) REFERENCES logs(log_date)
            );
        ''')
        self.conn.commit()

    def create_trigger3(self):
        self.cur.execute('''
            CREATE TRIGGER IF NOT EXISTS calculate_calories_trigger
            AFTER INSERT ON logs
            FOR EACH ROW
            BEGIN
                INSERT INTO calories_consumed (username, log_date, total_calories)
                VALUES (NEW.username, NEW.log_date,
                    (SELECT SUM(calorie_count) 
                     FROM food_calories 
                     WHERE food_name IN (NEW.GRAVY1, NEW.GRAVY2, NEW.GRAVY3, NEW.BREAD1, NEW.BREAD2, NEW.BREAD3))
                );
            END;
        ''')
        self.conn.commit()

    def display_specific_calories(self, username):
        self.cur.execute('''
            SELECT log_date, total_calories 
            FROM calories_consumed 
            WHERE username = ?;
        ''', (username,))
        rows = self.cur.fetchall()
        for row in rows:
            print(f"Date: {row[0]}, Total Calories: {row[1]}")

    def read_bmi_from_database(self, username):
        self.cur.execute("SELECT bmi FROM stats,user where username=? and stats.id=user.id;", (username,))
        bmi_value = self.cur.fetchone()
        self.fill_fruits(bmi_value)
    
    def drop_trigger(self):
        self.cur.execute("DROP TRIGGER IF EXISTS calculate_bmi_trigger;")

    def delete_database_file(self):
        self.conn.close()  
        os.remove(self.db_file)

    def create_user(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS user(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(20) NOT NULL UNIQUE,
            password VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            name VARCHAR(100) NOT NULL,
            age INTEGER NOT NULL,
            height NUMERIC(2,1) NOT NULL,
            weight NUMERIC(5,2) NOT NULL,
            mealpref VARCHAR(50) NOT NULL,
            sex VARCHAR(10) NOT NULL,
            mobile_no INTEGER NOT NULL,
            CONSTRAINT valid_sex CHECK(sex IN ('Male', 'Female')),
            CONSTRAINT valid_mealpref CHECK(mealpref IN ('Veg', 'Non-Veg', 'Vegan')),
            CONSTRAINT PW_len CHECK(length(password) >= 8))''')

    def checks(self, username):
        self.cur.execute('''SELECT * FROM user WHERE username=?;''', (username,))
        return bool(self.cur.fetchone())

    def display_user(self,username):
        self.cur.execute('SELECT * FROM user WHERE username=?;', (username,))
        print(self.cur.fetchone())
    
    def display_all(self, username):
        self.display_user(username)
        self.display_bmi(username)
        self.display_fruits(username)
        self.display_proteins(username)
        self.display_allergies(username)
        self.print_user_meals(username)
        self.display_specific_calories(username)

    def create_bmi(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS stats(
            id INTEGER not null primary key autoincrement,
            bmi NUMERIC(2) not null,
            CONSTRAINT universal_id FOREIGN KEY(id) REFERENCES user(id) on delete cascade on update cascade);''')

    def create_trigger1(self):
        self.cur.execute('''
            CREATE TRIGGER IF NOT EXISTS calculate_bmi_trigger
            AFTER INSERT ON user
            FOR EACH ROW
            BEGIN
                INSERT INTO stats (bmi) VALUES (ROUND(NEW.weight / (((NEW.height / 100.0) * (NEW.height / 100.0))), 0));
            END;
        ''')
        self.conn.commit()

    def display_bmi(self, username):
        self.cur.execute('''SELECT bmi FROM stats,user WHERE username=? and stats.id=user.id;''', (username,))
        print(self.cur.fetchone())
    
    def create_fruits(self):
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

    def display_fruits(self, username):
        self.cur.execute('SELECT fruit1,fruit2,fruit3,fruit4,fruit5,fruit6 from essential_fruits,user where username=? and user.id=essential_fruits.id;', (username,))
        print(self.cur.fetchone())
    
    def create_proteins(self):
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
    
    def create_trigger2(self):
        self.cur.execute('''
            CREATE TRIGGER IF NOT EXISTS insert_proteins
            AFTER INSERT ON user
            FOR EACH ROW
            BEGIN
                INSERT INTO essential_proteins (id, p1, p2, p3) VALUES 
                (NEW.id, 
                 CASE 
                     WHEN NEW.mealpref = 'Non-Veg' THEN 'chicken'
                     WHEN NEW.mealpref = 'Veg' THEN 'paneer'
                     WHEN NEW.mealpref = 'Vegan' THEN 'tofu'
                 END,
                 CASE 
                     WHEN NEW.mealpref = 'Non-Veg' THEN 'fish'
                     WHEN NEW.mealpref = 'Veg' THEN 'soya'
                     WHEN NEW.mealpref = 'Vegan' THEN 'quinoa'
                 END,
                 CASE 
                     WHEN NEW.mealpref = 'Non-Veg' THEN 'egg'
                     WHEN NEW.mealpref = 'Veg' THEN 'chia seeds'
                     WHEN NEW.mealpref = 'Vegan' THEN 'hemp seeds'
                 END);
            END;
        ''')
        self.conn.commit()

    def display_proteins(self, username):
        self.cur.execute('SELECT p1,p2,p3 FROM user,essential_proteins where username=? and essential_proteins.id=user.id;', (username,))
        print(self.cur.fetchone())

    def create_allergies(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS allergies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(20) NOT NULL,
            allergy VARCHAR(50) NOT NULL,
            CONSTRAINT fk_user FOREIGN KEY (username) REFERENCES user(username) ON DELETE CASCADE
        );
        ''')
        self.conn.commit()

    def insert_into_allergies(self, username):
        while True: 
            allergy = input('Enter the allergy name one by one if done enter Exit: ')
            if allergy == 'Exit':
                break
            self.insert_allergies(username, allergy)

    def insert_allergies(self, username, allergy):
        self.cur.execute('INSERT INTO allergies (username, allergy) VALUES (?, ?)', (username, allergy))
        self.conn.commit()

    def display_allergies(self, username):
        self.cur.execute('SELECT allergy FROM allergies WHERE username=?;', (username,))
        print(self.cur.fetchall())

    def create_logs(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS logs(
                log_date DATE NOT NULL,
                username VARCHAR(10) NOT NULL,
                GRAVY1 VARCHAR(10) NOT NULL,
                GRAVY2 VARCHAR(10) NOT NULL,
                GRAVY3 VARCHAR(10) NOT NULL,
                BREAD1 VARCHAR(10) NOT NULL,
                BREAD2 VARCHAR(10) NOT NULL,
                BREAD3 VARCHAR(10) NOT NULL,
                PRIMARY KEY (log_date, username),
                CONSTRAINT g1 CHECK(GRAVY1 IN ('RAJMA','KADHI','PANEER','POTATO','CHICKEN','OMLETE','FISH')),
                CONSTRAINT g2 CHECK(GRAVY2 IN ('RAJMA','KADHI','PANEER','POTATO','CHICKEN','OMLETE','FISH')),
                CONSTRAINT g3 CHECK(GRAVY3 IN ('RAJMA','KADHI','PANEER','POTATO','CHICKEN','OMLETE','FISH')),
                CONSTRAINT b1 CHECK(BREAD1 IN ('ROTI','WHITE-BREAD','BROWN-BREAD','RICE')),
                CONSTRAINT b2 CHECK(BREAD2 IN ('ROTI','WHITE-BREAD','BROWN-BREAD','RICE')),
                CONSTRAINT b3 CHECK(BREAD3 IN ('ROTI','WHITE-BREAD','BROWN-BREAD','RICE'))
            );
        ''')
        self.conn.commit()
    
    def insert_log(self, username):
        log_date_input = input("Enter the log date (YYYY-MM-DD): ")
        try:
            log_date = datetime.strptime(log_date_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")
            return
        print('For Gravies please enter one of the following RAJMA,KADHI,PANEER,POTATO,CHICKEN,OMLETE,FISH')
        lis=[ 'RAJMA','KADHI','PANEER','POTATO','CHICKEN','OMLETE','FISH']
        gravy1 = input('Enter first meal gravy: ') 
        while gravy1 not in lis:
            print('Invalid choice')
            time.sleep(0.3)
            gravy1 = input('Enter first meal gravy: ') 
        gravy2 = input('Enter second meal gravy: ')
        while gravy2 not in lis:
            print('Invalid choice')
            time.sleep(0.3)
            gravy2 = input('Enter second meal gravy: ') 
        gravy3 = input('Enter third meal gravy: ')
        while gravy3 not in lis:
            print('Invalid choice')
            time.sleep(0.3)
            gravy3 = input('Enter third meal gravy: ') 
        print('For Bread please enter one of the following ROTI,WHITE-BREAD,BROWN-BREAD,RICE')
        lis=['ROTI','WHITE-BREAD','BROWN-BREAD','RICE']
        bread1 = input('Enter the first bread: ')
        while bread1 not in lis:
            print('Invalid choice')
            time.sleep(0.3)
            bread1 = input('Enter the first bread: ')
        bread2 = input('Enter the second bread: ')
        while bread2 not in lis:
            print('Invalid choice')
            time.sleep(0.3)
            bread2 = input('Enter the second bread: ')
        bread3 = input('Enter the third bread: ')
        while bread3 not in lis:
            print('Invalid choice')
            time.sleep(0.3)
            bread3 = input('Enter the third bread: ')
        self.cur.execute('''
            INSERT INTO logs (log_date, username, GRAVY1, GRAVY2, GRAVY3, BREAD1, BREAD2, BREAD3)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (log_date, username, gravy1, gravy2, gravy3, bread1, bread2, bread3))
        self.conn.commit()

    def insert_into_logs(self, username):
        while True: 
            exit_msg = input('If you want to stop entering the meal logs type Exit: ')
            if exit_msg == 'Exit':
                break
            self.insert_log(username)
    
    def print_user_meals(self, username):
        self.cur.execute('''
            SELECT log_date, GRAVY1, GRAVY2, GRAVY3, BREAD1, BREAD2, BREAD3
            FROM logs
            WHERE username=?
        ''', (username,))
        user_meals = self.cur.fetchall()
        if user_meals:
            print(f"Meals eaten by {username}:")
            for meal in user_meals:
                print(meal)
        else:
            print(f"No meals found for username: {username}")

    def create(self):
        self.create_user()
        self.create_bmi()
        self.create_logs()
        self.create_allergies()
        self.create_trigger1()
        self.create_trigger2()
        self.create_fruits()
        self.create_proteins()
        self.create_food_calories_table()
        self.insert_food_calories()
        self.create_calories_consumed_table()
        self.create_trigger3()
        self.insert_random_users(5)

    def passwordcheck(self, username):
        self.cur.execute('''SELECT password FROM user WHERE username=?;''', (username,))
        return self.cur.fetchone()

    def insert_user(self):
        username = input('Enter username: ')
        if self.checks(username):
            print('Username already exists')
            time.sleep(0.5)
            return
        password = input('Enter password: ')
        while len(password) < 8:
            print('Invalid password')
            time.sleep(0.5)
            password = input('Enter password:')
        email = input('Enter email: ')
        name = input('Enter name: ')
        age = input('Enter age: ')
        while not age.isdigit():
            print("Age must be a number")
            time.sleep(0.5)
            age = input('Enter age: ')
        height = input('Enter height: ')
        while not height.isdigit():
            print("Height must be a number")
            time.sleep(0.5)
            height = input('Enter height: ')
        weight = input('Enter weight: ')
        while not weight.isdigit():
            print("Weight must be a number")
            time.sleep(0.5)
            weight = input('Enter weight: ')
        mealpref = input('Enter meal preference (Veg/Non-Veg/Vegan): ')
        while mealpref.lower() not in ['veg', 'non-veg', 'vegan']:
            print('Invalid meal preference')
            time.sleep(0.5)
            mealpref = input('Enter meal preference (Veg/Non-Veg/Vegan): ')
        sex = input('Enter sex (Male/Female): ')
        while sex.lower() not in ['male', 'female']:
            print('Invalid sex')
            time.sleep(0.5)
            sex = input('Enter sex (Male/Female): ')
        mobile_no = input('Enter mobile number: ')
        while len(mobile_no) < 10:
            print('Invalid mobile number')
            time.sleep(0.5)
            mobile_no = input('Enter mobile number:')
        self.cur.execute('INSERT INTO user (username, password, email, name, age, height, weight, mealpref, sex, mobile_no) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);',
                        (username, password, email, name, age, height, weight, mealpref, sex, mobile_no))
        self.read_bmi_from_database(username)
        self.insert_into_allergies(username)
        self.insert_into_logs(username)
        self.conn.commit()
        self.options()

    def options(self):
        choice = input('ENTER YOUR CHOICE\nLogin \nSign Up\n\n')
        if choice.lower() == 'login':
            self.login()
        elif choice.lower() == 'sign up':
            self.insert_user()
        else:
            print('Invalid Choice')
            time.sleep(0.3)
            self.options()
   
    def login(self):
        username = input('Enter Username: ')
        if not self.checks(username):
            print('Username does not exist')
            time.sleep(0.3)
            self.login()
        password = self.passwordcheck(username)[0]  
        passw=input('Enter password')
        while password != passw:
            print('Invalid password')
            time.sleep(0.3)
            passw = input('Enter password')
        self.main_page(username)
    
    def delete(self, username):
        self.this.append(username)

    def insert_into_tables(self, username):
        choice = input('ENTER THE VALUE YOU WANT TO INSERT\nMeal Logs\nAllergies\n\n')
        if choice.lower() == 'meal logs':
            self.insert_into_logs(username)
        elif choice.lower() == 'allergies':
            self.insert_into_allergies(username)
        else:
            print('Invalid Choice')
            time.sleep(0.3)
            self.insert_into_tables(username)
    
    def delete_menu(self, username):
        choice = input('ENTER THE VALUE YOU WANT TO DELETE\nUser\nAllergies\nLogs\n\n')
        if choice.lower() == 'user':
            self.delete(username)
        elif choice.lower() == 'allergies':
            self.delete_allergies(username)
        elif choice.lower() == 'logs':
            self.delete_logs(username)
        else:
            print('Invalid Choice')
            time.sleep(0.3)
            self.delete_menu(username)
    
    def delete_allergies(self, username):
        allergy = input('Enter the allergy you want to delete: ')
        self.cur.execute('DELETE FROM allergies WHERE username=? AND allergy=?', (username, allergy))
        self.conn.commit()
    
    def delete_logs(self, username):
        log_date_input = input("Enter the log date you want to delete (YYYY-MM-DD): ")
        try:
            log_date = datetime.strptime(log_date_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")
            return
        self.cur.execute('DELETE FROM logs WHERE username=? AND log_date=?', (username, log_date))
        self.conn.commit()

    def main_page(self, username):
        while True:
            choice = input('ENTER YOUR CHOICE\nInsert\nDisplay\nDelete\nQuit\nLog Out\n\n')
            if choice.lower() == 'insert':
                self.insert_into_tables(username)
            elif choice.lower() == 'display':
                self.display_all(username)
            elif choice.lower() == 'delete':
                self.delete_menu(username)
            elif choice.lower()=='log out':
                self.options()
            elif choice.lower() == 'quit':
                print('Exiting...')
                time.sleep(0.5)
                break
            else:
                print('Invalid Choice')
                time.sleep(0.3)
    
    
    
db = Database('health_db.sqlite')
