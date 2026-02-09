from math import pow, pi

def rectangle_area(a, b):
    """
    Calculate the area of a rectangle.
    Args:
        a (float): Length of the rectangle.
        b (float): Width of the rectangle.
    Returns:
        Area of the rectangle.
    """
    return a * b

def triangle_area(a, h):
    """
    Calculate the area of a triangle.
    Args:
        a (float): Length of the base of the triangle.
        h (float): Height of the triangle.
    Returns:
        Area of the triangle.
    """
    return 0.5 * a * h

def circle_area(r):
    """
    Calculate the area of a circle.
    Args:
        r (float): Radius of the circle.
    Returns:
        Area of the circle.
    """
    return pi * pow(r, 2)