# 🌍 AI for SDG 13: Predicting CO₂ Levels Using Weather Data

## 🔥 Project Overview

This project demonstrates how **machine learning** and **real-time weather data** can be combined to predict **carbon dioxide (CO₂) pollution levels**, helping communities understand and respond to climate-related risks.

✅ **SDG Focus**: Sustainable Development Goal 13 — *Climate Action*

---

## 🧠 Problem Statement

CO₂ emissions contribute heavily to climate change, but many regions lack affordable or accessible air pollution monitoring tools. By predicting CO₂ levels using basic weather features (temperature, humidity, wind speed), we offer a low-cost AI-driven estimation approach that can guide local climate action.

---

## 🤖 Solution Summary

We built a simple **Linear Regression** model that:
- Collects **live weather data** from OpenWeatherMap API
- Simulates CO₂ levels to build a training dataset
- Trains an ML model to predict CO₂ based on weather conditions
- Outputs CO₂ levels based on **today’s weather** in any city

---

## 🔧 Tech Stack

- **Python** 🐍
- **VS Code** 💻
- **OpenWeatherMap API**
- **Pandas & Scikit-learn**
- **Joblib** (for saving models)
- **CSV** (for dataset storage)

---

## 📂 Project Structure

climate_ai_project/
│
├── generate_data.py # Collects weather + simulated CO₂ data
├── train_model.py # Trains and saves the ML model
├── predict_today.py # Predicts CO₂ for current weather
├── weather_co2_data.csv # The dataset used for training
├── co2_predictor_model.pkl# Saved trained model
└── README.md # Project documentation
