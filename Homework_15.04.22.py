# Все пункты сделать как отдельные функции и их вызовы.
#
# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).

filename = "domains.txt"
def name_domains(filename):
    with open(filename, 'r') as my_file:
        data = my_file.read()
        data_list = []
        for each in data.split('\n'):
            data_list.append(each[1::])
    return data_list

filename = "domains.txt"
k = name_domains(filename)


# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"

filename = "names.txt"
def surname(filename):
    with open(filename, 'r') as my_file:
        data = my_file.read()
        data_list = []
        for each in data.split('\t')[1::3]:
            data_list.append(each)
    return data_list

filename = "names.txt"
n = surname(filename)


# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919"}, {"date": "8th February 1828"},  ...]

filename = "authors.txt"
def surname(filename):
    with open(filename, 'r') as my_file:
        data = my_file.read()
        data_list = []
        for each in data.split('\n'):
            each_1 = each.split('-')
            if len(each_1) > 1:
                data_list.append({"data": each_1[0::2]})
    return data_list


n = surname(filename)
