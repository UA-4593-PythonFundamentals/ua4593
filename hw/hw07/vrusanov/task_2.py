def mainProgram():
    input_number = int(input("Enter one of the numbers 1 - rectangle, 2 - triangle, 3 - circle: "))
    if input_number == 1:
        result = rectangle()
        print(f"The area of the rectangle is {result}")
    elif input_number == 2:
        result = triangle()
        print(f"The area of the triangle is {result}")
    elif input_number == 3:
        result = circle()
        print(f"The area of the circle is {result}")
    else:
        print("Invalid input")

def rectangle():
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    area = width * height
    return area

def triangle():
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    return area

def circle():
    radius = int(input("Enter the radius of the circle: "))
    area = 3.14 * radius * radius
    return area

mainProgram()