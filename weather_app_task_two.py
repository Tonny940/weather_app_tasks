import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Entry

import requests

api_key = "039a12d23806eea26ccefd5251862476"
cities = ['New York', 'California', 'Amsterdam', 'London', 'San Diego']
city_weather_info = {}


# Getting data from platform
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    try:
        return {'city': city,
                'clouds': data['weather'][0]['description'],
                'temp': int(data['main']['temp']),
                'humidity': data['main']['humidity'],
                }
    except Exception:
        messagebox.showinfo('Error', 'Wrong city name')


# Functionality popout windows with weather for given cities
def show_weather(city_data):
    for city, data in city_data.items():
        try:
            message = f"{city}: {data['clouds']}\n" \
                      f"temperature: {data['temp']}°C\n" \
                      f"humidity: {data['humidity']}%"
            messagebox.showinfo("Weather Info", message)
        except Exception:
            messagebox.showinfo('Error', 'Please try again')


# Functionality popout window with the coldest city and average temperatures in given
def min_average_temp(data_info):
    coldest_city = min(data_info, key=lambda city: data_info[city]["temp"])
    average_temp = sum([data_info[city]["temp"] for city in data_info]) / len(data_info)
    message = f"Coldest city is {coldest_city}: {data_info[coldest_city]['temp']}°C\n" \
              f"Avg temperature: {int(average_temp)}°C"
    messagebox.showinfo("Weather Statistics", message)


# Factory function working with users input
def custom_city(name):
    custom_city_data = {name: get_weather_data(name)}
    show_weather(custom_city_data)


# Extracting data for given cities
for city in cities:
    city_weather_info[city] = get_weather_data(city)

# TKinter GUI
root = tk.Tk()
root.title("Weather App")

# Input section
e_message = tk.Label(text="Enter city name")
e_message.pack()
e = Entry()
e.pack()

submit_btn = tk.Button(root, text="Weather Info", command=lambda: custom_city(e.get()))
submit_btn.pack()

given_cities_msg = tk.Label(text="Given cities weather")
given_cities_msg.pack()

# Button for showing weather in given cities
given_cities_btn = tk.Button(root, text="Show Given Cities",
                             command=lambda: show_weather(city_weather_info))
given_cities_btn.pack()

# Button for showing the coldest city and average temperature in given cities
min_average_temp_btn = tk.Button(root, text="Min Average Temperature",
                                 command=lambda: min_average_temp(city_weather_info))
min_average_temp_btn.pack()

root.mainloop()