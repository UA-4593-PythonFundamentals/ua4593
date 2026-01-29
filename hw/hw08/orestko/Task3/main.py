import module

def main():
    print("Виберіть фігуру для обчислення площі:")
    print("1 - Прямокутник")
    print("2 - Трикутник")
    print("3 - Коло")

    choice = input("Ваш вибір (1/2/3): ")

    if choice == "1":
        a = float(input("Введіть довжину прямокутника: "))
        b = float(input("Введіть ширину прямокутника: "))
        print("Площа прямокутника:", module.rectangle_area(a, b))
    elif choice == "2":
        a = float(input("Введіть основу трикутника: "))
        h = float(input("Введіть висоту трикутника: "))
        print("Площа трикутника:", module.triangle_area(a, h))
    elif choice == "3":
        r = float(input("Введіть радіус кола: "))
        print("Площа кола:", module.circle_area(r))
    else:
        print("Невірний вибір!")

if __name__ == "__main__":
    main()