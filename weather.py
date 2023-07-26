import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

def get_weather_condition(city="Lagos"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print("*** Get Weather Condition ***")
    city = input("\nEnter a city to get its current weather\n")

    # check if an empty string is submitted
    if not bool(city.strip()):
        city = "Lagos"
    weather_data = get_weather_condition(city)

    print("\n")
    pprint(weather_data)