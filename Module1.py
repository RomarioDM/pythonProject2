import datetime
import random
import psycopg2

def bericht():
    tekst = input("Uw bericht: ")
    return tekst

def reiziger():
    naam = input("Voer uw naam in: ")
    if len(naam) > 0 and naam.strip():
        return naam
    else:
        naam = "Anoniem"
        return naam


def datum():
        localtime = datetime.datetime.now()
        date = localtime.strftime("%Y-%m-%d")
        return date

def tijd():
    localtime = datetime.datetime.now()
    time = localtime.strftime("%H:%M")
    return time

def station():
    lst = ("Utrecht","Amsterdam","Den Haag")
    item = random.choice(lst)
    return item

connection_string = "host='localhost' dbname='zuil1' user='postgres' password='Rahasia123.'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()

query = """INSERT INTO bericht (bericht,naam,datum,tijd,station_city)
           VALUES (%s, %s, %s, %s, %s);"""
data = (bericht(),reiziger(),datum(),tijd(),station())

cursor.execute(query, data)

conn.commit()
conn.close()