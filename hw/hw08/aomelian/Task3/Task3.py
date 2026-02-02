import module

def area_calc():
    while(True):
        print("Choose a shape to calculate area of: ")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("4. Exit")
        val = int(input("\nYour choice: "))
        match val:
            case 1: 
                print("Value of A: ", end="")
                a = float(input())
                print("Value of B: ", end="")
                b = float(input())
                print("The area of rectangle is: ", end="")
                print(module.rectangle_area(a,b))
            case 2: 
                print("Value of Height: ", end="")
                h = float(input())
                print("Value of A: ", end="")
                a = float(input())
                print("The area of triangle is: ", end="")
                print(module.triangle_area(h,a))
            case 3:
                print("Value of Radius: ", end="")
                r = float(input())
                print("The area of circle is: ", end="")
                print(module.circle_area(r))
            case 4: 
                break
            case _: 
                print("Invalid choice! Please choose 1-4.")
        

if __name__ == "__main__":
    area_calc()



