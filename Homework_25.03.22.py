#  1) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому
#  правилу: если value меньше 100, то new_value равно половине значения value,
#  в противном случае - противоположне value число

value = 120
new_value = value/2 if value < 100 else -value
print(new_value)

# 2) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно 1, в противном случае - 0

value = 200
new_value = 1 if value < 100 else 0
print(new_value)

# 3) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно True, в противном случае - False

value = 200
new_value = True if value < 100 else False
print(new_value)

# 4) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же.
# Пример: было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.
#
my_str = "qwh"
if len(my_str) < 5:
    my_str += my_str
else :
    my_str
print(my_str)

# 5) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же.
# Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.
#
my_str = "qwj"
if len(my_str) < 5:
    my_str = my_str + my_str[::-1]
else:
    my_str
print(my_str)

# 6) Доработать задание с калькулятором, чтобы в конце вычисления у пользователя спрашивало, нужен ли калькулятор еще.
# И если да, то запустить вычисление заново

continue_1 = 'y'
while continue_1 == 'y':
    input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n")

    try:
        value_1 = float(input("Введи первое число: "))
        value_2 = float(input("Введи второе число: "))

        if input_case == '1':
            sign = '+'
            result = value_1 + value_2
        elif input_case == '2':
            sign = '-'
            result = value_1 - value_2
        elif input_case == '3':
            sign = '*'
            result = value_1 * value_2
        elif input_case == '4':
            sign = '/'
            result = value_1 / value_2
        else:
            print("!!!Такой операции нет!!!")
        print(f'{value_1}  {sign}  {value_2} = {result}')

    except ValueError:
        print("!!!Введи числовое значение цифрами!!!")
    except ZeroDivisionError:
        print("!!!На ноль делить нельзя!!!")

    continue_1 = input("Если хотите прдолжить, нажмите 'y', а если нет нажмите любую кнопку: ")
