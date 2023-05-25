
from tkinter import *
import requests
import json
from datetime import datetime

root =Tk()
root.geometry("400x400")
root.title("Weather")

city_value = StringVar()
 
def showWeather():

    api_key = "eda2b2s6d#sd65f4de7c4b8" # from OpenWeatherMap
    
    city_name=city_value.get()
 
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    response = requests.get(weather_url)
 
    weather_info = response.json()
 
 
    tfield.delete("1.0", "end")

    if weather_info['cod'] == 200:
 
        temp = int(weather_info['main']['temp'])
        feels_like_temp = int(weather_info['main']['feels_like'])
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
             
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"{city_name}' not found!"
    tfield.insert(INSERT, weather)
 
 
city_head= Label(text = 'Enter City Name').pack() 
 
inp_city = Entry(textvariable = city_value,  width = 24).pack()
 
 
Button(command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 

weather_now = Label(text = "Weather: ", font = 'arial 12 bold').pack()
 
tfield = Text(width=46, height=10)
tfield.pack()
 
root.mainloop()