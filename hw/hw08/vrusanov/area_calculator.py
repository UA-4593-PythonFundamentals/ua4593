
from math import pow, pi


def rectangle_area(a, b):
    """
    Calculate the area of a rectangle.
    Formula: S = a * b
    Args:
        a (float): Length of the first side
        b (float): Length of the second side
    Returns:
        float: Area of the rectangle
    """
    return a * b


def triangle_area(h, a):
    """
    Calculate the area of a triangle.
     Formula: S = 0.5 * h * a
    Args:
        h (float): Height of the triangle
        a (float): Base of the triangle
        Returns:
        float: Area of the triangle
    """
    return 0.5 * h * a


def circle_area(r):
    """
    Calculate the area of a circle.
    Formula: S = pi * r ** 2
    Args:
        r (float): Radius of the circle
        Returns:
        float: Area of the circle
    """
    return pi * pow(r, 2)

