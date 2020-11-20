import pymysql
# Open database connection
db = pymysql.connect("localhost","root","","database")
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query to UPDATE required records
#sql = """UPDATE EMPLOYEE SET AGE = 21 WHERE SEX = '%c'" % ('M')"""
sql="""DELETE FROM EMPLOYEE WHERE FIRST_NAME='MAC'"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    #print("Total number of rows updated :", db.total_changes)
    print("operation done successfully")
except:
    # Rollback in case there is any error
    db.rollback()
    print("operation fail..")
# disconnect from server
db.close()
