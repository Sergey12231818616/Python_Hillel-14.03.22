# 1











#######################################################################
#6
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

    continue_1 = input("Если хотите прдолжить, нажмите 'y', а если нет нажмите любую кнопку")
