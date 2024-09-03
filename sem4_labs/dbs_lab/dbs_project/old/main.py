from old.database import Database 
import time
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.prompt import Prompt, IntPrompt, FloatPrompt
class Nutridash:
    def __init__(self,db_file='NutriDash_Database.db'):
        self.db=Database(db_file)
        self.console = Console(force_interactive=True, width=128, color_system='auto')
        self.heading = Panel(Text('NUTRI DASH', justify='full', style='bold magenta reverse'),
                             style='bold magenta reverse', border_style='bold magenta')


    def page_heading(self, heading, style='bold italic white', end='.'):
        self.console.clear()
        self.console.print(Align(self.heading, align='center', style='magenta reverse'))

        page_heading = Panel(Text(f'{heading}{end}', justify='center', style=style),
                             style=style)
        self.console.print(Align(page_heading, align='center', style=style))


    def home_page(self):
        self.console.clear()
        self.console.print(Align(self.heading, align='center', style='magenta reverse'))
        self.page_heading('What would you like to do', end='?')
        choice = Prompt().ask(choices=['Login', 'Register', 'Exit'], default='Exit')
        if choice == 'Login':
            self.log_page()
        elif choice == 'Register':
            self.register_page()
        else:
            exit()

    def register_page(self):
        self.console.clear()
        self.console.print(Align(self.heading, align='center', style='magenta reverse'))
        self.page_heading('Registration. Create an account.')
        username = Prompt().ask('Username')
        if self.db.User.select(username):
            rprint('[bold red]Username already exists![/]')
            time.sleep(0.5)
            self.register_page()
        email = Prompt().ask('Email')
        password = Prompt().ask('Password', password=True)
        confirm_password = Prompt().ask('Confirm Password', password=True)
        name=Prompt().ask('name: ',name=True)
        age=Prompt().ask('age: ',age=True)
        height=Prompt().ask('height: ',height=True)
        weight=Prompt().ask('weight: ',weight=True)
        mealpref=Prompt().ask('meal preference [Veg,Non-Veg,Vegan]: ',mealpref=True)
        sex=Prompt().ask('sex: ',sex=True)
        mobile_no=Prompt().ask('mobile number: ',mobile_no=True)
        if password == confirm_password:
            self.db.User.insert(username,password,email,name,age,height,weight,mealpref,sex,mobile_no)
            rprint('[bold green]Successfully registered![/bold green]')
            time.sleep(2)
            self.user_details_page()
        else:
            rprint('[bold red]Passwords do not match![/]')
            time.sleep(2)
            self.register_page()


    def log_page(self):
        self.console.print(Align(self.heading, align='center', style='magenta reverse'))
        self.page_heading('Login')
        username = Prompt.ask('Username')
        password = Prompt.ask('Password', password=True)
        if self.db.User.authenticate(username,password):
            self.main_page(username=username)
        else:
            print('Invalid username')
            time.sleep(2)
            self.log_page()


    def main_page(self,username=False,name=False):
        self.console.clear()


    def run(self):
        #self.db.delete_database()
        self.db.create_database()
        self.home_page()

        
if __name__=='__main__':
    Nutridash().run()