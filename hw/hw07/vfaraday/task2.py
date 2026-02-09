import math

def area_rectangle(width, height):
    """Calculate rectangle area"""
    return width * height


def area_triangle(base, height):
    """Calculate triangle area"""
    return 0.5 * base * height


def area_circle(radius):
    """Calculate circle area"""
    return math.pi * radius ** 2


def main():
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Choose figure to calculate (1-3): ")

    if choice == '1':
        w = float(input("Enter width: "))
        h = float(input("Enter height: "))
        print(f"Rectangle square: {area_rectangle(w, h):.2f}")

    elif choice == '2':
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print(f"Triangle square: {area_triangle(b, h):.2f}")

    elif choice == '3':
        r = float(input("Enter radius: "))
        print(f"Circle Square: {area_circle(r):.2f}")

    else:
        print("Wrong choice")


if __name__ == "__main__":
    main()