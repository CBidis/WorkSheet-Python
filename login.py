import sqlite3
import sys, os, traceback
import time
#import mtTkinter as Tkinter
#from tkinter import *
import messagebox
from ErrorLogFile import * 


def New_employee(name,surname):
    try:
        conn = sqlite3.connect('worksheet.db')
        print ("Opened database successfully")
        conn.execute("INSERT INTO Names VALUES (?,?)",(name,surname))      
        conn.commit()
        messagebox.showinfo("Successful Entry","Welcome to IBM  "+name+'  '+surname)
    except sqlite3.IntegrityError as e:
        messagebox.showerror("Warning","User Already Exists")
        conn.close()
        ErrorLogfile('ErrorLogFiles\\integrityerrors.txt',str(e),surname)
        raise e
    except sqlite3.Error as e1:
        messagebox.showerror("Error","An error occured while connecting to the Database")
        conn.close()
        ErrorLogfile('ErrorLogFiles\\connections_errors.txt',str(e1),'None')
        raise e1
    conn.close()
    
    
def Login(name,surname):
    try:
        conn = sqlite3.connect('worksheet.db')
        cur=conn.execute('SELECT * FROM names WHERE NAME=? AND SURNAME=?',(name,surname))
        if cur.fetchall():
            messagebox.showinfo("Have a nice day","Welcome back  "+name+'  '+surname)
        else:
            messagebox.showerror("Warning","Name or Surname is wrong , check your Input")
            conn.close()
            ErrorLogfile('ErrorLogFiles\\NotfoundInDb.txt','These entries dont exist in the db',name+' and '+surname)
            raise ValueError
    except sqlite3.Error as e:
        messagebox.showerror("Warning","Not Connected to the Database")
        ErrorLogfile('ErrorLogFiles\\connections_errors.txt',str(e),'None')
        raise e
    conn.close()



    


    
