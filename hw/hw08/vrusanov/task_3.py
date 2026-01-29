from area_calculator import rectangle_area, triangle_area, circle_area
from math import pi


def display_menu():
    print("\n" + "=" * 50)
    print("Area Calculator")
    print("=" * 50)
    print("Choose a figure to calculate its area:")
    print("1. Rectangle (S = a * b)")
    print("2. Triangle (S = 0.5 * h * a)")
    print("3. Circle (S = pi * r ** 2)")
    print("4. Exit")
    print("=" * 50)


def get_positive_number(prompt):
    """
    Get a positive number from user input.
    
    Args:
        prompt (str): The prompt message to display
        
    Returns:
        float: A positive number entered by the user
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid number.")


def calculate_rectangle():
    print("\n--- Rectangle Area Calculator ---")
    a = get_positive_number("Enter the length of side a: ")
    b = get_positive_number("Enter the length of side b: ")
    area = rectangle_area(a, b)
    print(f"\nResult: The area of the rectangle is {area:.2f}")


def calculate_triangle():
    print("\n--- Triangle Area Calculator ---")
    h = get_positive_number("Enter the height (h): ")
    a = get_positive_number("Enter the base (a): ")
    area = triangle_area(h, a)
    print(f"\nResult: The area of the triangle is {area:.2f}")


def calculate_circle():
    print("\n--- Circle Area Calculator ---")
    r = get_positive_number("Enter the radius (r): ")
    area = circle_area(r)
    print(f"\nResult: The area of the circle is {area:.2f}")
    print(f"(Using pi = {pi:.6f})")


def main():
    print("\nWelcome to the Area Calculator!")
    print(f"This program uses the math module (pi = {pi:.6f})")
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            calculate_rectangle()
        elif choice == '2':
            calculate_triangle()
        elif choice == '3':
            calculate_circle()
        elif choice == '4':
            print("\nThank you for using the Area Calculator. Goodbye!")
            break
        else:
            print("\nError: Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()

