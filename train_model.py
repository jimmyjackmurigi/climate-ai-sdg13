import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Step 1: Load the dataset
df = pd.read_csv("weather_co2_data.csv")

# Step 2: Split into features (X) and target (y)
X = df[["temperature", "humidity", "wind_speed"]]
y = df["co2_ppm"]

# Step 3: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("✅ Model trained!")
print(f"📉 MAE: {mae:.2f}")
print(f"📈 R² Score: {r2:.2f}")

# Step 6: Save the model
joblib.dump(model, "co2_predictor_model.pkl")
print("💾 Model saved as 'co2_predictor_model.pkl'")
