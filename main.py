import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import psycopg2 as pg2

class Database:
    def __init__(self, db, username, password, port):
        self.db = db
        self.username = username
        self.password = password
        self.port = port
        self.conn = pg2.connect(database= self.db, user=self.username, password= self.password, port= self.port)
        self.cur = self.conn.cursor()
    def close(self):
        self.cur.close()
        self.conn.close()
    def execute_query(self,query):
        self.cur.execute(query)
        self.conn.commit()
    def getone_execute(self,query):
        self.cur.execute(query)
        return self.cur.fetchone()
    def getall_execute(self,query):
        self.cur.execute(query)
        return self.cur.fetchall()

class loginScreen(Widget):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    
   
    def submitBtn(self):
        db = Database(db='watchify',username='postgres',password='password',port=5433)
    
        try:
            
            #isUserValid = db.getone_execute('SELECT user_name,user_pass FROM my_user WHERE user_name =%s AND user_pass =%s'%(username,password))
            users = db.getall_execute('SELECT user_name,user_pass FROM my_user')
            
            for user_name,user_pass in users:
                if user_name == self.username.text and user_pass == self.password.text:
                    print('Welcome %s'%(self.username.text))
                else:
                    print('Wrong pass')
            """
            if isUserValid != '' :
                print('Welcome %s'%(self.username.text))
            else:
                print('Wrong password')
            """
       
            self.username.text = ''
            self.password.text = ''
        except Exception as e:
            print(e)
    

class MyApp(App):
    def build(self):
        return loginScreen()


if __name__ =='__main__':
    MyApp().run()        