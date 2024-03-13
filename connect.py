import mysql.connector
import os
from dotenv import load_dotenv


'''
This is a connection class, it loads some .env variables and calls to
a database. Variables are stored in a .env file for privacy reasons.
When this class is initiated it connects to the database and creates
a cursor object. This object is used to execute any sql code that you would
need. As long as the values are passed in as text it should go through.
I havent done rigorous testing with this its old code from sophomore year
its just a proof of concept to the the ball rolling

'''


class Connect:
    def __init__(self):
        load_dotenv()
        self.db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            passwd=os.getenv("DB_PASSWD"),
            database=os.getenv("DB_DATABASE"),
            port=os.getenv("DB_PORT")
        )
        self.cur = self.db.cursor()
    
    def select_query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def execute(self, sql):
        self.cur.execute(sql)