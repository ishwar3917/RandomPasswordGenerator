# Set up and Test Api

import requests
import os
from dotenv import load_dotenv

# Load env
load_dotenv()

# Get the API KEY
api_key = os.getenv("API_KEY")


while True:

    try:
        city_name = input("Enter city name : ").strip()
    except (KeyboardInterrupt, EOFError):
        print("Enter correct city name ")
        continue
    if city_name == "":
        print("Please enter a city name ")
        continue

    try:
        # &units=metric because of this temperature is getting in celsius
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        )
        data = response.json()
    except requests.exceptions.RequestException as e:
        print("Network or API error ", e)
        continue
    if str(data.get("cod")) != "200":
        print("Enter a valid city name")
    else:
        break

# Print raw json

print(data)

# Temperature

print(f"\nTemperature of {city_name} is : {data['main']['temp']}°C")
print(f"\nFeel like Temperature of {city_name} is : {data['main']['feels_like']}°C")
print(
    f"\nDescription of weather in {city_name} is : {data['weather'][0]['description']}"
)
print(f"\nHumidity in {city_name} is : {data['main']['humidity']}% ")
print(f"\nWind speed in {city_name} is : {data['wind']['speed']}m/s ")
