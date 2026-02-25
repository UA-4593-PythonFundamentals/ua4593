import module_area as module

Question = str(input("Enter name of figure to calculate area:"))   
if Question == 'rectangle':
    width = float(input("Enter width of rectangle:"))
    height = float(input("Enter height of rectangle:"))
    module.rectangle_area(width, height)
    print(f"Area of rectangle is {module.rectangle_area(width, height)}")
elif Question == 'triangle':
    width = float(input("Enter width of triangle: "))
    height = float(input("Enter height of triangle: "))
    module.triangle_area(width, height)
    print(f"Area of triangle is {module.triangle_area(width, height)}")
elif Question == 'circle':
    radius = float(input("Enter radius of circle: "))
    module.circle_area(radius)
    print(f"Area of circle is {module.circle_area(radius)}")
else:
    print("Invalid input")