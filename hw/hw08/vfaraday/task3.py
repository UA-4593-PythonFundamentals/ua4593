import task3Formula

def main():
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Choose figure to calculate (1-3): ")

    if choice == '1':
        w = float(input("Enter width: "))
        h = float(input("Enter height: "))
        print(f"Rectangle square: {task3Formula.rectangle_area(w, h)}")

    elif choice == '2':
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print(f"Triangle square: {task3Formula.triangle_area(b, h)}")

    elif choice == '3':
        r = float(input("Enter radius: "))
        print(f"Circle Square: {task3Formula.circle_area(r)}")

    else:
        print("Wrong choice")


if __name__ == "__main__":
    main()