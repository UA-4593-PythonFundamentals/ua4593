import tkinter as tk
from tkinter import font
from OWM import get_weather

HEIGHT = 500
WIDTH = 500


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="white")
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="dark blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.80, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12, 'bold'))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

def show_weather():
    city = entry_field.get()
    status, wind, humidity, temperature, rain, heat_index, clouds = get_weather(city)
    text = (
        f"{city}\n"
        f"Status: {status}\n"
        f"Wind: {wind['speed']} m/s, {wind['deg']}°\n"
        f"Humidity: {humidity}\n"
        f"Temperature: {temperature['temp']}°C, {temperature['temp_max']}°C, {temperature['temp_min']}°C\n"
        f"Rain: {rain.get('3h', 0)}\n"
        f"Heat Index: {heat_index}\n"
        f"Clouds: {clouds}"
    )
    label["text"] = text

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="black", 
                   font=('Courier', 8), 
                   command=show_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

print(get_weather("Kyiv"))

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

