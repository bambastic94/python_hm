"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

print("Введите целое положительное число: ")
n = int(input())

print(f"n + nn + nnn = {str(n) + str(n + n) + str(n + n + n)}")