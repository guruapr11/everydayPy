''' This program creates tables in mysql based on the file names dynamically and
also inserts the file data into tables'''
import pymysql
import datetime
import os

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="Bigboss@34",
  database="guru2"
)
mycursor = mydb.cursor()

dt  = datetime.date.today()
dnt= str(dt.year) +"_"+ str(dt.month)+"_"+str(dt.day)

def import_data(lang,dumguru):
    rcount=0
    os.chdir('C:/tech/python/New folder')
    for files in (os.listdir('C:/tech/python/New folder')):
        filename=str(files)
        if filename.startswith(lang):
            with open(files) as fread:
                for row in fread:
                    mycursor.execute("""insert into """ + dumguru + """ values (%s)""",row)
                    rcount = rcount + 1
    print("record(s) inserted for language {0} is {1}".format(lang,rcount))


count=0
array_langs = ['DE','ES','FR']
for lang in array_langs:
    dumguru = lang + "_" + str(dnt)
    mycursor.execute(""" CREATE TABLE """ + dumguru + """ ( dum VARCHAR(20) )""")
    import_data(lang,dumguru)
    count=count+1
print ("total tables created were", count)
mydb.commit()
mycursor.close()
print ("Done")





