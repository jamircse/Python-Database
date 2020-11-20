import pymysql
db=pymysql.connect("localhost","root","","database")
conn=db.cursor();
sql="""SELECT *FROM buyers"""
try:
    conn.execute(sql)
    result=conn.fetchall()
    for row in result:
          print(row)
except:
    print("Operation fail to execute database ")
