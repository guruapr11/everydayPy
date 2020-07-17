''' This program has 2 parts.
1. Export from Database to CSV file (remove the commented out part)
2. To extract records from DB and do some calculations and update back '''
import mysql.connector
#import csv
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bigboss@34",
  database="guru2"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM table1 where age=22")

myresult = mycursor.fetchall()

#for x in myresult:
#  print (x)

#c = csv.writer(open('dbdump01.csv', 'w',newline=''))
#c.writerow(col[0] for col in mycursor.description)

for x in myresult:
    #c.writerow(x)
    total = x[0] + 10
    mycursor.execute("""update table1 set number = %s where age = %s""", (total,x[3]))
mydb.commit()

print(mycursor.rowcount, "record(s) affected")