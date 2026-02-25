import math

def calculate_rectangle_area():
    try:
        a = float(input("Enter A: "))
        b = float(input("Enter B: "))

        if a <= 0 or b <= 0:
            print("Sides must be positive numbers.\n")
            return
        
        print(f"Area of rectangle = {a * b:.2f}\n")
    except ValueError:
        print("Please enter valid numbers.\n")

def  calculate_triangle_area():
    try:
        a = float(input("Enter A: "))
        b = float(input("Enter B: "))
        c = float(input("Enter C: ")) 

        if a <= 0 or b <= 0 or c <= 0:
            print("Sides must be positive numbers.\n")
            return
            
        if a + b <= c or a + c <= b or b + c <= a:
            print("These sides cannot form a triangle.\n")
            return
        p = (a + b + c)/2
        area = math.sqrt(p*(p-a)*(p-b)*(p-c))
        print(f"Area of triangle is: {area:.2f}")
    except ValueError:
        print("Please enter valid numbers.\n")

def calculate_cirlce_area():
 while True:
     try:
        r = float(input("Enter r: "))
        if r <= 0:
            print("Sides must be positive numbers.\n")
            continue
        
        print(f"Area of circle is: {math.pi * (r ** 2):.2f}")
        break
     except ValueError:
        print("Please enter valid numbers.\n")

if __name__ == "__main__":
    print ('This module calculates the are of the defined figure')