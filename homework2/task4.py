"""
Задание 4. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""

a = input("Введите целые числа через пробел: ")
a_lst = int(a.replace(' ', ''))
b_lst = str(a_lst)

count = 0
while a_lst > 0:
    a_lst //= 10
    count += 1

lst = list(b_lst)

for i in range(0,count-1,2):
    temp = lst[i]
    lst[i] = lst[i+1]
    lst[i + 1] = temp

print(lst)

#Работает только для чисел меньше 10
