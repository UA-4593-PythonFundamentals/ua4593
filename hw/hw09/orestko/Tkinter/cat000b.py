from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import time
import os

root = Tk()                         # створюєм корневий об'єкт - вікно
root.geometry('400x300')            # встановлюємо розміри вікна
root.title("CAT")                   # встановлюємо заголовок вікна

script_dir = os.path.dirname(os.path.abspath(__file__))

icon = PhotoImage(file=os.path.join(script_dir, "iconCat.png")) # альтернативна опція встановлення іконки
root.iconphoto(False, icon)         # альтернативна опція встановлення іконки

logo = PhotoImage(file=os.path.join(script_dir, "cat.png"))   # створюємо об'єкт зображення
logo1 = Label(image=logo)           # створюємо об'єкт зображення 

game = 3  # умова продовження гри
healthCat = 20  # "здоров'я,"
leisureCat = 20  # leisure - "задоволення"
def update_clock():
    ''' функція, яка відповідає за оновлення ігрової ситуації раз на секунду '''
    heppimin()
    try:
        root.after(1000, update_clock)
    except:
        pass


def heppimin():
    global healthCat  # працюємо з глобальними аргументами
    global leisureCat  # працюємо з глобальними аргументами
    
    healthCat = healthCat - 3  # кожної ітерації параметр "здоров'я," зменшується на 3
    leisureCat = leisureCat - 3  # кожної ітерації параметр "задоволення" зменшується на 3
    
    l1.configure(text="health - " + str(healthCat) + "%")  
    l2.configure(text="leisure - " + str(leisureCat) + "%") 

    if healthCat <= 0 or leisureCat <= 0:
        answer = mb.askyesno(title="You lost", message="Do you want to play again?")
        if answer == True:
            healthCat = 50
            leisureCat = 50
        else:
            root.destroy()
            return
    elif healthCat >= 100 and leisureCat >= 100:
        answer2 = mb.askyesno(title="You win", message="Do you want to play again?")
        if answer2 == True:
            healthCat = 50
            leisureCat = 50
        else:
            root.destroy()
            return
def health():
    global healthCat
    global leisureCat
    healthCat = healthCat + 10
    leisureCat = leisureCat - 2
    l1.configure(text="health - " + str(healthCat) + "%")
    l2.configure(text="leisure - " + str(leisureCat) + "%")
    l3.configure(text="your cat is healthy")
    if leisureCat <= 10:
        mb.showerror("sorry", "your cat is sad")

def leisure():
    global healthCat
    global leisureCat
    healthCat = healthCat - 2
    leisureCat = leisureCat + 10
    l1.configure(text="health - " + str(healthCat) + "%")
    l2.configure(text="leisure - " + str(leisureCat) + "%")
    l3.configure(text="your cat is happy")
    if healthCat <= 10:
        mb.showerror("sorry", "your cat is ill")


label2= Label(width=27,height=3, text = "It is your Cat", font="Arial")
b1 = ttk.Button(width=15,text="feed", command=health)   # годувати
b2 = ttk.Button(width=15,text="caress", command=leisure) # пестити
b3 = ttk.Button(width=15,text="train", command=health)  # виховувати, тренувати
b4 = ttk.Button(width=15,text="play", command=leisure)   # грати

l1 = Label(width=20,height=3, text = "health - " + str(healthCat) + "%")          # здоров'я, 
l2 = Label(width=20,height=2, text = "leisure - " + str(leisureCat) + "%")         # задоволення, дозвілля
l3 = Label(width=20,height=2, text = "your cat is healthy") # здоровий

label2.grid(row=0, column=2,columnspan=3,rowspan=2)
b1.grid(row=2, column=0)
b2.grid(row=3, column=0)
b3.grid(row=4, column=0)
b4.grid(row=5, column=0)
l1.grid(row=6, column=0)
l2.grid(row=7, column=0)
l3.grid(row=7, column=3)
logo1.grid(row=2, column=2,columnspan=5,rowspan=5)

update_clock()
root.mainloop()		    # Для відображення вікна треба викликати в нього метод mainloop() , який запускає цикл обробки 	подій вікна взаємодії з користувачем.
