import requests
import os

# storing the API key as an enviroment variable and pulling it
key = os.environ.get('WEATHER_KEY')
print(key)

# api for current weather in minneapolis imperial units
# weather_url = f'https://api.openweathermap.org/data/2.5/weather?q=minneapolis,mn,us&units=imperial&appid={key}'

weather_url = 'https://api.openweathermap.org/data/2.5/weather'
# query = {'q': 'minsk,by', 'units': 'imperial', 'appid': key}


# ask the user for the city and country and output weather

city = input('Enter your city: ')
country = input('Enter the 2 letter country code')
location = f'{city},{country}'

query = {'q': location, 'units': 'imperial', 'appid': key}

response = requests.get(weather_url, params=query)
data = response.json()

# print(data)

# grab the temp from the dictionary
temp = data['main']['temp']
print(f'The current temperature in Minneapolis is {temp}F')