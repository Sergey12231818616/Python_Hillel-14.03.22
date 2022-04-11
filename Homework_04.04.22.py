# 1. Дано целое число (int). Определить сколько нулей в этом числе.

my_int = 25470005100
symbol = str(0)
my_str = str(my_int)
my_result = my_str.count(symbol)
print(my_result)




# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
my_int = 100200
len_1 = len(str(my_int))

my_int_reverse = int(str(my_int)[::-1])
len_2 = len(str(my_int_reverse))

result = len_1 - len_2
print(result)





#
# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = [1, 2, 3, 4, 5, ]
my_srez_1 = my_list_1[0::2]

my_list_2 = [10, 20, 30, 40, 50, ]
my_srez_2 = my_list_2[1::2]

my_result = []
print(id(my_result))
my_result.extend(my_srez_1)
my_result.extend(my_srez_2)

print(my_result, id(my_result))





# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list = [1, 22, 33, ]
symbol = my_list[0]
new_list = my_list[1::]
new_list.append(symbol)
print(new_list)





# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list = [1, 2, 3, 4]
symbol = my_list.pop(0)
my_list.append(symbol)

print(my_list)





# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)


my_str = "6 больше чем 2 но меньше чем 8"
numbers = [int(numbers) for numbers in str.split(my_str) if numbers.isdigit()]
result = sum(numbers)
print(result)





# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "level up or down"
l_limit = "l"
r_limit = "o"
result_1 = my_str.find(l_limit) + 1
result_2 = my_str.rfind(r_limit)
sub_str = my_str[result_1:result_2]
print(sub_str)




# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

text = '43644213'
para = 2
symbol = '_'
if len(text) % 2 == 0:
    result = [text[i:i + para] for i in range(0, len(text), para)]

else:
    text += symbol
    result = [text[i:i + para] for i in range(0, len(text), para)]
print(result)





# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

my_list = [2, 4, 1, 5, 3, 9, 0, 7]
result = 0
for num in range(1, len(my_list) - 1):
    if int(my_list[num - 1]) < int(my_list[num]) and int(my_list[num]) > int(my_list[num + 1]):
        result += 1
print(result)





# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.


my_list = [1, 2, 3, "11", "22", 33]

new_list = []
for symbol in my_list:
    if type(symbol) == str:
        new_list.append(symbol)
print(new_list)


# 11. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.

my_str = 'aaaaaaavvvvvvvvvnnnnnnkm1'
my_list = []

for symbol in set(my_str):
    if my_str.count(symbol) == 1:
        my_list.append(symbol)
print(my_list)



# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.


my_str_1 = "samsa s  ujhduhfi"
my_str_2 = "samsa"
my_list = []
result = set(my_str_1) & set(my_str_2)

for symbol in result :
    my_list.append(symbol)
print(my_list)




# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу

my_str_1 = "aaaasdf1"
my_str_2 = "asdfff2"
my_list = []
result = set(my_str_1) & set(my_str_2)

for symbol in result :
    if my_str_2.count(symbol) == 1 and my_str_1.count(symbol) == 1:
        my_list.append(symbol)
print(my_list)


