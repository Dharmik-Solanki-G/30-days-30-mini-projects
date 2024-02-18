import tkinter as tk
import requests
  
def fetch_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    api_key = '30d4741c779ba94c470ca1f63045390a'
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

    if weather_data.status_code == 200:
        weather_json = weather_data.json()
        if weather_json.get('cod') == 200:
            weather = weather_json['weather'][0]['main']
            temp = round(weather_json['main']['temp'])
            update_ui(city, weather, temp)
        else:
            result_label.config(text=f"City not found: {city}")
    else:
        result_label.config(text="Failed to fetch weather data. Please try again later.")

def update_ui(city, weather, temp):
    result_label.config(text=f"The weather in {city} is: {weather}\nThe temperature in {city} is: {temp}°C")
    color = get_color(weather)
    root.config(bg=color)
    result_label.config(bg=color)

def get_color(weather):
    if weather.lower() == 'clear':
        return '#87CEEB'  # Sky Blue
    elif weather.lower() == 'clouds':
        return '#A9A9A9'  # Dark Gray
    elif weather.lower() == 'rain':
        return '#4682B4'  # Steel Blue
    elif weather.lower() == 'thunderstorm':
        return '#800080'  # Purple
    elif weather.lower() == 'snow':
        return '#FFFFFF'  # White
    elif weather.lower() == 'mist' or weather.lower() == 'haze' or weather.lower() == 'fog':
        return '#D3D3D3'  # Light Gray
    elif weather.lower() == 'smoke':
        return '#696969'  # Dim Gray
    elif weather.lower() == 'dust' or weather.lower() == 'sand':
        return '#FFD700'  # Gold
    elif weather.lower() == 'tornado':
        return '#FF0000'  # Red
    else:
        return '#FFFFFF'  # White

# GUI
root = tk.Tk()
root.title("Weather App")

# City Entry
city_label = tk.Label(root, text="Enter City Name:", font=("Helvetica", 14))
city_label.grid(row=0, column=0, padx=10, pady=10)
city_entry = tk.Entry(root, font=("Helvetica", 14), bd=2, relief="solid")
city_entry.grid(row=0, column=1, padx=10, pady=10)

# Fetch Button
fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather, font=("Helvetica", 14), bd=2, relief="raised")
fetch_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 14), bd=2, relief="solid", wraplength=400, justify="left")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
