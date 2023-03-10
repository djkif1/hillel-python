# ------------------------------Задача 1-------------------------------------

print()  # пропуск строки для красоты

# Написати програму, яка конвертує градуси у радіани
# (або навпаки, за бажанням, але вкажіть що саме обрали!).
# 180 градусів - це Pi радіан.

# Взідні дані:
# градуси (або радіани).

# На виході:
# конвертована величина (градуси або радіани)
# округлена до 5 цифр після коми

# --------------------------Градусы-----------------------------

degrees = float(input("Введите градусы: "))

radians = degrees * 3.14159 / 180
rad = round(radians, 5)  # сокращаем количество цифр после запятой

print(f"{degrees} градусов = {rad} радиан")

# ------------------------------Задача 2---------------------------------------

print()  # пропуск строки для красоты

# Написати програму, що рахує абонплату за комунальним лічильника
# (наприклад, електроенергії або газу).

# Вхідні дані:
# попередні показання
# теперішні показання
# тариф.

# На виході:
# скільки потрібно сплатити, округлено до двох цифр після коми

# --------------------------Решение-----------------------------

previous = float(input("Введите предварительные показания : "))
current = float(input("Введите текущие показания : "))
tariff = float(input("Введите тариф : "))

p = current - previous  # Отнимаем предварительные от текущих показателей
y = tariff * p  # умножаем на тариф
x = round(y, 2)  # сокращаем количество цифр после запятой
print(f'Сумма к оплате {x}')

# ------------------------------Задача 3---------------------------------------

print()  # пропуск строки для красоты

# Написати програму, що рахує податок від надхождення на рахунок підприємця.

# Вхідні дані:
# розмір надходження
# відсоток податка

# На виході:
# скільки потрібно сплатити податку
# скільки залишиться чистого прибутку
# (обидва значення округлені до двох цифр після коми)


profit = float(input("Введите сумму прибыли : "))
taxR = float(input("Введите налоговую ставку : "))

tax = profit * (taxR / 100)  # делим прибыль на 100 и умножаем на налог
income = profit - tax  # Отнимаем налог от прибыли что б узнать чистую

income1 = round(income, 2)  # сокращаем количество цифр после запятой
tax1 = round(tax, 2)  # сокращаем количество цифр после запятой

print(f'Сумма к оплате {tax1}')
print(f'Чистая прибыль  {income1}')

# ------------------------------Задача 3---------------------------------------

# Написати програму що рахує витрати на паливо.

# Вхідні дані:
# витрачання палива автомобілем за 100км
# сьогоднішня ціна 1 л палива
# скільки кілометрів треба здолати

# На виході:
# скільки грошей на це піде, округлено до двох цифр після коми

consumption = float(input("Введите расход в литрах на 100км : "))
fuel_price = float(input("Введите цену за литр топлива : "))
kilometers = float(input("Введите количество километров : "))

cons = fuel_price * (consumption / 100)  # делим расход на 100 и умножаем на цену
# (узнаем цену за км)
km = cons * kilometers  # умножаем цену за км на количество нужных км
km1 = round(km, 2)  # сокращаем количество цифр после запятой
print(f'Сумма к оплате {km1}')
