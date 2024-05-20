import tkinter as tk
from tkinter import messagebox
import requests

def fetch_weather(location):
    #OpenWeatherMap API key
    api_key = 'eedc59f239d20e60a4a0bf1207ca7b6c'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            messagebox.showerror("Error", data['message'])
            return None
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

def display_weather_gui(data):
    if data:
        city = f"{data['name']}, {data['sys']['country']}"
        temperature = f"Temperature: {data['main']['temp']}°C"
        humidity = f"Humidity: {data['main']['humidity']}%"
        conditions = f"Weather Conditions: {data['weather'][0]['description']}"

        root = tk.Tk()
        root.title("Weather Information")

        tk.Label(root, text=city).pack()
        tk.Label(root, text=temperature).pack()
        tk.Label(root, text=humidity).pack()
        tk.Label(root, text=conditions).pack()

        root.mainloop()
    else:
        messagebox.showerror("Error", "Weather data not available.")

def main():
    location = input("Enter city or ZIP code: ")
    weather_data = fetch_weather(location)
    display_weather_gui(weather_data)

if __name__ == "__main__":
    main()
