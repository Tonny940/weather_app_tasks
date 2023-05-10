import json

import requests as requests

API_KEY = '039a12d23806eea26ccefd5251862476'
cities = ['New York', 'California', 'Amsterdam', 'London', 'San Diego']
city_weather_info = {}


def extract_data(city, key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)

    return {'clouds': data['weather'][0]['description'],
            'temp': int(data['main']['temp']),
            'humidity': data['main']['humidity'],
            }


def print_info(city, weather_data):
    print(f"{city}: \n"
          f"{weather_data['clouds']} \n"
          f"Temperature: {weather_data['temp']}°C \n"
          f"Humidity: {weather_data['humidity']}% \n")


for city in cities:
    city_weather_info[city] = extract_data(city, API_KEY)

for city in city_weather_info.keys():
    print_info(city, city_weather_info[city])

coldest_places = min(city_weather_info, key=lambda place: city_weather_info[place]['temp'])
average_temperature = sum(city_weather_info[place]['temp'] for place in city_weather_info) / len(city_weather_info)

print(f"Coldest city: {coldest_places}, {city_weather_info[coldest_places]['temp']}°C")
print(f"Average temperature: {int(average_temperature)}°C\n")

print('To exit write "END"')
city_input = input("Enter city: ")

while city_input != 'END':
    try:
        weather_info = extract_data(city_input, API_KEY)
        print_info(city_input, weather_info)
    except Exception:
        print("Wrong city name! Try again please!\n")

    print('To exit write "END"')
    city_input = input("Enter city: ")