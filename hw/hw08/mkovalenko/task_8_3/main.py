import calculation

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

dict_functions = {"R": calculation.rectangle_area, "T": calculation.triangle_area, "C": calculation.circle_area}

figure_type = input("Choose figure: R - for rectangle; T - for triangle; C - for circle: ").upper()

my_func = dict_functions.get(figure_type)
if my_func:
    params = input_parameters(figure_type)
    print("Figure area:", my_func(*params))
else:
    print("Incorrect choice!")
 
