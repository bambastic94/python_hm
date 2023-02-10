"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

lst = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь',
       'октябрь', 'ноябрь', 'декабрь']

dct = {'1': 'январь', '2': 'февраль', '3': 'март', '4': 'апрель', '5': 'май', '6': 'июнь','7':
       'июль', '8': 'август', '9': 'сентябрь', '10': 'октябрь', '11': 'ноябрь', '12': 'декабрь'}

num = input("Введите номер месяца: ")

print(f'Результат через список: {lst[int(num) - 1]}')
print(f'Результат через словарь: {dct[num]}')
