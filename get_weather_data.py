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

# Check if the "main" key exists in the weather data
if "main" in weather_data:
    main_data = weather_data["main"]

    # Extract the data you want to save to the CSV file
    data = {
        "date": weather_data.get("dt", "N/A"),
        "temperature": main_data.get("temp", "N/A"),
        "humidity": main_data.get("humidity", "N/A"),
        "wind_speed": weather_data["wind"].get("speed", "N/A"),
        "min_temp": main_data.get("temp_min", "N/A"),
        "max_temp": main_data.get("temp_max", "N/A"),
        "pressure": main_data.get("pressure", "N/A"),
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
else:
    print("Error: Unable to retrieve weather data.")

