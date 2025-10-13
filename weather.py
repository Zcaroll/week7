import requests

# api for current weather in minneapolis
weather_url = 'https://api.openweathermap.org/data/2.5/weather?q=minneapolis,mn,us&units=imperial&appid=2bd00eeb43f1c08033f6d59a07cc60ac'

response = requests.get(weather_url)
data = response.json()

print(data)

temp = data['main']['temp']
print(temp)