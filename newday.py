import sqlite3
import os
from ErrorLogFile import * 
#from tkinter import *
import messagebox
def New_entry(namesur,ergo,activity,date,tim1,tim2,dt):
    #get the decimal form of hours!
    secs = dt.total_seconds()
    hoursdec = secs / 3600
    #change dot char with coma char for the summing of dechours in the csv file
    a=str(hoursdec).replace('.',',')
    #print(a)
    #change dot char with coma char for the summing of dechours in the csv file
    try:
        conn = sqlite3.connect('worksheet.db')
    
        conn.execute('insert into Ergo values (? , ? , ? , ? , ? ,?, ?, ?)',(namesur,ergo,activity,date,tim1,tim2,a,str(dt)))      
        conn.commit()
        messagebox.showinfo("Successful Entry","You just created your Entry for the"+'  '+date)
        conn.close()

    except sqlite3.IntegrityError as e:
        messagebox.showerror("Warning","You have created your Entry for:"+date)
        conn.close()
        ErrorLogfile('ErrorLogFiles\\integrityerrors.txt',date,' ')
        raise e
    except sqlite3.Error as e1:
        messagebox.showerror("Error","An error occured while connecting to the Database")
        conn.close()
        ErrorLogfile('ErrorLogFiles\\connections_errors.txt',str(e1),'None')
        raise e1

    conn.close()
        

def cre(mindate,maxdate):
    try:
        
        conn = sqlite3.connect('worksheet.db')
        cur=conn.execute('SELECT NAME,ERGO,ACTIVITY,DATE,HOURSDEC,HOURS FROM Ergo WHERE DATE BETWEEN ? AND ?',(mindate,maxdate))
        
        if cur.fetchall():   
            fo=open('worksheet.xls','a')
            cur1=conn.execute('SELECT NAME,ERGO,ACTIVITY,DATE,HOURSDEC,HOURS FROM Ergo WHERE DATE BETWEEN ? AND ?',(mindate,maxdate))
            for r in cur1.fetchall():
                 name,ergo,activity,date,hoursdec,hours = r
                 #print(name,ergo,activity,date,str(hoursdec)[0:4],hours)dtformated = strptime(str(dt),("%H:%M"))
                 
                 fo.write(name+'\t'+ergo+'\t'+activity+'\t'+date+'\t'+str(hoursdec)[0:4]+'\t'+hours)
                 fo.write('\n')
            fo.close()
            conn.close()
            messagebox.showinfo("Results","Your results for the Month are located here:"+'  '+os.path.abspath('worksheet.xls'))
        else:
            messagebox.showerror("Error","No entries for your dates")
            conn.close()
            raise ('Empty Dataset')
            
     
    except sqlite3.Error as e:
        messagebox.showerror("Warning","Not connected to the database")
        ErrorLogfile('ErrorLogFiles\\connections_errors.txt',str(e),' ')
        raise e

    
    conn.close()
         

    
def weekcre(mindate,maxdate):
    try:
        conn = sqlite3.connect('worksheet.db')
        cur=conn.execute('SELECT NAME,ERGO,ACTIVITY,TIME_IN,TIME_OUT,HOURS FROM Ergo WHERE DATE BETWEEN ? AND ?',(mindate,maxdate))
        if cur.fetchall():
            fo=open('weekworksheet.xls','a')
            cur1=conn.execute('SELECT DATE,NAME,ERGO,ACTIVITY,TIME_IN,TIME_OUT,HOURS FROM Ergo WHERE DATE BETWEEN ? AND ?',(mindate,maxdate))
            for r in cur1.fetchall():
                date,name,ergo,activity,timei,timeo,hours = r
                
                #creating the right format for the excel file
                t1 = time.strptime(timei[10:len(timei)].strip(), "%H:%M:%S")
                t2 = time.strptime(timeo[10:len(timeo)].strip(), "%H:%M:%S")
                timei = time.strftime( "%I:%M %p", t1 )
                timeo = time.strftime( "%I:%M %p", t2 )
                #creating the right format for the excel file
                fo.write(date+'\t'+name+'\t'+ergo+'\t'+activity+'\t'+timei+'\t'+timeo+'\t'+hours)
                fo.write('\n')
            fo.close()    
            conn.close()
            messagebox.showinfo("Results","Your results for the Week are located here:"+'  '+os.path.abspath('weekworksheet.xls'))
        else:
            messagebox.showerror("Error","No entries for your dates")
            conn.close()
            raise ('Empty Dataset')
        
    except sqlite3.Error as e:
        
        messagebox.showerror("Warning","Not connected to the database")
        ErrorLogfile('ErrorLogFiles\\connections_errors.txt',str(e),' ')
        raise e

    
    conn.close()


def allentries():
    try:
        conn = sqlite3.connect('worksheet.db')
        cur=conn.execute('SELECT NAME,ERGO,ACTIVITY,TIME_IN,TIME_OUT,HOURS,DATE,HOURSDEC FROM Ergo ')
        if cur.fetchall():
            fo=open('FullReport.xls','a')
            fo.write('Όνομα-Επώνυμο'+'\t'+'Υποδιέυθυνση' +'\t'+'Εργασιά'+'\t'+'Ωρα Εισόδου'+'\t'+'Ώρα Εξόδου'+'\t'+'Σύνολο Ωρών'+'\t'+'Ημερομηνία'+'\t'+'Ωρες σε δεκαδική μορφή')
            fo.write('\n')
            cur1=conn.execute('SELECT NAME,ERGO,ACTIVITY,TIME_IN,TIME_OUT,HOURS,DATE,HOURSDEC FROM Ergo ')
            for r in cur1.fetchall():
                name,ergo,activity,timei,timeo,hours,date,hoursdec = r
                #creating the right format for the excel file
                t1 = time.strptime(timei[10:len(timei)].strip(), "%H:%M:%S")
                t2 = time.strptime(timeo[10:len(timeo)].strip(), "%H:%M:%S")
                timei = time.strftime( "%I:%M %p", t1 )
                timeo = time.strftime( "%I:%M %p", t2 )
                #creating the right format for the excel file
                fo.write(name+'\t'+ergo+'\t'+activity+'\t'+timei+'\t'+timeo+'\t'+hours+'\t'+date+'\t'+str(hoursdec)[0:4])
                fo.write('\n')
            fo.close()    
            conn.close()
            messagebox.showinfo("Results","Your results  are located here:"+'  '+os.path.abspath('FullReport.xls'))
        else:
            messagebox.showerror("Error","You have made no Entries")
            conn.close()
            raise ('Empty Dataset')
        
    except sqlite3.Error as e:
        
        messagebox.showerror("Warning","Not connected to the database")
        ErrorLogfile('ErrorLogFiles\\connections_errors.txt',str(e),' ')
        raise e

    
    conn.close()




def deentries(dedate):
    try:
        conn = sqlite3.connect('worksheet.db')
        cur=conn.execute('DELETE  FROM Ergo  WHERE DATE=?',(dedate,))
        conn.commit()
        if cur.rowcount>0:
            messagebox.showinfo("Success","Your Entry was deleted successfully")
        else:
            messagebox.showerror("Error","Not Entries corresponding to your Date")
            conn.close()
        
    except sqlite3.Error as e1:
        messagebox.showerror("Error","Not connected to the database")
        conn.close()
        raise e1
        
    conn.close()
    
