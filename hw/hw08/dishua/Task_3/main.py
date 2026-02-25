import area_calc

def main():
    while True:
        print("What area do you want to calculate? Possible values are 'rectangle','triangle' or 'circle'")
        figure = input().strip().lower()

        if figure in ["rectangle"]:
            area_calc.calculate_rectangle_area()
        elif figure in ["triangle"]:
            area_calc.calculate_triangle_area()
        elif figure in ["circle"]:
            area_calc.calculate_cirlce_area()
        else:
            break

if __name__ == "__main__":
    main()