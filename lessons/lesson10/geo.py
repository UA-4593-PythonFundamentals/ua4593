import random
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)** 0.5

    def __repr__(self):
        return f"({self.x}, {self.y})"
    
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def __str__(self):
        return f"{self.__class__.__name__:<12} Area: {self.area():<8} Perimeter: {self.perimeter()}"

class Rectangle(Shape):
    def __init__(self, bottom_left: Point, top_right: Point):
        self.bottom_left = bottom_left
        self.top_right = top_right

    def area(self):
        width = self.top_right.x - self.bottom_left.x
        height = self.top_right.y - self.bottom_left.y
        return width * height

    def perimeter(self):
        width = self.top_right.x - self.bottom_left.x
        height = self.top_right.y - self.bottom_left.y
        return 2 * (width + height)
    def __str__(self):
        return f"{super().__str__()} Bottom Left: {self.bottom_left} Top Right: {self.top_right}"
    
class Circle(Shape):
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius
    def __str__(self):
        return f"{super().__str__()} Center: {self.center} Radius: {self.radius}"
    
class CircleColor(Circle):
    def __init__(self, center: Point, radius: float, color: str):
        super().__init__(center, radius)
        self.color = color
    def __str__(self):
        return f"{super().__str__()} Color: {self.color}"
    
# Example usage:
if __name__ == "__main__":
    shapes = []
    for _ in range(6):
        shape = None
        p1 = Point(random.randint(0, 10), random.randint(0, 10))
        p2 = Point(random.randint(0, 10), random.randint(0, 10))
        r = random.randint(1, 5)
        r_color = random.choice(["Red", "Green", "Blue"])
        print(f"Generated Points: p1={p1}, p2={p2}, Color={r_color}")
        match random.choice(["Rectangle", "Circle", "CircleColor"]):
            case "Rectangle":
                shape = Rectangle(p1, p2)
            case "Circle":
                shape = Circle(p1, r)
            case "CircleColor":
                shape = CircleColor(p1, r, r_color)
        shapes.append(shape)
    print("Shapes information:")
    for shape in shapes:
        print(shape)