from rich import print
import time
import os
from datetime import datetime
import random
import string
import sqlite3

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
        print("[bold green]User '{}' and '{}' inserted successfully.[/bold green]".format(username, password))
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
        self.insert_random_users(10)

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
            print("[bold red]Invalid date format. Please use YYYY-MM-DD format.[/bold red]")
            return
        print('[bold]For Gravies please enter one of the following RAJMA,KADHI,PANEER,POTATO,CHICKEN,OMLETE,FISH[/bold]')
        lis=[ 'RAJMA','KADHI','PANEER','POTATO','CHICKEN','OMLETE','FISH']
        gravy1 = input('Enter first meal gravy: ') 
        while gravy1 not in lis:
            print('[bold red]Invalid choice[/bold red]')
            time.sleep(0.3)
            gravy1 = input('Enter first meal gravy: ')
        gravy2 = input('Enter second meal gravy: ')
        while gravy2 not in lis:
            print('[bold red]Invalid choice[/bold red]')
            time.sleep(0.3)
            gravy2 = input('Enter second meal gravy: ')
        gravy3 = input('Enter third meal gravy: ')
        while gravy3 not in lis:
            print('[bold red]Invalid choice[/bold red]')
            time.sleep(0.3)
            gravy3 = input('Enter third meal gravy: ')
        print('[bold]For Breads please enter one of the following ROTI,WHITE_BREAD,BROWN_BREAD,RICE[/bold]')
        lis=['ROTI','WHITE_BREAD','BROWN_BREAD','RICE']
        bread1 = input('Enter first meal bread: ')
        while bread1 not in lis:
            print('[bold red]Invalid choice[/bold red]')
            time.sleep(0.3)
            bread1 = input('Enter first meal bread: ')
        bread2 = input('Enter second meal bread: ')
        while bread2 not in lis:
            print('[bold red]Invalid choice[/bold red]')
            time.sleep(0.3)
            bread2 = input('Enter second meal bread: ')
        bread3 = input('Enter third meal bread: ')
        while bread3 not in lis:
            print('[bold red]Invalid choice[/bold red]')
            time.sleep(0.3)
            bread3 = input('Enter third meal bread: ')
        self.cur.execute('''
            INSERT INTO logs (log_date, username, GRAVY1, GRAVY2, GRAVY3, BREAD1, BREAD2, BREAD3) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (log_date, username, gravy1, gravy2, gravy3, bread1, bread2, bread3))
        self.conn.commit()

    def options(self):
        print('[bold]Choose any option below:[/bold]\n'
            '[1] Insert User\n'
            '[2] Display User\n'
            '[3] Insert Log\n'
            '[4] Display Calories Consumed\n'
            '[5] Insert Allergies\n'
            '[6] Display Allergies\n'
            '[7] Display Proteins\n'
            '[8] Display BMI\n'
            '[9] Display Fruits\n'
            '[10] Display All\n'
            '[11] Delete User\n'
            '[12] Exit\n'
            '[13] Display calorie from date to date\n'
            '[14] Display what i should have\n')
        option = int(input("Enter your choice: "))
        self.choose(option)

    def choose(self, option):
        if option!=12:
            username=self.login()
        if option == 1:
            if self.checks(username):
                print('[bold red]User already exists![/bold red]')
            else:
                password = input("Enter password: ")
                email = input("Enter email: ")
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                height = float(input("Enter height in cm: "))
                weight = float(input("Enter weight in kg: "))
                mealpref = input("Enter meal preference: ")
                sex = input("Enter sex: ")
                mobile_no = int(input("Enter mobile number: "))
                self.insert_2_user((username, password, email, name, age, height, weight, mealpref, sex, mobile_no))
                self.options()
        elif option == 2:
            self.display_user(username)
            self.display_bmi(username)
            self.display_fruits(username)
            self.display_proteins(username)
            self.display_allergies(username)
            self.print_user_meals(username)
            self.display_specific_calories(username)
            self.options()
        elif option == 3:
            self.insert_log(username)
            self.options()
        elif option == 4:
            self.display_specific_calories(username)
            self.options()
        elif option == 5:
            self.insert_into_allergies(username)
            self.options()
        elif option == 6:
            self.display_allergies(username)
            self.options()
        elif option == 7:
            self.display_proteins(username)
            self.options()
        elif option == 8:
            self.display_bmi(username)
            self.options()
        elif option == 9:
            self.display_fruits(username)
            self.options()
        elif option == 10:
            self.display_all(username)
            self.options()
        elif option == 11:
            self.delete_user(username)
            self.options()
        elif option == 12:
            self.delete_database_file()
            print("[bold red]Database file deleted successfully![/bold red]")
            exit()
        elif option==13:
            self.execute_calories_query(username)
            self.options()
        elif option==14:
            self.execute_user_details_query(username)
            self.options()
        else:
            print("[bold red]Invalid Option![/bold red]")
            self.options()

    def execute_calories_query(self,username):
        date1=input('Enter start date: ')
        date2=input('Enter final date: ')
        self.cur.execute("""
            SELECT username, SUM(total_calories) AS total_calories_consumed
            FROM calories_consumed
            WHERE username=? AND log_date BETWEEN ? AND ?
            GROUP BY username;
        """,(username,date1,date2))
        results = self.cur.fetchall()
        for row in results:
            print("Username:", row[0])
            print("Total Calories Consumed:", row[1])

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.cur.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password))
        user = self.cur.fetchone()
        if user:
            print("[bold green]Login successful![/bold green]")
            return username
        else:
            print("[bold red]Invalid username or password![/bold red]")

    def execute_user_details_query(self,username):
        self.cur.execute("""
            SELECT u.username, u.email, u.age, u.height, u.weight, f.fruit1, f.fruit2, f.fruit3, f.fruit4, f.fruit5, f.fruit6, p.p1, p.p2, p.p3
            FROM user u
            LEFT JOIN essential_fruits f ON u.id = f.id
            LEFT JOIN essential_proteins p ON u.id = p.id
            WHERE u.username=?;
        """,(username,))
        results = self.cur.fetchall()
        for row in results:
            print("Username:", row[0])
            print("Email:", row[1])
            print("Age:", row[2])
            print("Height:", row[3])
            print("Weight:", row[4])
            print("Fruits:", row[5:11])
            print("Proteins:", row[11:])

    def delete_user(self, username):
        self.cur.execute('''DELETE FROM user WHERE username = ?''', (username,))
        self.conn.commit()
        print("[bold green]User '{}' deleted successfully.[/bold green]".format(username))

    def print_user_meals(self, username):
        self.cur.execute('SELECT * FROM logs WHERE username=?;', (username,))
        rows = self.cur.fetchall()
        for row in rows:
            print(f"Date: {row[0]}, Gravy1: {row[2]}, Gravy2: {row[3]}, Gravy3: {row[4]}, Bread1: {row[5]}, Bread2: {row[6]}, Bread3: {row[7]}")

db = Database('user_data.db')
