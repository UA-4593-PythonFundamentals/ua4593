def rectangle_area(length, width):
    """Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

def triangle_area(base, height):
    """Calculate the area of a triangle.

    Args:
        base (float): The base length of the triangle.
        height (float): The height of the triangle.

    Returns:
        float: The area of the triangle.
    """
    return 0.5 * base * height

def circle_area(radius):
    """Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    import math
    return math.pi * radius ** 2

print("Rectangle area (length=5, width=3):", rectangle_area(5, 3))
print("Triangle area (base=4, height=6):", triangle_area(4, 6))
print("Circle area (radius=7):", circle_area(7))