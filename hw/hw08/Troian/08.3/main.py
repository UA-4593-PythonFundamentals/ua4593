import module

print("Test\n--------------------------------------------")
print(module.area_of_rectangle(10,10))

print(module.area_of_triangle(10,10))

print(module.area_of_circle(10))
print("--------------------------------------------")


print("--------------------------------------------\nRectangle:")
print(module.area_of_rectangle(int(input("Enter side a:")),int(input("Enter side b:"))))

print("--------------------------------------------\nTriangle:")
print(module.area_of_triangle(int(input("Enter side a:")),int(input("Enter height:"))))

print("--------------------------------------------\nCircle:")
print(module.area_of_circle(int(input("Enter radius:"))))
print("--------------------------------------------")