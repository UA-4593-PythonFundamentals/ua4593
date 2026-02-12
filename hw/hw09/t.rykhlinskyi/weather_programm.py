import tkinter as tk
from pyowm import OWM
from tkinter import messagebox

# --- Логіка Weather API ---
API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather():
    city = entry_field.get() # Отримуємо назву міста з поля вводу
    if not city:
        messagebox.showwarning("Warning", "Please enter a city name")
        return

    try:
        # Шукаємо погоду
        observation = mgr.weather_at_place(city)
        w = observation.weather
        
        # Форматуємо дані для виводу
        status = w.detailed_status
        temp = w.temperature('celsius')['temp']
        wind = w.wind()['speed']
        humidity = w.humidity
        
        final_str = f"City: {city}\nConditions: {status}\nTemp: {temp}°C\nWind: {wind} m/s\nHumidity: {humidity}%"
        label['text'] = final_str
        
    except Exception:
        # Якщо місто не знайдено або інша помилка
        label['text'] = "Error:\nCity not found"

# --- Створення GUI (Tkinter) ---
HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Верхня частина (поле вводу та кнопка)
frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=get_weather) # Викликаємо нашу функцію
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

# Нижня частина (вивід інформації)
lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), justify='left', anchor='nw')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()