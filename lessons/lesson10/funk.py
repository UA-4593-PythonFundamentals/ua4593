def create_car(make, model, year):
    return {"make": make, "model": model, "year": year}

def display_info(car):
    return f"{car['year']} {car['make']} {car['model']}"
def honk(self):
    return "Beep beep!"
def repaint(self, new_color):
    self["color"] = new_color
    return f"The car has been repainted to {self["color"]}."
def age(self, current_year):
    return current_year - self["year"]
    
if __name__ == "__main__":
    car = create_car("Toyota", "Corolla", 2015)
    print(car["make"], car["model"], car["year"])  # Output: Toyota Corolla 2015
    print(display_info(car))  # Output: 2015 Toyota Corolla
    print(honk(car))          # Output: Beep beep!
    print(repaint(car, "Blue")) # Output: The car has been repainted to Blue.
    print(age(car, 2024))       # Output: 9
    print("-----")
    car2 = create_car("Honda", "Civic", 2018)
    print(display_info(car2)) # Output: 2018 Honda Civic
    print(honk(car2))         # Output: Beep beep!
    print(repaint(car2, "Red")) # Output: The car has been repainted to Red.
    print(age(car2, 2024))      # Output: 6