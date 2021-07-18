# Algoritms
# Homework 01
# Trushin Denis
import random

def first_task():
    # 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

    input_int = int(input("Введите целое число: "))
    sum_item = 0
    multiply_item = 1

    for item in disintegrator(input_int):
        sum_item += item
        multiply_item *= item
    print(f'Сумма цифр равна {sum_item}, произведение {multiply_item}')


def disintegrator(any_int: int):
    if any_int < 0:
        any_int *= -1
    dig_array = []
    while any_int // 10 > 0:
        dig_array.append(any_int % 10)
        any_int = any_int // 10
    dig_array.append(any_int)
    return dig_array


def second_task(a = 5, b = 6):
    # 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый
    # сдвиг вправо и влево на два знака. Объяснить полученный результат.
    print(f'a = {bin(a)} b = {bin(b)}')
    print(f'a & b = {bin(a & b)}')
    print(f'a | b = {bin(a | b)}')
    print(f'~a = {bin(~a)}, ~b = {bin(~b)}')
    print(f'a << 2 = {bin(a << 2)}')
    # умножение на 2^n где n - количество сдвигов (порядков в двоичной системе)
    print(f'a >> 2 = {bin(a >> 2)}')
    # целочисленное деление на 2^n где n - количество сдвигов


def third_task(x1: int, y1: int, x2: int, y2: int):
    # 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида
    # y=kx+b, проходящей через эти точки.
    if x1 != x2:
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        print(" y = %.2f*x + %.2f" % (k, b))
    else:
        print(f"функция не определена")


def fourth_task(first, last):
    # 4. Написать программу, которая генерирует в указанных пользователем границах:
    # случайное целое число;
    # случайное вещественное число;
    # случайный символ.
    # Для каждого из трех случаев пользователь задает свои границы диапазона.
    # Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
    # Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
    if type(first) == type(last):
        if isinstance(first, int):
            result = random.randint(first, last)
            #Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
        elif isinstance(first, str):
            items = [chr(i) for i in range(ord(first), ord(last)+1)]
            result = random.choice(items)
        elif isinstance(first, float):
            result = random.uniform(first, last)
        else:
            result = 'Unsupported types'
    else:
        result = 'Different types'
    return result


def fifth_task(first: chr, second: chr):
    # 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят
    # и сколько между ними находится букв.
    # [A-Z] --65-90
    first = ord(first.upper())
    second = ord(second.upper())
    if first > 64 and first < 91 and second > 64 and second < 91:
    # Если буквы принадлежат английскому алфавиту
        print(f'{chr(first)} стоит на {first - 64} позиции в алфавите, {chr(second)} на {second - 64}')
        if first - second >=0:
            print(f'Расстояние между буквами {first - second}')
        else:
            print(f'Расстояние между буквами {second - first}')
    else:
        print('Буква не принадлежит английскому алфавиту')


def sixth_task(chr_num: int):
    #6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
    print(f'{chr_num} соответствует буква {chr(chr_num+64)}')


def seventh_task(a: int, b : int, c : int):
    #7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
    # составленного из этих отрезков. Если такой треугольник существует, то определить,
    # является ли он разносторонним,равнобедренным или равносторонним.
    if (a > 0 and b > 0 and c > 0) and (a + b > c) and (a + c > b) and (b + c > a):
        print(f'Треугольник со сторонами {a}, {b}, {c} может быть построен')
        if a == b and a == c:
            print('И он будет равносторонний')
        elif a == b or a == c or b == c:
            print('И он будет равнобедренный')
    else:
        print(f'Треугольник со сторонами {a}, {b}, {c} невозможно построить')


def eighth_task(year: int):
    # 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
    # год, номер которого кратен 400, — високосный;
    # остальные годы, номер которых кратен 100, — невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300);
    # остальные годы, номер которых кратен 4, — високосные.
    if (year >= 1582):
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):
            print(f'{year} год високосный')
        else:
            print(f'{year} год не високосный')
    else:
        print('Григорианский календарь введён в 1582 году.')


def ninth_task(a: int, b : int, c : int):
    # 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
    if (a > b and a < c) or (a < b and a > c):
        print(f'{a} среднее')
    elif (b > a and b < c) or (b < a and b > c):
        print(f'{b} среднее')
    elif (c > a and c < b) or (c < a and c > b):
        print(f'{c} среднее')
    else:
        print('Определить среднее не удалось')


if __name__ == '__main__':

#    first_task()
#    second_task()
#    third_task(2, 3, 5, 6)
#    print(fourth_task('A', 'G')) # requared min and max element. Example: 1, 23 or 's', 'z' or 2.67, 5.31
#    fifth_task('S', 'Z') #[A-Z,a-z]
#    sixth_task(26) # 1-26
#    seventh_task(-12,4,5)
#    eighth_task(1900)
    ninth_task(12, 12, 8)