from tkinter import *
import tkinter
import psycopg2
import requests
from PIL import Image, ImageTk

root = Tk()
button1 = Button(master=root, text='Amsterdam',command=root.destroy)
button1.pack()
button2 = Button(master=root, text='Utrecht',command=root.destroy)
button2.pack()
button3 = Button(master=root, text='Rotterdam',command=root.destroy)
button3.pack()
root.geometry("300x200")
root.mainloop()


def find_customers_from():
    query = """SELECT     id,bericht
               FROM       bericht
               WHERE      beoordeling IS TRUE 
               ORDER BY datum_beoordeeld,tijd_beooordeeld DESC
               LIMIT 5"""
    with conn.cursor() as cursor:
        cursor.execute(query)
        records = cursor.fetchall()
    return records

connection_string = "host='localhost' dbname='zuil1' user='postgres' password='Rahasia123.'"
conn = psycopg2.connect(connection_string)

customers = find_customers_from()
lst =[]
for record in customers:
    lst.append(record[1])
cursor = conn.cursor()

column_names = []
data_rows = []

with conn as connection:
    with connection.cursor() as cursor:
      cursor.execute("select ov_bike, elevator, toilet, park_and_ride from station_service where station_city ='Amsterdam'")
      column_names = [desc[0] for desc in cursor.description]
      for row in cursor:
        for i in row:
          data_rows.append(i)

tuples = [(key, value) for i, (key, value) in enumerate(zip(column_names, data_rows))]
res = dict(tuples)
print(res)

conn.commit()
conn.close()


url = "https://api.openweathermap.org/data/2.5/weather?q=Amsterdam&units=metric&appid=7751f43e6e24b3097fa9579eb6e0795e"

res = requests.get(url)

data = res.json()

temp = data['main']['temp']
a = ('Temperature : {} degree celcius'.format(temp))

wind_speed = data['wind']['speed']
b = ('Wind Speed : {} m/s'.format(wind_speed))

latitude = data['coord']['lat']
c = ('Latitude : {}'.format(latitude))

longitude = data['coord']['lon']
d = ('Longitude : {}'.format(longitude))

description = data['weather'][0]['description']
e = ('Description : {}'.format(description))


win = Tk()
win.title("Stationshalscherm")
win.geometry("1300x600")
win.config(bg="#CACAFF")

naam = Label(win,text ='Amsterdam Centraal', font = ('Algerian', 25, 'bold'),fg="Navyblue",bg="#CACAFF")
naam.grid(row=0,column=0,sticky=W,padx=10)

w = Label(win, text ="\n"+"\nRecente berichten", font = ('Helvetica', 20, 'bold'),fg="Navyblue",bg="#CACAFF")
w.grid(row=7,column=1,sticky=W,padx=20)

label = Label(win, text=lst[0], font = ('Helvetica', 16, 'bold'),bg="#CACAFF")
label.grid(row=8,column=1,sticky=W,padx=20)

label1 = Label(win, text=lst[1], font = ('Helvetica', 16, 'bold'),bg="#CACAFF")
label1.grid(row=9,column=1,sticky=W,padx=20)

label2 = Label(win, text=lst[2], font = ('Helvetica', 16, 'bold'),bg="#CACAFF")
label2.grid(row=10,column=1,sticky=W,padx=20)

label3 = Label(win, text=lst[3], font = ('Helvetica', 16, 'bold'),bg="#CACAFF")
label3.grid(row=11,column=1,sticky=W,padx=20)

label4 = Label(win, text=lst[4], font = ('Helvetica', 16, 'bold'),bg="#CACAFF")
label4.grid(row=12,column=1,sticky=W,padx=20)

label5 = Label(win, text="\nLive weerbericht", font = ('Helvetica', 20, 'bold'),fg="Navyblue",bg="#CACAFF")
label5.grid(row=1,column=0,sticky=W,padx=10)

label6 = Label(win, text=a, font = ('Helvetica', 16, 'bold'),bg="#CACAFF")
label6.grid(row=2,column=0,sticky=W,padx=10)

label7 = Label(win, text=b, font = ('Helvetica', 16, 'bold'),bg="#CACAFF")
label7.grid(row=3,column=0,sticky=W,padx=10)

label8 = Label(win, text=c, font = ('Helvetica', 16, 'bold'),bg="#CACAFF")
label8.grid(row=4,column=0,sticky=W,padx=10)

label9 = Label(win, text=d, font = ('Helvetica', 16, 'bold'),bg="#CACAFF")
label9.grid(row=5,column=0,sticky=W,padx=10)

label10 = Label(win, text=e, font = ('Helvetica', 16, 'bold'),bg="#CACAFF")
label10.grid(row=6,column=0,sticky=W,padx=10)

label11 = Label(win, text="\n"+"\nDe faciliteiten op dit station", font=('Helvetica', 20, 'bold'),fg="Navyblue",bg="#CACAFF")
label11.grid(row=7,column=0,sticky=W,padx=10)


image1 = Image.open("img_lift.png")
test = ImageTk.PhotoImage(image1)
label12 = tkinter.Label(image=test)
label12.image = test
label12.place(x=10,y=380)

image2 = Image.open("img_pr.png")
test1 = ImageTk.PhotoImage(image2)
label12 = tkinter.Label(image=test1)
label12.image = test1
label12.place(x=200,y=380)

image3 = Image.open("recent-removebg-preview.png")
test2 = ImageTk.PhotoImage(image3)
label13 = tkinter.Label(image=test2,bg="#CACAFF")
label13.image = test2
label13.place(x=550,y=50)

win.mainloop()