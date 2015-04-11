
import sqlite3

conn = sqlite3.connect('worksheet.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE Names
       (NAME  TEXT,SURNAME TEXT PRIMARY KEY)''')
        

print ("Table created successfully")

conn.execute('''CREATE TABLE Ergo
       (NAME TEXT,ERGO   TEXT,ACTIVITY TEXT,DATE  REAL PRIMARY KEY,TIME_IN  TEXT , TIME_OUT  TEXT ,HOURSDEC INT(2),HOURS TEXT)''')
        
        
        

print ('Table created successfully')
conn.close()
