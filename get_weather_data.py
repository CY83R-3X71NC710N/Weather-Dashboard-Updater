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
data = {}

for key, value in weather_data.items():
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            data[sub_key] = sub_value
    else:
        data[key] = value

# Save the data to a CSV file
with open("weather.csv", "a") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=data.keys())
    writer.writerow(data)
