import sqlite3

#conn = sqlite3.connect('test.db')
conn = sqlite3.connect('databse.db')
print("Opened database successfully");

#conn.execute('''CREATE TABLE COMPANY
 #        (ID INT PRIMARY KEY     NOT NULL,
  #      NAME           TEXT    NOT NULL,
   #      AGE            INT     NOT NULL,
    #     ADDRESS        CHAR(50),
     #    SALARY         REAL);''')

conn.execute('''CREATE TABLE buyers
         (id INT PRIMARY KEY     NOT NULL,
        Name           TEXT    NOT NULL,
        Phone          TEXT     NOT NULL,
        Email          TEXT     NOT NULL,
         ADDRESS        CHAR(120));''')
print("Table created successfully");

conn.close()
