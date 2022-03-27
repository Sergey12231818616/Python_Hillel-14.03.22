input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n")

value_1 = float(input("Введи первое число:"))
value_2 = float(input("Введи второе число:"))
if input_case == '1':
    print(value_1 + value_2)
elif input_case == '2':
    print(value_1 - value_2)
elif input_case == '3':
    print(value_1 * value_2)
elif input_case == '4':
    print(value_1 / value_2)
else:
    print("Такой операции нет!!!")
