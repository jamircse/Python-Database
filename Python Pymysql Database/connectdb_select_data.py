import pymysql
db=pymysql.connect("localhost","root","","database")
if(db):
    print("database connection success..")
else:
    print("database connection errors")

cursor=db.cursor();
sql = "SELECT * FROM buyers"
try:
   cursor.execute("SELECT * FROM buyers LIMIT 100")
 
   rows = cursor.fetchall()
   
 
   for row in rows:
       #print(row)
       
      id = row[0]
      name = row[1]
      phone = row[2]
      email = row[3]
      address = row[4]
      # Now print fetched result
      print ("id = %s,name = %s,phone = %s,email = %s,address = %s" % \
             (id, name, phone, email, address )) 
except:
    print ("Error: unable to fetch data")

# disconnect from server
db.close()
