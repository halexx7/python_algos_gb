"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def math_res(symbol, number_one, number_two):
    """
    Функция вычисляет результат операции над двумя числами.

    symbol: знак операции (+, -, *, /)
    number_one: Первое число
    number_two: Второе число
    """
    if symbol == '+':
        res = number_one + number_two
    elif symbol == '-':
        res = number_one - number_two
    elif symbol == '/':
        res = number_one / number_two
    else:
        res = number_one * number_two
    return res


def calc():
    """
    Функция описывает работу простейшего калькулятора.
    """
    symbol = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    i = 0
    if symbol == '0':
        return 'До свидания!'
    elif symbol in ('+', '-', '*', '/'):
        try:
            number_one = int(input('Введите первое число: '))
            number_two = int(input('Введите второе число: '))
            if number_two != 0:
                print(f'Ваш результат = {math_res(symbol, number_one, number_two)}')
            else:
                print('На ноль делить нельзя!')
        except ValueError:
            print('Вы ввели не число!')
        return calc()
    else:
        print('Вы ввели неизвестный символ!')
        return calc()


print(calc())

