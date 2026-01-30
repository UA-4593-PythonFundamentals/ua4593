import math
def rectangle_area (a, b):
  """This function calculates the area of rectangle"""
  result = a * b
  return result

def triangle_area (a, b, c):
  """This function calculates the area of triangle"""
  p = (a + b + c) / 2
  result = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
  return result

def circle_area (r):
  """This function calculates the area of circle"""
  result = round(math.pi * (r ** 2), 2)
  return result

choice = input("Choise the figure: ")
if choice == "rectangle":
  a = int(input("Enter a side a: "))
  b = int(input("Enter a side b: "))
  print("Area of rectangle = ", rectangle_area(a, b))

elif choice == "triangle":
  a = int(input("Enter a side a: "))
  b = int(input("Enter a side b: "))
  c = int(input("Enter a side c: "))
  print("Area of triangle = ", triangle_area(a, b, c))

elif choice == "circle":
  r = int(input("Enter a radius: "))
  print("Area of circle = ", circle_area(r))
