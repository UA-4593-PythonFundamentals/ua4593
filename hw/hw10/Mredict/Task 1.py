class Polygon:
    def __init__(self, sides):
        self.sides = sides
        self.lengths = []

    def input_lengths(self):
        for i in range(self.sides):
            self.lengths.append(float(input(f"Enter length of side {i + 1}: ")))
    
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.lengths = [length, width, length, width]

    def square(self):
        return self.lengths[0] * self.lengths[1]
    
# Example usage
number_of_sides = int(input("Enter number of sides of the polygon: "))
if number_of_sides == 4:
    length = float(input("Enter length of the rectangle: "))
    width = float(input("Enter width of the rectangle: "))
    rectangle = Rectangle(length, width)
    print(f"Area of the rectangle: {rectangle.square()}")
else:
    polygon = Polygon(number_of_sides)
    polygon.input_lengths()
    print(f"Sides lengths: {polygon.lengths}")
