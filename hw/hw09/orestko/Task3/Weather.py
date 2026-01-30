import tkinter as tk
from tkinter import messagebox
from pyowm import OWM

# -------------------
# Налаштування PyOWM
# -------------------
API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

# -------------------
# Функція отримання погоди
# -------------------
def get_weather():
    city = entry_field.get()
    if not city:
        messagebox.showwarning("Помилка", "Введіть місто!")
        return
    
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        temp = w.temperature('celsius')['temp']
        status = w.detailed_status
        humidity = w.humidity
        wind = w.wind()['speed']

        label.config(text=f"Місто: {city}\n"
                          f"Температура: {temp}°C\n"
                          f"Стан: {status}\n"
                          f"Вологість: {humidity}%\n"
                          f"Швидкість вітру: {wind} м/с")
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося отримати погоду:\n{e}")


# -------------------
# Створення GUI
# -------------------
HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Верхня рамка для введення міста
frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)  


# Нижня рамка для відображення результату
lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()