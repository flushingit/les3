# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, birth_year, city, email, phone):
    return name, surname, birth_year, city, email, phone


print(user_data(surname=input("Введите фамилию "), name=input("Ведите имя "), birth_year=input("Ведите год рождения "),
                city=input("Ведите город проживания "), email=input("Ведите эл. почту "),
                phone=input("Ведите телефон ")))
