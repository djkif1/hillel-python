total = 0
while True:
    user_input = input("Введите число или sum: ")  #
    if user_input.lower() == "sum":  #
        break

    try:
        num = float(user_input)
        total += num  #
    except ValueError:
        print('Не корректный ввод')

print("Сумма введеных чисел:", total)

# __________________________________________________________________________________________________________________


total = []
while True:  # запускаем бесконечный цыкл
    user_input = input("Введите число или sum: ")  # Предлогаем ввести число или sum
    if user_input.lower() == "sum":  # Проверяем что введено и если (sum) выходим из цыкла
        break  #
    if user_input.isdigit():  # проверяем что юзверь ввел число
        num = float(user_input)  # присваиваем переменной значение которое ввел юзверь и тип флоат
        total.append(num)  # добавляем число в список (total)
    else:
        print('Не корректный ввод')  # придупреждаем о не корректном вводе
print("Сума введених чисел:", sum(total))  # При выходе из цыкла печатаем сумму чисел списка (total)

# ____________________________________________________________________________________________________________________

total = []
while True:
    user_input = input("Введите число или sum: ")
    if user_input.lower() == "sum":
        break
    try:
        num = float(user_input)
        total.append(num)
    except ValueError:
        print('Не корректный ввод')

print("Сумма введеных чисел:", sum(total))
