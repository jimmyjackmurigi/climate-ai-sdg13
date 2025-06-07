import requests
import joblib

# Load your model
model = joblib.load("co2_predictor_model.pkl")

# Get today's weather
api_key = "d7eea1d8e1ea9e3b99358cd4750e0b57"  # Your actual key
city = "Nairobi"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

# Extract features
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]

# Make prediction
features = [[temperature, humidity, wind_speed]]
predicted_co2 = model.predict(features)[0]

print(f"📍 Weather in {city}")
print(f"🌡️ Temperature: {temperature}°C")
print(f"💧 Humidity: {humidity}%")
print(f"🍃 Wind Speed: {wind_speed} m/s")
print(f"\n🔮 Predicted CO₂ Level: {predicted_co2:.2f} ppm")
