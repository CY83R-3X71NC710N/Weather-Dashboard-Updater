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
#    "date": weather_data["dt"],
    "temperature": weather_data["main"]["temp"],
    "humidity": weather_data["main"]["humidity"],
    "wind_speed": weather_data["wind"]["speed"],
    "min_temp": weather_data["main"]["temp_min"],
    "max_temp": weather_data["main"]["temp_max"],
    "pressure": weather_data["main"]["pressure"],
    "visibility": weather_data.get("visibility", "N/A"),  # added this line
    "cloud_coverage": weather_data["clouds"]["all"],
    "sunrise_time": weather_data["sys"]["sunrise"],
    "sunset_time": weather_data["sys"]["sunset"],
    "weather_description": weather_data["weather"][0]["description"],
    "weather_icon": weather_data["weather"][0]["icon"],
}

# Save the data to a CSV file
with open("weather.csv", "a") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=data.keys())
    writer.writerow(data)
