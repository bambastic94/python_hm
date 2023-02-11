"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""


def primfacs(n):
    i = 2
    a = []
    while i <= n:
        if n % i == 0:
            a.append(i)
        i = i + 1
    return a

print(primfacs(int(input("Введите число: "))))
