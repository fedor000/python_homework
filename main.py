def calc(n1, n2, znak):
    """Function evaluates the expression and prints the result"""
    if znak == '+':
        print(n1 + n2)
    elif znak == '-':
        print(n1 - n2)
    elif znak == '*':
        print(n1 * n2)
    elif znak == '/':
        if n1 == 0:
            raise ZeroDivisionError
        print(n1/n2);


try:
    num_1 = float(input('Введите первое число: '))
    num_2 = float(input('Введите второе число: '))
    operator = input('Выберите действие ( (+) or (-) or (*) or (/) : ')
    calc(num_1, num_2, operator)
except ZeroDivisionError:
    print('Деление на 0')

