from areas import area_of_circle, area_of_rectangle, area_of_triangle

def main():
    
    input_type = input("Enter the shape (rectangle, triangle, circle): ").strip().lower()
    if input_type == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {area_of_rectangle(length, width)}")
    elif input_type == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: {area_of_triangle(base, height)}") 
    elif input_type == "circle":
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {area_of_circle(radius)}")
        
if __name__ == "__main__":
    main()
    