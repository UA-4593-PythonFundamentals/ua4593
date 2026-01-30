import math

def rec_area(length: int | float, width: int | float) -> float:
  """
  Calculate the area of a rectangle.
  """
  return length * width

def triangle_area(base: int | float, height: int | float) -> float:
  """
  Calculate the area of a triangle.
  """
  return 0.5 * base * height

def circle_area(radius: int | float) -> float:
  """
  Calculate the area of a circle.
  """
  return math.pi * radius ** 2

def main():
  while True:
    try:
      shape = input("Enter shape (rectangle, triangle, circle) or 'exit' to quit: ").strip().lower()

      if shape == 'exit':
        break
      elif shape == 'rectangle':
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = rec_area(length, width)
        print(f"Area of rectangle: {area}")
      elif shape == 'triangle':
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = triangle_area(base, height)
        print(f"Area of triangle: {area}")
      elif shape == 'circle':
        radius = float(input("Enter radius: "))
        area = circle_area(radius)
        print(f"Area of circle: {area}")
    except ValueError:
      print("Unknown shape. Please try again.")

if __name__ == "__main__":
  main()