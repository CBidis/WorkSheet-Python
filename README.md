# WorkSheet-Python
WorkSheet  aims to simplify the way that employees give reports to their employers about the working hours
and their work in the project they participate.It consists of 4 basic python programmes.

# worksheetDB.py

This programme creates the the 2 tables that our applciation uses if the user opens the app for the first time.
SQLite is the database engine.

#worksheet.py

Is the programme responsible for the graphical user interface creation , TKinter was the library used for the most of the front
end designs.
ErrorLogFile is a small module created to log all the errors in the application , connection problems , user authentication problems, etc.
The interface consists of several buttons that will be detailed in the next modules.

#login.py

This module is used for the the login proccess and the registration of new users to the application.
If the register button is pressed we have an insert in our table with a  new user , likewise if the login button is pressed 
the table is searched for the user given.


#newday.py

The newday module is used only if we have a succesful login , when this happens we have the next options:

1)Create a new entry , by filling the fields of username , workspace , date , time-in , time-out and the role we have 
we create an entry for the given date.
We can only have one entry for every date!

2)Delete entry , if we make any mistakes in the creation of our entries we can always go back and delete any wrong entries
and create a new one.

3)Create .csv with month work , by filling the two date fields and pressing this button we have the creation of an excel file 
with all the entries of the month we worked . the two date fields work like , from 1/1/2015 to 31/1/2015 will give us all the
work entries for the month of January.

4)The week report button creates the week report , uses the same as the month report , creates the responding excel for a week
of work.

5) The check entries button , it actually creates an excel file with all of our entries , so the filling of the date fields is 
not necessary.

6)Finally the logout button returns us to the login/register screen.

 
