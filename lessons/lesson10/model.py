class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    def honk(self):
        return "Beep beep!"
    def repaint(self, new_color):
        self.color = new_color
        return f"The car has been repainted to {self.color}."
    def age(self, current_year):
        return current_year - self.year
    
if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 2015)
    print(car.make, car.model, car.year)  # Output: Toyota Corolla 2015
    print(car.display_info())  # Output: 2015 Toyota Corolla
    print(car.honk())          # Output: Beep beep!
    print(car.repaint("Blue")) # Output: The car has been repainted to Blue.
    print(car.age(2024))       # Output: 9
    print("-----")
    car2 = Car("Honda", "Civic", 2018)
    print(car2.display_info()) # Output: 2018 Honda Civic
    print(Car.display_info(car2)) # Output: 2018 Honda Civic
    print(car2.honk())         # Output: Beep beep!
    print(Car.honk(car2))         # Output: Beep beep!
    print(car2.repaint("Red")) # Output: The car has been repainted to Red.
    print(car2.age(2024))      # Output: 6
