import csv
import requests

# Set your API key here
api_key = "3076487f690bacceb693d2eb90b87f1e"

# Set the city and country code for which you want to get the weather information
city = "London"
country_code = "uk"

# Construct the API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}"

# Send the API request
response = requests.get(url)

# Get the weather data
weather_data = response.json()

# Extract the data you want to save to the CSV file
data = {
    "date": weather_data["dt"],
    "temperature": weather_data["main"]["temp"],
    "humidity": weather_data["main"]["humidity"],
    "wind_speed": weather_data["wind"]["speed"]
}

# Save the data to a CSV file
with open("weather.csv", "a") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=data.keys())
    writer.writerow(data)
