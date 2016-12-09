# 1. Написать функцию без аргументов, которая будет принимать на вход через imput имя, фамилию, фозраст

# 2. Запускаем такую программу, в цикле работает эта функция.

# 3. При закрытии программы сохраняем список пользователей в файл. Программу завершаем по какому-нибудь условию.

# 4.  При очередном запуске программы читаем список пользователей из файла, далее снова п.2

# 5*. Логируйте каждый запуск программы отдельной функцией log.
# Время запуска пишем в log.txt

# 6**. Удаление конкретного пользователя.

import sys, os, datetime

# 1

def log():
    curtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logfile = open('log.txt', 'a')
    logfile.write(curtime + '\n')

def get_student():
    global students
    name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    age = input("Введите возраст: ")
    students.append([name, last_name, int(age)])

log()

menu = """
Select option:
q - quid
a - add student
"""

students = []
filename = 'students.txt'

# 4.

if os.path.isfile(filename):
    for line in open(filename, 'r'):
        students.append(line.strip().split())


# 2

while True:
    option = input(menu)

    if option.lower() == "q":
        print("Quiting")
        wfile = open(filename, 'w')
        for (name, last_name, age) in students:
            # 3
            wfile.write("{last_name} {name} {age}\n".format(name = name, last_name = last_name, age = age))
        sys.exit(0)
    elif option.lower() == "a":
        get_student()
    else:
        print("\nWrong option selected. Tru again.")
