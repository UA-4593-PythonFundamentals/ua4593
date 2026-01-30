import random
secret_num = random.randint(1, 100)

attempts = 10
win = False

print("Спробуйте вгадати число від 1 до 100. У вас є 10 спроб.")

for attempt in range(1, attempts + 1):
    while True:
        num = int(input(f"Спроба {attempt}: Введіть число: "))
        if 1 <= num <= 100:
            break
        else:
            print("Будь ласка, введіть число від 1 до 100.")

    if num == secret_num:
        print(f"Вітаю! Ви вгадали число {secret_num} з {attempt} спроби!")
        win = True
        break
    elif num < secret_num:
        print("Загадане число більше за ваше.")
    else:
        print("Загадане число менше за ваше.")

if not win:
    print(f"На жаль, ви не вгадали число. Загадане число було {secret_num}.")