import pymysql

# Open database connection
#db = pymysql.connect("sql12.freemysqlhosting.net","sql12345764","sql12345764","Ui4yvwsAy3");
db = pymysql.connect("localhost","root","","database");

if(db):
    print("Opened database successfully");
else:
    print("database not Opened  ");

cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
LAST_NAME, AGE, SEX, INCOME)
VALUES ('Modon', 'Mohan', 20, 'M', 2100)"""


try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print("data insert successfully");
    
except:
# Rollback in case there is any error
   db.rollback()
# disconnect from server
db.close()
