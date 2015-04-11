from tkinter import *
from PIL import ImageTk
from PIL import Image
import messagebox
from ErrorLogFile import *
from datetime import *
from time import *
import webbrowser
import time
import os
print(os.path.abspath("image files\\12.jpg"))
#main function callings
def connect():
   from login import Login
   if not v4.get() or not v5.get():
      messagebox.showerror("Warning","Check your input for empty fields!")
      raise
   Login(v4.get(),v5.get())
   #hiding the buttons after succesful login
   b.lower()
   c.lower()
   eip.lower()
   ecl.lower()
   spip.lower()
   dnpip.lower()
   d.place(x=0,y=0)
   de.place(x=0,y=390)
   e.place(x=819,y=0)
   f.place(x=819,y=300)
   g.place(x=819,y=550)
   d.lift()
   de.lift()
   e.lift()
   f.lift()
   g.lift()
   e1.lift()
   e2.lift()
   v7.set(v4.get()+' '+v5.get())#with succesful logins we have name and surname ready for the next action
   e3.lift()
   e4.lift()
   e5.lift()
   e6.lift()
   e7.lift()
   e8.lift()
   logout.place(x=405,y=0)
   logout.lift()
   
   
           
def register():
   from login import New_employee
   if not v1.get() or not v2.get():
      messagebox.showerror("Warning","Check your input for empty fields!")
      raise
   New_employee(v1.get(),v2.get())
   #hiding the buttons after succesful register
   eip.lower()
   ecl.lower()
   b.lower()
   logout.lower()
   v4.set(v1.get())
   v5.set(v2.get())

def logoff():
   #showing and hiding the apprpriate buttons after logoff 
   b.lift()
   c.lift()
   eip.lift()
   ecl.lift()
   spip.lift()
   dnpip.lift()
   d.lower()
   de.lower()
   e.lower()
   f.lower()
   g.lower()
   e1.lower()
   e2.lower()
   e3.lower()
   e4.lower()
   e5.lower()
   e6.lower()
   e7.lower()
   e8.lower()
   logout.lower()

def hours():
   
   from newday import New_entry
   try:
      datetime.strptime(v6.get(),("%Y/%m/%d"))
   except ValueError:
      messagebox.showerror("Warning","Date does not match format yy/mm/dd")
      ErrorLogfile('ErrorLogFiles\BaDdataTime.txt','Wrong format of DateTime',v6.get())
      raise ValueError
   #:%S"
   try:
      t1=datetime.strptime(v8.get(),("%H:%M:%S"))
      t2=datetime.strptime(v9.get(),("%H:%M:%S"))
      dt=t2-t1
      
      New_entry(v7.get(),v10.get(),v11.get(),v6.get(),t1,t2,dt)
   except ValueError:
      messagebox.showerror("Warning","Time does not match format hh:mm:ss ")
      ErrorLogfile('ErrorLogFiles\BaDdataTime.txt','Wrong format of time ',v8.get()+' and '+v9.get())
      raise ValueError
def createcsv():
   from newday import cre

   try:
      datetime.strptime(v12.get(),("%Y/%m/%d"))
      datetime.strptime(v13.get(),("%Y/%m/%d"))
   except ValueError:
      messagebox.showerror("Warning","Date does not match format yy/mm/dd")
      ErrorLogfile('ErrorLogFiles\BaDdataTime.txt','Wrong format of DateTime',v12.get()+' or '+v13.get())
      raise ValueError
   print(v12.get(),v13.get())
   cre(v12.get(),v13.get())


def createweekcsv():
   from newday import weekcre
   
   try:
      datetime.strptime(v12.get(),("%Y/%m/%d"))
      datetime.strptime(v13.get(),("%Y/%m/%d"))
   except ValueError:
      messagebox.showerror("Warning","Date does not match format yy/mm/dd")
      ErrorLogfile('ErrorLogFiles\BaDdataTime.txt','Wrong format of DateTime',v12.get()+' or '+v13.get())
      raise ValueError
   weekcre(v12.get(),v13.get())

def Fullreport():
   from newday import allentries
   allentries()

def delete():
   from newday import deentries
   try:
      datetime.strptime(v6.get(),("%Y/%m/%d"))
   except ValueError:
      messagebox.showerror("Warning","Date does not match format dd/mm/yy")
      ErrorLogfile('ErrorLogFiles\BaDdataTime.txt','Wrong format of DateTime',v6.get())
      raise ValueError
   deentries(v6.get())

def html():
   webbrowser.open_new_tab('helloworld.html')
      
             
#main function callings   
   

#set basic window information and size
ipg = Tk()
ipg.title("Month-Worksheet")
ipg.minsize(1024,768)
ipg.resizable(width=FALSE, height=FALSE)
#set basic window information and size
#for background image!
background_image=ImageTk.PhotoImage(file=os.path.abspath("image files\\12.jpg"))
background_label = Label(ipg, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#for background image!
#adding buttons and functionality
#main buttons
#bbutton creation
bbutton_image=ImageTk.PhotoImage(file=os.path.abspath("image files\\newemp.png"))
b = Button(ipg,command =register,image=bbutton_image,height=50, width=200)
#bbutton creation
#cbutton creation
cbutton_image=ImageTk.PhotoImage(file=os.path.abspath("image files\\login.png"))
c = Button(ipg,command =connect,image=cbutton_image,height=50, width=200)
#cbutton creation
#dbutton creation
dbutton_image=ImageTk.PhotoImage(file=os.path.abspath("image files\\neww.png"))
d = Button(ipg,command =hours,image=dbutton_image,height=50, width=200)
#dbutton creation
#ebutton creation
ebutton_image=ImageTk.PhotoImage(file=os.path.abspath("image files\\csv.png"))
e = Button(ipg,command =createcsv,image=ebutton_image,height=50, width=200)
#ebutton creation
#ebutton creation
fbutton_image=ImageTk.PhotoImage(file=os.path.abspath("image files\\weekr.png"))
f = Button(ipg,command =createweekcsv,image=fbutton_image,height=50, width=200)
#ebutton creation
gbutton_image=ImageTk.PhotoImage(file=os.path.abspath("image files\\centries.png"))
g = Button(ipg,command =Fullreport,image=gbutton_image,height=50, width=200)
#ebutton creation
usebutton_image=ImageTk.PhotoImage(file=os.path.abspath("image files\\useful.png"))
use = Button(ipg,command =html,image=usebutton_image,height=50, width=200)
#ebutton creation
debutton_image=ImageTk.PhotoImage(file=os.path.abspath("image files\\de.png"))
de = Button(ipg,command =delete,image=debutton_image,height=50, width=200)
#ebutton creation
#logoutbutton creation
loutbutton_image=ImageTk.PhotoImage(file=os.path.abspath("image files\\lout.png"))
logout = Button(ipg,command =logoff,image=loutbutton_image,height=50, width=200)
#logoutbutton creation

#entry widgets
v1 = StringVar()
eip = Entry(textvariable=v1)
eip.place(x=0,y=60,relheight=0.05,relwidth=0.2)
v1.set('Enter your name please')
#entry widgets
v2 = StringVar()
ecl = Entry(textvariable=v2)
ecl.place(x=0,y=100,relheight=0.05,relwidth=0.2)
v2.set('Enter your Surname please')
#entry widgets
v4 = StringVar()
spip = Entry(textvariable=v4)
spip.place(x=820,y=60,relheight=0.05,relwidth=0.2)
v4.set('Enter your Name please')
#t4=v4.get()
#entry widgets
v5 = StringVar()
dnpip = Entry(textvariable=v5)
dnpip.place(x=820,y=100,relheight=0.05,relwidth=0.2)
v5.set('Enter your Surname please')
#t5=v5.get()
#entry widgets
v6 = StringVar()
e1 = Entry(textvariable=v6)
e1.place(x=0,y=180,relheight=0.05,relwidth=0.2)
e1.lower()#only after login is visible
v6.set(time.strftime("%Y/%m/%d"))
#entry widgets

v7 = StringVar()
e2 = Entry(textvariable=v7)
e2.place(x=0,y=100,relheight=0.05,relwidth=0.2)
e2.lower()#only after login is visible
v7.set('Enter your Name and Surname please')
#entry widgets
v8 = StringVar()
e3 = Entry(textvariable=v8)
e3.place(x=0,y=220,relheight=0.05,relwidth=0.2)
e3.lower()#only after login is visible
v8.set(time.strftime("%H:%M:%S"))
#entry widgets
v9 = StringVar()
e4 = Entry(textvariable=v9)
e4.place(x=0,y=260,relheight=0.05,relwidth=0.2)
e4.lower()#only after login is visible
v9.set(time.strftime("%H:%M:%S"))
#entry widgets
v10 = StringVar()
e5 = Entry(textvariable=v10)
e5.place(x=0,y=140,relheight=0.05,relwidth=0.2)
e5.lower()#only after login is visible
v10.set('Set your Work Space')
#entry widgets
v11 = StringVar()
e6 = Entry(textvariable=v11)
e6.place(x=0,y=300,relheight=0.05,relwidth=0.2)
e6.lower()#only after login is visible
v11.set('Technical Design')
#entry widgets
v12 = StringVar()
e7 = Entry(textvariable=v12)
e7.place(x=820,y=140,relheight=0.05,relwidth=0.2)
e7.lower()#only after login is visible
v12.set(time.strftime("%Y/%m/%d"))
#entry widgets
v13 = StringVar()
e8 = Entry(textvariable=v13)
e8.place(x=820,y=180,relheight=0.05,relwidth=0.2)
e8.lower()#only after login is visible
v13.set(time.strftime("%Y/%m/%d"))
#entry widgets


#entry widgets

#packing the starting buttons to frame
b.place(x=0,y=0)
c.place(x=819,y=0)
use.place(x=0,y=550)




ipg.mainloop()
