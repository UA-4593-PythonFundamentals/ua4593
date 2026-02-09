#import random
from random import randint
n = randint(1, 100)
#print(n)
attempts = 0    #порожній лічильник
while attempts <10:    #while True:
    u = int(input(f"Спроба № {attempts + 1}. Введіть ціле число від 1 до 100: "))
    attempts += 1
    if u > n:
        print("задане число менше ніж ваше")
    elif u < n:
        print('задане число більше ніж ваше')
    elif u == n:
        print('Вітаю! Ви екстрасенс вищого розряду')
        break
else:
    print(f'кількість спроб вичерпано. Відповідь: {n}')
