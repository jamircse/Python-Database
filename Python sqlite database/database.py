'''
import sqlite3
conn = sqlite3.connect('database.db')
if(conn):
 print("Opened database successfully");
 
cursor = conn.execute("SELECT *FROM  user");
for row in cursor.fetchall():
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("pass = ", row[2])
'''
from sqlite3 import connect

# Replace username with your own A2 Hosting account username:
conn = connect('jamir.db')
curs = conn.cursor()

#curs.execute("CREATE TABLE employees (firstname varchar(32), lastname varchar(32), title varchar(32));")
#curs.execute("INSERT INTO employees VALUES('Elizabeth ', 'Davis', 'Engineer');")
#conn.commit()

curs.execute("SELECT * FROM employees;")
for (name) in curs.fetchall():
    print(name)

conn.close()
