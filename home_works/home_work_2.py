# 1. Написать функцию без аргументов, которая будет принимать на вход через imput имя, фамилию, фозраст

# 2. Запускаем такую программу, в цикле работает эта функция.

# 3. При закрытии программы сохраняем список пользователей в файл. Программу завершаем по какому-нибудь условию.

# 4.  При очередном запуске программы читаем список пользователей из файла, далее снова п.2

# 5*. Логируйте каждый запуск программы отдельной функцией log.
# Время запуска пишем в log.txt

# 6**. Удаление конкретного пользователя.

import sys

# 1

def get_student():
    name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    age = input("Введите возраст: ")
    print(name, last_name, age)

menu = """
Select option:
q - quid
a - add student
"""
while True:
    option = input(menu)

    print(option)
    if option.lower() == "q":
        print("Quiting")
        sys.exit(0)
    elif option.lower() == "a":
        get_student()
    else:
        print("\nWrong option selected. Tru again.")
