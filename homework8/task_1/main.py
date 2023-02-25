"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import csv


def get_data(files):
    prod_list = []
    name_list = []
    code_list = []
    type_list = []
    for file in files:
        with open(file) as f:
            data = f.readlines()
            for line in data:
                if 'Изготовитель системы' in line:
                    a = data[data.index(line)]
                    prod_list.append(a.split(':')[1].strip())
                if 'Название ОС' in line:
                    a = data[data.index(line)]
                    name_list.append(a.split(':')[1].strip())
                if 'Код продукта' in line:
                    a = data[data.index(line)]
                    code_list.append(a.split(':')[1].strip())
                if 'Тип системы' in line:
                    a = data[data.index(line)]
                    type_list.append(a.split(':')[1].strip())
    return [prod_list, name_list, code_list, type_list]


def write_to_csv(files):
    main_data = []
    headers_list = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers_list)
    result = get_data(files)
    for i in range(len(result[0])):
        temp = []
        temp.append(i + 1)
        for j in result:
            temp.append(j[i])
        main_data.append(temp)
    with open('data_report_new.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(main_data)


files_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']

write_to_csv(files_list)
