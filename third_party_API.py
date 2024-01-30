import requests
import json
'''
A third party API is less customizable but can be more powerful.
typically these APIs require an API key (stored in .env for now) that can be retrieved from their website.
You can stack your own logic on top of another API to add more functionality or you can just use theirs as is.

In this example I am getting weather data from a weather API. This will return to me the data of weather from a city that
I request from.
'''


def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."

        elif response.status_code == 404:
            return f"City not found: {city}"

        else:
            return f"Error: {data['message']}"

    except requests.RequestException as e:
        return f"Error: {e}"

# Replace 'your_api_key' with your actual OpenWeatherMap API key
api_key = 'your_api_key'
query_string = input("Enter the city for weather information: ")

result = get_weather(api_key, query_string)
print(result)
