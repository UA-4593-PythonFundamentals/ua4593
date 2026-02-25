import math

def rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): Length of the rectangle.
        width (float): Width of the rectangle.

    Returns:
        Area of the rectangle.
    """
    return length * width

def triangle_area(base, height):
    """
    Calculate the area of a triangle.

    Args:
        base (float): Length of the base of the triangle.
        height (float): Height of the triangle.

    Returns:
        Area of the triangle.
    """
    return 0.5 * base * height

def circle_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): Radius of the circle.

    Returns:
        Area of the circle.
    """
    return math.pi * (radius ** 2)

def area_calculate_program():
    """
    Calculate and print the area based on the user's shape choice.
    """
    print('Choose a shape:\n 1. Rectangle\n 2. Triangle\n 3. Circle')

    choice = int(input('Enter the number of your choice: '))

    match choice:
        case 1:
            length = float(input('Enter the length of the rectangle: '))
            width = float(input('Enter the width of the rectangle: '))
            
            print(f'Area of the rectangle: {rectangle_area(length, width)}')
        case 2:
            base = float(input('Enter the base of the triangle: '))
            height = float(input('Enter the height of the triangle: '))

            print(f'Area of the triangle: {triangle_area(base, height)}')
        case 3:
            radius = float(input('Enter the radius of the circle: '))

            print(f'Area of the circle: {circle_area(radius)}')
        case _:
            print('Wrong number of shape.')
    
area_calculate_program()