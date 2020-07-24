import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='Bigboss@34')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_hospital_details(H_ID):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Hospital where Hospital_Id = %s"""
        cursor.execute(select_query, (H_ID,))
        fetch_recs = cursor.fetchall()
        print("Printing Hospital record: ")
        for recs in fetch_recs:
            print ("Hospital_ID",recs[0])
            print ("Hospital Name", recs[1])
            print ("Bed Count", recs[2])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def get_doctor_details(DOC_ID):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from doctor where Hospital_Id = %s"""
        cursor.execute(select_query, (DOC_ID,))
        fetch_recs = cursor.fetchall()
        print("Printing Hospital record: ")
        for recs in fetch_recs:
            print ("DoC_ID",recs[0])
            print ("DOC Name", recs[1])
            print ("Hosp ID", recs[2])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

get_hospital_details(2)
get_doctor_details(105)