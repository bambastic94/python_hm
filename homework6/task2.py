"""
Определить индексы элементов массива (списка), значения которых принадлежат заданному
диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
"""

lst = [1, 23, 1, 5, 4, 7, 5, 4, 3, 7, 56, 87, 98, 6, 4, 34, 67, 3, 212, 34, 4, 5, 65, 76, 78, 31, 84, 26, 72, 18]
min_num = int(input("Задайте нижний диапазон: "))
max_num = int(input("Задайте верхний диапазон: "))
lst_index = []
for i in range(len(lst)):
    if min_num <= lst[i] <= max_num:
        lst_index.append(i)

print(lst_index)