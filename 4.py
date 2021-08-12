# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.


def func_1(x, y):
    res = x
    for i in range(abs(y) - 1):
        res = res * x
    return 1 / res


while True:
    try:
        x = float(input("Введите действительное положительное число "))
    except ValueError:
        print("Не корректный ввод ")
        continue
    else:
        if x <= 0:
            print("Нужно ввести действительное положительное число")
            continue
        else:
            break
while True:
    try:
        y = int(input("Целое отрицательное число "))
    except ValueError:
        print("Не корректный ввод ")
        continue
    else:
        if y >= 0:
            print("Нужно ввести целое отрицательное число")
            continue
        else:
            break

print(func_1(x, y), (lambda x1, y1: x1 ** y1)(x, y))
