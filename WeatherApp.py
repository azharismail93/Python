# GUI
import tkinter as tk
from tkinter import messagebox 
# HTTP Requests
import requests

# API Setup
API_KEY = "735d34c4d1332e5b2f9dd024440449db"
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Fetch Weather Data
def fetch_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        city = data['name']
        weather = data['weather'][0]['description'] 
        print(f"Current temperature in {city} is {temperature}°C with {weather}.")
    else:
        return response.status_code
    
if __name__ == "__main__":
    print("##### Weather App #####")
    city = input("Enter the city name to get the current weather: ")
    fetch_weather(city)