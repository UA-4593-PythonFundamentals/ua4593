import module

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
    print("Area of Rectangle:", module.rectangle_area(length, width))

elif choice == '2':
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of Triangle:", module.triangle_area(base, height))

elif choice == '3':
    radius = float(input("Enter radius: "))
    print("Area of Circle:", module.circle_area(radius))
    
else:
    print("Invalid input")