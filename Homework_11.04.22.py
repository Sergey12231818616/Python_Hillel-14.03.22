# Для задания 1-7 за основу можете взять код из предідущих ДЗ.
#
# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.


my_list = ['abs', '123', 'efd', 'dfdf', 'ffwef']
new_list = []
def reverse_list(my_list):
    for index, item in enumerate(my_list):
        if index % 2 != 0:
            new_list.append(item[::-1])
        else:
            new_list.append(item)
    return new_list
print(reverse_list(my_list))


# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".

new_list = []
def search_first_a(my_list):
    for symbol in my_list:
        if 'a' == symbol[0]:
            new_list.append(symbol)
    return new_list
print(search_first_a(my_list))


# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.

new_list = []
def search_a(my_list):
    for symbol in my_list:
        if 'a' in symbol:
            new_list.append(symbol)
    return new_list
print(search_a(my_list))

# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.

my_list = [1, 2, 3, "11", "22", 33]

new_list = []
def return_str(my_list):
    for symbol in my_list:
        if type(symbol) == str:
            new_list.append(symbol)
    return new_list
print(return_str(my_list))

# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.

my_str = 'aaaaaaavvvvvvvvvnnnnnnkm1'
my_list = []
def unic(my_str):
    for symbol in set(my_str):
        if my_str.count(symbol) == 1:
            my_list.append(symbol)
    return my_list
print(unic(my_str))

# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_1 = "samsa s  ujhduhfi"
my_str_2 = "samsa"
my_list = []
def unic_in_str(my_str_1, my_str_2):
    result = set(my_str_1) & set(my_str_2)
    for symbol in result:
        my_list.append(symbol)
    return my_list
print(unic_in_str(my_str_1, my_str_2))

# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

my_str_1 = "aaaasdf1"
my_str_2 = "asdfff2"
my_list = []
def unic_in_str1(my_str_1, my_str_2):
    result = set(my_str_1) & set(my_str_2)
    for symbol in result :
        if my_str_2.count(symbol) == 1 and my_str_1.count(symbol) == 1:
            my_list.append(symbol)
    return my_list
print(unic_in_str1(my_str_1, my_str_2))

# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com

import random

names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
value = random.randint(100, 1000)
random_word = ''.join(chr(random.randint(ord('a'), ord('z'))) for j in range(random.randint(5, 7)))

def create_email(domains, names):
    e_mail = random.choice(names) + '.' + str(value) + '@' + str(random_word) + '.' + random.choice(domains)
    return e_mail
print(create_email(domains, names))
