def rectangle_area(l, w):
    '''
    Calculates the area of a rectangle given its length and width.
    '''
    return l * w
def triangle_area(l, h):
    '''
    Calculates the area of a triangle given its base and height.
    '''
    return 0.5 * l * h
def circle_area(r):
    '''
    Calculates the area of a circle given its radius.
    '''
    import math
    return math.pi * r ** 2

print(">>>>>>>>>>>>>>>>>>>>>>>>>")
print("AREA CALCULATOR")
print("<<<<<<<<<<<<<<<<<<<<<<<<<")
print("Choose the operation:")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")
choice = input("Enter choice (1/2/3): ")

if choice == '1':
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area of Rectangle:", rectangle_area(length, width))

elif choice == '2':
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of Triangle:", triangle_area(base, height))

elif choice == '3':
    radius = float(input("Enter radius: "))
    print("Area of Circle:", circle_area(radius))

else:
    print("Invalid input")