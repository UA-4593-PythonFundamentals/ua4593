import math
def rect_area(length, width):
    """
    Return the are of a rectangle.

    Args:
        length (int or float): The length of the rectangle
        width (int or float): The width of the rectangle
    
    Returns:
        int or float: The area of the rectangle
    """
    return length * width
def triangle_area(base, height):
    """
    Return the area of a triangle.

    Args:
        base (int or float): The base of the triangle
        height (int or float): The height of the triangle

    Returns:
        int or float: The area of the triangle
    """
    return (base * height) / 2
def circle_area(radius):
    """
    Return the area of a circle.

    Args:
        radius (int or float): The radius of the circle
    
    Returns:
        float: the area of the circle

    """
    return math.pi * radius ** 2

print(rect_area(10, 7))
print(triangle_area(5, 7))
print(circle_area(4))