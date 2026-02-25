class Polygon:
    def info(self):
        print(f'I am a {self.__class__.__name__}')

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))
    
rect = Rectangle(length, width)

print(f'Rectangle area is: {rect.area()}')
rect.info()