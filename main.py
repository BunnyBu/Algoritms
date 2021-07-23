# Algorithms
# Homework 02
# Trushin Denis
import random


def first_task():
    # 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
    # Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
    # а должна запрашивать новые данные для вычислений.
    # Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
    # Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
    # то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
    # Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

    sign = None  # UnboundLocalError: local variable 'sign' referenced before assignment
    while sign != '0':
        num1 = int(input("Введите первое число: "))
        sign = input('Введите знак операции или "0" для завершения: ')
        num2 = int(input("Введите второе число: "))
        if sign == '0':
            print("Работа завершена")
            pass
        elif sign == '+':
            print(f'{num1} + {num2} = {num1 + num2}')
        elif sign == '-':
            print(f'{num1} - {num2} = {num1 - num2}')
        elif sign == '*':
            print(f'{num1} * {num2} = {num1 * num2}')
        elif sign == '/':
            try:
                print(f'{num1} / {num2} = {num1 / num2}')
            except ZeroDivisionError:
                print("Деление на 0. Результат не определён, повторите ввод.")
        else:
            print("Непонятный знак операции, повторите ввод.\n*****************")


def disintegrator(any_int: int):
    if any_int < 0:
        any_int *= -1
    dig_array = []
    while any_int // 10 > 0:
        dig_array.append(any_int % 10)
        any_int = any_int // 10
    dig_array.append(any_int)
    return dig_array


def second_task(number: int):
    # 2. Посчитать четные и нечетные цифры введенного натурального числа.
    # Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
    digits = disintegrator(number)
    result = {'Чёт': 0, 'Нечет': 0}
    result['Чёт'] += digits.count(0) + digits.count(2) + digits.count(4) + digits.count(6) + digits.count(8)
    result['Нечет'] += digits.count(1) + digits.count(3) + digits.count(5) + digits.count(7) + digits.count(9)
    return result


def third_task(number: int):
    # Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
    # Например, если введено число 3486, то надо вывести число 6843.
    result = ''
    for i in disintegrator(number):
        result += str(i)
    return int(result)


def fourth_task(input_len):
    # 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125...
    # Количество элементов (n) вводится с клавиатуры.
    result = 0
    for i in range(0, input_len):
        result += (-1 / 2) ** i
    return result


def fifth_task():
    # 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
    # Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
    ascii_sub_table = {x: chr(x) for x in range(32, 128)}
    index = 32
    while index:
        for _ in range(0, 10):
            print(str(index).rjust(3) + ': \'' + str(ascii_sub_table[index]) + "'", end=' | ')
            index += 1
            if index > 127:
                index = 0
                break
        print()


def sixth_task():
    # 6. В программе генерируется случайное целое число от 0 до 100.
    # Пользователь должен его отгадать не более чем за 10 попыток.
    # После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
    # чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
    passnum = random.randint(0, 101)
    print("Игра угадайте число от 0 до 100. У Вас есть 10 попыток.")
    for _ in range(0, 10):
        trynum = int(input("Введите число: "))
        if passnum == trynum:
            print(f"Вы угадали! Действительно {passnum}")
        elif passnum < trynum:
            print("Вы не угадали. Загаданное число меньше введённого.")
        else:
            print("Вы не угадали. Загаданное число больше введённого.")
    print(f"Попытки закончились, было загадано {passnum}.")


def seventh_task(inputnum: int):
    # 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
    # 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
    result1 = 0
    for index in range(1, inputnum+1):
        result1 += index
    result2 = inputnum * (inputnum+1) / 2
    return result1, result2


def eighth_task():
    # 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
    # Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
    array = []
    count_digit = 0
    count_num = int(input('Введите длину последовательности: '))
    for _ in range(0, count_num):
        array.append(int(input("Введите последовательность чисел по одному: ")))
    digit = input('Введите цифру поска и подсчёта: ')
    for item in array:
        count_digit += str(disintegrator(item)).count(str(digit))
    print(f'Найдено {count_digit} вхождений.')


def ninth_task():
    # 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
    # Вывести на экран это число и сумму его цифр.
    array = []
    count_num = int(input('Введите длину последовательности: '))
    for _ in range(0, count_num):
        array.append(int(input("Введите последовательность чисел по одному: ")))
    max = []
    max.append(array[0])
    max.append(sum(disintegrator(array[0])))
    for item in array:
        if max[1] < sum(disintegrator(item)):
            max[0] = item
            max[1] = sum(disintegrator(item))
    print(f'Первое введённое наибольшее число по сумме цифр: {max[0]}, сумма равна {max[1]}')


if __name__ == '__main__':

    # first_task()
    # print(second_task(340104800534661))
    # print(third_task(2376901))
    # print(fourth_task(int(input('Введите длину последоватльности: '))))
    # fifth_task()
    # sixth_task()
    # print(seventh_task(7))
    # eighth_task()
    #ninth_task()
    pass
