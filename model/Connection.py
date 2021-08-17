from logging import fatal
from model.MDbLog import MDbLog
import sqlite3
import asyncio
from sqlite3 import Error
from sqlite3.dbapi2 import connect

class Connection:
    global conn
    def _createVersion(self,nameVersion):
        print(self.conn)
        
        cur = self.conn.cursor()
        cur.execute("INSERT INTO LOG (name_version) VALUES ({nameversion})".format(nameversion= nameVersion))
        cur.close()
        self.conn.commit()
       
        
    def create_connection(self,db_file):
        # create connection with sqlite3
        
        try:
            self.conn = sqlite3.connect(db_file,check_same_thread=False)
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
       
    def create_log(self,dataHash):
        result = False
        try:
            cur = self.conn.cursor()
            print ("INSERT INTO LOG (name_version , link_version , decreption_version) VALUES ({nVs},{lVs}, {dVs})".format(nVs= dataHash.name_version , lVs= dataHash.link_version, dVs =dataHash.decreption_version ))
            cur.execute("INSERT INTO LOG (name_version , link_version , decreption_version) VALUES ({nVs},{lVs}, {dVs})".format(nVs= dataHash.name_version , lVs= dataHash.link_version, dVs =dataHash.decreption_version ))
            self.conn.commit()
            result = True
        except Error as e:
            print(e)
            result = False
        return result

    def check_version(self, _version):
        result = False
        try:
             cur = self.conn.cursor()
             query= "SELECT *  from LOG where name_version = '{nV}'".format(nV= _version)
             print(query)
             cur.execute(query)
             record= cur.fetchall()
             print(record)
             cur.close()
             if len(record) == 0:
                result= True
             else:
                result = False
        except Error as e:
            print(e)
            result = False
        return result

    def get_version_by_name(self,_vesion):
        result = MDbLog
        try:
             cur = self.conn.cursor()
             query= "SELECT *  from LOG where name_version = '{nV}'".format(nV= _vesion)
             print(query)
             cur.execute(query)
             record= cur.fetchone()
             print(record)
             cur.close()
             result = record
        except Error as e:
            print(e)
            result = False
        return result

    def __init__(self):
        self.conn = None
        self.create_connection('./db/logVerionDB.db')

      

    
