from areas import function_rectangle_area, function_triangle_area, function_circle_area 
your_choice = input("Enter figure (rectangle, triangle, circle): ").lower()

if your_choice == "rectangle":
    a = float(input("Enter length of rectangle: "))
    b = float(input("Enter width of rectangle: "))
    print(f"Area of rectangle: {round(function_rectangle_area(a, b), 2)}")

elif your_choice == "triangle": 
    a = float(input("Enter base of triangle: "))
    h = float(input("Enter height of triangle: "))
    print(f"Area of triangle: {round(function_triangle_area(a, h), 2)}")

elif your_choice == "circle":
    r = float(input("Enter radius of circle: "))
    print(f"Area of circle: {round(function_circle_area(r), 2)}")
