import pandas as pd
import random

# Simulate 50 weather + CO2 rows
data = []

for _ in range(50):
    temp = random.uniform(15, 35)            # Temperature in °C
    humidity = random.uniform(30, 90)        # %
    wind_speed = random.uniform(0, 10)       # m/s
    # Simulated CO2 ppm based on temp/humidity/wind
    co2 = 400 + (temp * 2) + (humidity * 0.5) - (wind_speed * 1.5)
    
    data.append({
        "temperature": round(temp, 2),
        "humidity": round(humidity, 2),
        "wind_speed": round(wind_speed, 2),
        "co2_ppm": round(co2, 2)
    })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("weather_co2_data.csv", index=False)
print("✅ Dataset saved as 'weather_co2_data.csv'")
