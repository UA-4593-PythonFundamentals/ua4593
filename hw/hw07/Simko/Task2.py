def function_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width


def function_triangle_area(base, height):
    """Calculate the area of a triangle."""
    return (base * height) / 2


def function_circle_area(radius):
    """Calculate the area of a circle."""
    import math
    return math.pi * radius ** 2

#######3######Головна программа############

your_choice = input("Enter figure (rectangle, triangle, circle): ")

if your_choice == "rectangle":
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    print(f"Area of rectangle: {round(function_rectangle_area(length, width), 2)}")
elif your_choice == "triangle":
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    print(f"Area of triangle: {round(function_triangle_area(base, height), 2)}")
elif your_choice == "circle":
    radius = float(input("Enter radius of circle: "))
    print(f"Area of circle: {round(function_circle_area(radius), 2)}")

