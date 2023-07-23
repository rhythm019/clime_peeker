from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
import os
from PIL import Image, ImageTk

root=Tk()
root.title("ClimePeeker")
root.geometry("900x480+400+400")
root.configure(bg="#57adff")
root.resizable(False,False)

def getWeather():
    location=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(location)
    obj=TimezoneFinder()

    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)} ° N,{round(location.longitude,4)} ° E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #weather
    user_api=os.environ['current_weather_data']
    city=location

    complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+str(location)+"&appid="+user_api

    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    #create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15) 
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    h.config(text=(temp_city," ° c"))
    p.config(text=(weather_desc))
    w.config(text=(hmdt,"%"))
    d.config(text=(wind_spd,"m/s"))

    #days
    first=datetime.now()
    day1.config(text=first.strftime("%A"))

    
##icon
image_icon=PhotoImage(file="C:\\Users\\Armaan\\Desktop\\codes\\project\\logo.png")
root.iconphoto(False,image_icon)

Round_box=PhotoImage(file="C:\\Users\\Armaan\\Desktop\\codes\\project\\Rounded Rectangle 1.png")
Label(root,image=Round_box,bg="#57adff").place(x=30,y=110)

#label

label2=Label(root,text="Temperature =",font=("Helvetica",12),fg="white",bg="#203243")
label2.place(x=45,y=140)

label3=Label(root,text="Weather desc=",font=("Helvetica",12),fg="white",bg="#203243")
label3.place(x=45,y=160)

label4=Label(root,text="Humidity =",font=("Helvetica",12),fg="white",bg="#203243")
label4.place(x=45,y=180)

label5=Label(root,text="Wind Speed =",font=("Helvetica",12),fg="white",bg="#203243")
label5.place(x=45,y=200)

##search box
Search_image=PhotoImage(file="C:\\Users\\Armaan\\Desktop\\codes\\project\\Rounded Rectangle 3.png")
myimage=Label(image=Search_image,bg="#57adff")
myimage.place(x=270,y=120)

weat_image=PhotoImage(file="C:\\Users\\Armaan\\Desktop\\codes\\project\\Layer 7.png")
weatherimage=Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=290,y=127)

textfield=tk.Entry(root,justify="center",width=15,font=("poppins",25,"bold"),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()

Search_icon=PhotoImage(file="C:\\Users\\Armaan\\Desktop\\codes\\project\\Layer 6.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=645,y=125)

##Bottom box
frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

#bottom boxes
firstbox=PhotoImage(file="C:\\Users\\Armaan\\Desktop\\codes\\project\\Rounded Rectangle 2.png")
secondbox=PhotoImage(file="C:\\Users\\Armaan\\Desktop\\codes\\project\\Rounded Rectangle 2 copy.png")

Label(frame,image=firstbox,bg="#212120").place(x=30,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=300,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=400,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=500,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=600,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=700,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=800,y=30)

#clock(for time)
clock=Label(root,font=("Helvetica",30,"bold"),fg="white",bg="#57adff")
clock.place(x=30,y=20)

#timezone
timezone=Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
timezone.place(x=700,y=20)

long_lat=Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)

#thpwd
h=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
h.place(x=150,y=140)
p=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
p.place(x=150,y=160)
w=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
w.place(x=150,y=180)
d=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
d.place(x=150,y=200)

#first cell
firstframe=Frame(root,width=250,height=145,bg="#282829")
firstframe.place(x=18,y=320)
day1=Label(firstframe,font="arial 20",bg="#282829",fg="#fff")
day1.place(x=80,y=2)
firstimage=Label(firstframe,bg="#282829")
firstimage.place(x=0,y=34)
photo1=PhotoImage(file="C:\\Users\\Armaan\\Desktop\\codes\\project\\lake.png")
my_label=Label(root,image=photo1,height=145,width=250)

firstimage.config(image=photo1)
firstimage.image=photo1

#second cell
secondframe=Frame(root,width=580,height=140,bg="#282829")
secondframe.place(x=300,y=320)
day2=Label(secondframe,bg="#282829",fg="#fff")
day2.place(x=10,y=5)
secondimage=Label(secondframe,bg="#282829")
secondimage.place(x=1,y=2)
photo2=PhotoImage(file="C:\\Users\\Armaan\\Desktop\\codes\\project\\wet.png")
my_label=Label(root,image=photo2,height=200,width=580)

secondimage.config(image=photo2)
secondimage.image=photo2
root.mainloop()