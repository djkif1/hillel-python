

# 1. Написать программу, которая запрашивает у пользователя два числа и выводит
#    на экран их сумму, разность, произведение и частное.

def chapter1():
    x = float(input('Введіть перше число: '))
    y = float(input('Введіть друге число: '))

    z = x+y
    q = x-y
    w = x*y
    s = x/y

    print(f'Сумма {z}')
    print(f'Разность {q}')
    print(f'Произведение {w}')
    print(f'Деление {round(s,2)}')

chapter1()
print()

# 2. Написать программу, которая запрашивает у пользователя длину и ширину прямоугольника,
#    а затем выводит его площадь и периметр.


# 3. Написать программу, которая запрашивает у пользователя радиус окружности
#    и выводит ее площадь и длину окружности.

# 4. Написать программу, которая запрашивает у пользователя три числа и выводит
#    на экран среднее арифметическое этих чисел.

x = float(input('Введіть перше число: '))
y = float(input('Введіть друге число: '))
c = float(input('Введіть трете число: '))

f = (x+y+c)/3

print(f'Середне арифметичне цих чисел: {round(f,2)}')
print()

# 5. Написать программу, которая запрашивает у пользователя год его рождения
#    и выводит его возраст на текущий момент.

def age():
    this_ear = 2023
    birth = int(input('Введіть рік вашого народження: '))
    age = this_ear-birth
    print(f'Вам вже, або буде {age} років.')

age()
print()