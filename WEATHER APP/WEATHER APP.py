from tkinter import *
from PIL import ImageTk,Image
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz



root = Tk()
#root.configure(bg="gray")
root.geometry("900x500")
root.resizable(False,False)
root.title('WEATHER APP')
icon=PhotoImage(file="Copy of logo.png")
root.iconphoto(False,icon)


def getWeather():
	try:
		city=textfield.get()

		geolocator= Nominatim(user_agent="geoapiExercises")
		location= geolocator.geocode(city)
		obj = TimezoneFinder()
		result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
		print(result)

		home=pytz.timezone(result)
		local_time=datetime.now(home)
		current_time=local_time.strftime("%I:%M:%p")
		clock.config(text=current_time)
		name.config(text="CURRENT WEATHER")

		#weather
		api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b2ca934821dba48f5868e093d5d7e5c1"
		
		json_data = requests.get(api).json()
		condition = json_data['weather'][0]['main']
		description = json_data['weather'][0]['description']
		temp = int(json_data['main']['temp']-273.15)
		pressure = json_data['main']['pressure']
		humidity = json_data['main']['humidity']
		wind = json_data['wind']['speed']

		t.config(text=(temp,"°"))
		c.config(text=(condition,"|","FEELS",temp,"°"))

		w.config(text=wind)
		h.config(text=humidity)
		d.config(text=description)
		p.config(text=pressure)

	except Exception as e:
		messagebox.showerror("weather App","invalid entry!!")







textfield=Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()



#search_icon=PhotoImage("Copy of search_icon.png")
#myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#1ab5ef",command=getWeather)
myimage_icon=Button(text="SEARCH",borderwidth=9,cursor="hand2",bg="#1ab5ef",command=getWeather)
myimage_icon.place(x=360,y=40)
#myimage_icon.config(width=51,height=38)

#Button(frame_1, text="Single",height = 10).pack(side=LEFT, anchor=S, padx=[0,40])



#logo
#logo_image=PhotoImage(file="Copy of logo.png")
logo_image=PhotoImage(file="Copy of logo.png")
logo=Label(image=logo_image)
logo.place(x=150,y=100)




#bottom box
frame_image=PhotoImage(file="Copy of box.png")
frame_myimage=Label(image=frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)




#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20,'bold'))
clock.place(x=30,y=130)


#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=410,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)


w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)

d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=405,y=430)

p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)








root.mainloop()