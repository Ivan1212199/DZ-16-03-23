"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
"""

NomberOfCoins = int(input('Введите количество монеток: '))
from random import randint
FirstValue, SecondMeaning = 0, 0
for i in range(NomberOfCoins):
    temp = randint(0, 1)
    print(temp, end=' ')
    if temp > 0: FirstValue += 1
    else: SecondMeaning += 1
print()
if FirstValue > SecondMeaning:
    print(f'Нужно перевернуть {SecondMeaning} монеток')
else:
    print(f'Нужно перевернуть {FirstValue} монеток')