"""
Задание 2.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

a = int(input("Введите число: "))
max1 = 0

while a > 0:
    temp = a % 10
    if temp > max1:
        max1 = temp
    a //= 10

print(f"Самая большая цифра в числе: {max1}")
