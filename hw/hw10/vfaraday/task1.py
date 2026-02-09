class Polygon:
    pass

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

rect = Rectangle(10, 5)
print(f"Rectangle Area: {rect.get_area()}")
print(f"Is rect a Polygon? {isinstance(rect, Polygon)}")