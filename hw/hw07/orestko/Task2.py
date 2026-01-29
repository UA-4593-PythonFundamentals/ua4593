def rectangle_area(l, w):
    return l * w

def triangle_area(b, h):
    return 0.5 * b * h

def circle_area(r):
    pi = 3.14159
    return pi * (r ** 2)

def main():
    print("Виберіть фігуру для розрахунку площі:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")

    choice = input("Ваш вибір (1/2/3): ")

    if choice == "1":
        l = float(input("Введіть довжину прямокутника: "))
        w = float(input("Введіть ширину прямокутника: "))
        print("Площа прямокутника:", rectangle_area(l, w))
    
    elif choice == "2":
        b = float(input("Введіть основу трикутника: "))
        h = float(input("Введіть висоту трикутника: "))
        print("Площа трикутника:", triangle_area(b, h))
    
    elif choice == "3":
        r = float(input("Введіть радіус: "))
        print("Площа кола:", circle_area(r))
    
    else:
        print("Не вірний вибір")

if __name__ == "__main__":
    main()