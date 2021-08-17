import sqlite3
import asyncio
from sqlite3 import Error

class Connection:
    global conn
    def _createVersion(self,nameVersion):
        print(self.conn)
        
        cur = self.conn.cursor()
        cur.execute("INSERT INTO LOG (name_version) VALUES ({nameversion})".format(nameversion= nameVersion))
        self.conn.commit()
       
        
    def create_connection(self,db_file):
        # create connection with sqlite3
        
        try:
            self.conn = sqlite3.connect(db_file)
            # print(sqlite3.version)
            self.conn.execute('''CREATE TABLE LOG
         (ID INTEGER PRIMARY KEY AUTOINCREMENT     NOT NULL,
         name_version           TEXT    NOT NULL,
         link_version           TEXT     ,
         decreption_version     TEXT,
         date_create            TEXT);''')
            print("Table created successfully")
            self.conn.close()
        except Error as e:
            print(e)
       

    
    def __init__(self):
        self.conn = None
        self.create_connection('./db/logVerionDB.db')

      

    
