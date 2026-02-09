import areas

def area_calculate_program():
    """
    Calculate and print the area based on the user's shape choice.
    """
    print('Choose a shape:\n 1. Rectangle\n 2. Triangle\n 3. Circle')

    choice = int(input('Enter the number of your choice: '))

    match choice:
        case 1:
            length = float(input('Enter the length of the rectangle: '))
            width = float(input('Enter the width of the rectangle: '))
            
            print(f'Area of the rectangle: {areas.rectangle_area(length, width)}')
        case 2:
            base = float(input('Enter the base of the triangle: '))
            height = float(input('Enter the height of the triangle: '))

            print(f'Area of the triangle: {areas.triangle_area(base, height)}')
        case 3:
            radius = float(input('Enter the radius of the circle: '))

            print(f'Area of the circle: {areas.circle_area(radius)}')
        case _:
            print('Wrong number of shape.')
    
if __name__ == "__main__":
    area_calculate_program()