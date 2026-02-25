
def input_parameters(figure_type):
    if figure_type == 'R':
        a = int(input("Enter A side: "))
        b = int(input("Enter B side: "))
        return (a, b)
    elif figure_type == 'T':
        a = int(input("Enter A side: "))
        h = int(input("Enter H side: "))
        return (a, h)
    elif figure_type == 'C':
        r = int(input("Enter radius: "))
        return (r,)
    else:
        print("Incorrect params!")

rectangle_area = lambda a, b: a * b
triangle_area = lambda a, h: a * h / 2
circle_area = lambda r: 3.1415 * r**2

dict_functions = {"R": rectangle_area, "T": triangle_area, "C": circle_area}

figure_type = input("Choose figure: R - for rectangle; T - for triangle; C - for circle: ").upper()

my_func = dict_functions.get(figure_type)
if my_func:
    params = input_parameters(figure_type)
    print("Figure area:", my_func(*params))
else:
    print("Incorrect choice!")
