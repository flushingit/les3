# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя,предусмотреть обработку ситуации деления на ноль.

def del_funct(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)

        return num1 / num2
    except ValueError:
        return "Неправильный ввод"
    except ZeroDivisionError:
        return "Деление на 0"


print(f"Результат", del_funct(input("Введите делимое "), input("Введите делитель ")))
