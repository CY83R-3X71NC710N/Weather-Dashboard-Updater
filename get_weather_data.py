import csv
import requests
import os

# Set the city and country code for which you want to get the weather information
city = "milwaukee"
country_code = "us"

# Construct the API URL using the environment variable as the API key
url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={os.environ['API_KEY']}"

# Send the API request
response = requests.get(url)

# Get the weather data
weather_data = response.json()

# Extract the data you want to save to the CSV file
data = {
    "date": weather_data.get("dt", "N/A"),
    "temperature": weather_data["main"].get("temp", "N/A"),
    "feels_like": weather_data["main"].get("feels_like", "N/A"),
    "humidity": weather_data["main"].get("humidity", "N/A"),
    "wind_speed": weather_data["wind"].get("speed", "N/A"),
    "wind_deg": weather_data["wind"].get("deg", "N/A"),
    "visibility": weather_data.get("visibility", "N/A"),
    "cloud_coverage": weather_data["clouds"].get("all", "N/A"),
    "sunrise_time": weather_data["sys"].get("sunrise", "N/A"),
    "sunset_time": weather_data["sys"].get("sunset", "N/A"),
    "weather_description": weather_data["weather"][0].get("description", "N/A"),
    "weather_icon": weather_data["weather"][0].get("icon", "N/A"),
}

# Save the data to a CSV file
with open("weather.csv", "a") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=data.keys())
    writer.writerow(data)
