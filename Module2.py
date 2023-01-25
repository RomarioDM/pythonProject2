import psycopg2
import datetime

def datum():
    localtime = datetime.datetime.now()
    date = localtime.strftime("%Y-%m-%d")
    return date

def tijd():
    localtime = datetime.datetime.now()
    time = localtime.strftime("%H:%M")
    return time

def modarator():
    naam = input("Uw naam: ")
    return naam

def beoordeling():
    status = input("Voor positief toets P en voor negatief toets N: ")
    if status == "P":
        return True
    elif status == "N":
        return False

def bericht_id():
    x = int(input("Bericht ID: "))
    return x

def find_customers_from():
    query = """SELECT     id,bericht
               FROM       bericht
               WHERE      beoordeling IS NULL """
    with conn.cursor() as cursor:
        cursor.execute(query)
        records = cursor.fetchall()
    return records


connection_string = "host='localhost' dbname='zuil1' user='postgres' password='Rahasia123.'"
conn = psycopg2.connect(connection_string)

customers = find_customers_from()
for record in customers:
    print(record[0],record[1])
cursor = conn.cursor()

query1 = """UPDATE bericht
            SET moderatornaam = %s, beoordeling = %s, datum_beoordeeld = %s, tijd_beooordeeld = %s
            WHERE id = %s """
data1 = (modarator(),beoordeling(),datum(),tijd(),bericht_id())

cursor.execute(query1,data1)

conn.commit()
conn.close()