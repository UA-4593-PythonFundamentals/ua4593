
def rectangle_area(a, b):
    '''
    Calculates the area of a rectangle given its length and width.
    '''
    return a * b
def triangle_area(a, h):
    '''
    Calculates the area of a triangle given its base and height.
    '''
    return 0.5 * a * h
def circle_area(r):
    '''
    Calculates the area of a circle given its radius.
    '''
    from math import pi, pow
    return pi * pow(r, 2)