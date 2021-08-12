# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def sum_func(a1, a2, a3):
    res_sum = [a1, a2, a3]
    res_sum = sorted(res_sum, reverse=True)
    return res_sum[0] + res_sum[1]


print(sum_func(int(input("Введите первое число ")), int(input("Введите второе число ")),
               int(input("Введите третье число "))))
