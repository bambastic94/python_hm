"""
Задайте последовательность чисел. Напишите программу, которая выведет список
неповторяющихся элементов исходной последовательности.
"""

lst = [2, 4, 6, 8, 4, 1, 6, 4, 3, 7]
new_lst = []
for el in lst:
    if el not in new_lst:
        new_lst.append(el)

print(lst)
print(new_lst)