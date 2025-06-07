import requests

# --- SETUP ---
API_KEY = "d7eea1d8e1ea9e3b99358cd4750e0b57"
CITY = "Nairobi"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# --- FETCH DATA ---
response = requests.get(URL)
data = response.json()

# --- EXTRACT KEY INFORMATION ---
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
description = data["weather"][0]["description"]

# --- DISPLAY ---
print(f"✅ Weather in {CITY}:")
print(f"🌡️ Temperature: {temperature} °C")
print(f"💧 Humidity: {humidity} %")
print(f"💨 Wind Speed: {wind_speed} m/s")
print(f"🌥️ Description: {description}")
