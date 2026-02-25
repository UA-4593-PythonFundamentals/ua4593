class Polygon:

    def __init__(self):
        pass
        
class Rectangle(Polygon):

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b
    
rect = Rectangle(3, 4)
print(f"Area is: {rect.square()}")