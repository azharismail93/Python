# GUI
import tkinter as tk
from tkinter import messagebox 
# HTTP Requests
import requests

# API Setup
API_KEY = "735d34c4d1332e5b2f9dd024440449db"
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Fetch Weather Data
def fetch_weather():
    # Get city name from user input in GUI
    city_name = city_entry.get()
    # Check if city name is empty
    if not city_name:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raises error for bad responses
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            city = data['name']
            weather = data['weather'][0]['description'] 
            result_label.config(text=f"Current temperature in {city} is {temperature}°C with {weather}.")
        else:
            messagebox.showwarning(f"{response.status_code}: Unable to fetch weather data.")
    except Exception as e:
        messagebox.showwarning("An error occurred", e)
    
# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x100")

tk.Label(root, text="Enter City Name:").grid(row=0, column=0, padx=3, pady=10)
city_entry = tk.Entry(root, width=15)
city_entry.grid(row=0, column=1, padx=5, pady=10)

tk.Button(root, text="Get Weather", command=fetch_weather).grid(row=0, column=2, padx=3, pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=1, column=0, columnspan=10, pady=10)

root.mainloop()