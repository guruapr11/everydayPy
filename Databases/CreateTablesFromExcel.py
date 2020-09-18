''' This program creates tables in mysql based on the file names dynamically and
also inserts the file data into tables'''
import pymysql
#from sqlalchemy import create_engine
import datetime
import os
import sys
import pandas as pd
import chardet

#mydb1 = create_engine('mysql+pymysql://root:Bigboss@34@localhost/guru2')
mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="Bigboss@34",
  database="guru2"
)

mycursor = mydb.cursor()

dt  = datetime.date.today()
dnt= str(dt.year) +"_"+ str(dt.month)+"_"+str(dt.day)

def find_encoding(files):
    r_file = open(files, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc

def import_data(lang,dumguru):
    #rcount=0
    os.chdir('C:/tech/python/langs')
    for files in (os.listdir('C:/tech/python/langs')):
        my_encoding = find_encoding(files)
        filename=str(files)
        if filename.startswith(lang):
            #with open(files) as fread:

                df = pd.read_excel(files,encoding=my_encoding,errors='ignore')
                df.to_sql(name=dumguru, con=mydb)
                #for row in fread:
                #    mycursor.execute("""insert into """ + dumguru + """ values (%s)""",row)
                #    rcount = rcount + 1
    #print("record(s) inserted for language {0} is {1}".format(lang,rcount))


count=0
array_langs = ['DE','ES','FR']
for lang in array_langs:
    dumguru = lang + "_" + str(dnt)
    mycursor.execute(""" CREATE TABLE """ + dumguru + """ ( ID INT, dum VARCHAR(20), city VARCHAR(20) )""")
    import_data(lang,dumguru)
    count=count+1
print ("total tables created were", count)
mydb.commit()
mycursor.close()
print ("Done")





