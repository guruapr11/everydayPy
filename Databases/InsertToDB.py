'''This program is a simple insert into mySQL DB table from a CSV file'''
#If you are loading multiple files within the same table, you can use the if_exists parameter:
# df.to_sql(name='Table1', con=mydb, if_exists='append')'''
#For larger datasets use:
# chunksize = 10000
# for chunk in pd.read_csv('ourfile.csv', chunksize=chunksize):
#     chunk.to_sql(name='Table1', con=mydb, if_exists='append')

import csv
import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="Bigboss@34",
  database="guru2"
)
mycursor = mydb.cursor()
with open('C:/tech/python/Book11.csv') as csv_file:
    csv_data = csv.reader(csv_file,delimiter=',')
    for row in csv_data:
        mycursor.execute("INSERT INTO table1 values (%s, %s, %s, %s)", row)
        print (row)
mydb.commit()
mycursor.close()
print ("Done")