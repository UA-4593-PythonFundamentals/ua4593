class polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height

    def area(self):
        return 0.5 * self.width * self.height
rect = Rectangle(10, 5)
print(f"Площа прямокутника: {rect.area()}")