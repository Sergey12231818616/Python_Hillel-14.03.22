# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.
#
my_list = [1, 101, 256, 56, 548, 5, ]
for symbol in my_list:
    if symbol > 100:
        print(symbol)


# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.
#
my_list = [1, 101, 256, 56, 548, 5, ]
my_results = []
for symbol in my_list:
    if symbol > 100:
        my_results.append(symbol)
print(my_results)


# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

my_list = [2, 3, 1, ]
if len(my_list) < 2:
    my_list.append(0)
else:
    index_value = my_list[-1] + my_list[-2]
    my_list.append(index_value)
print(my_list)