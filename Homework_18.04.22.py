# Все пункты являются частью одного задания, поэтому можно использовать функции несколько раз и не дублировать код.
# Если хотите, можете использовать значения по умолчанию и аннотацию типов.
# 
# 1. Написать функцию, которая получает один параметр - имя директории и возвращает словарь вида
# {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
# Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))
#
# 2. Написать функцию, которая получает два параметра - словарь, описанный в пункте 1
# и булевое значение (True/False) - можно сделать параметром по умолчанию.
# Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
# Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.
#
# 3. Написать функцию, которая получает два параметра - словарь, описанный в пункте 1 и строку, которая может быть
# или именем файла, или именем папки. (В имени файла должна быть точка).
# В зависимости от того, что функция получила (имя файла или имя папки) - записать его в соответствующий список
# и вернуть обновленный словарь.
#
# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать функцию, которая получает два параметра - словарь, описанный в пункте 1 и имя директории.
# Функция проверяет соответствие полученного словаря и реальной файловой системы в полученной папке и,
# если надо, создает нужные папки и пустые файлы, в соответствии со структурой словаря.

import os


def create_folder_describe(folder: str) -> dict:
    folder_objects = os.listdir(folder)
    filenames = []
    subfolders = []
    for obj in folder_objects:
        obj_path = os.path.join(folder, obj)
        if os.path.isdir(obj_path):
            subfolders.append(obj)
        elif os.path.isfile(obj_path):
            filenames.append(obj)
    return {'filenames': filenames, 'dirnames': subfolders}


def sort_folder_objects(folder_objects: dict, without_reverse=True):
    for key in folder_objects:
        folder_objects[key].sort(reverse=not without_reverse)
    return folder_objects


def update_folder_objects(folder_objects: dict, obj_name: str):
    key = "filenames" if "." in obj_name else "dirnames"
    folder_objects[key].append(obj_name)
    return folder_objects



fo = create_folder_describe("alphabet")
print(fo)

sort_fo = sort_folder_objects(fo, False)
print(sort_fo)

new_fo = update_folder_objects(fo, "qwe.txt")
new_fo = update_folder_objects(new_fo, "AAA")

