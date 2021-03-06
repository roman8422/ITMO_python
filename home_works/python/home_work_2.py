# 1. Написать функцию без аргументов, которая будет принимать на вход через imput имя, фамилию, фозраст

# 2. Запускаем такую программу, в цикле работает эта функция.

# 3. При закрытии программы сохраняем список пользователей в файл. Программу завершаем по какому-нибудь условию.

# 4.  При очередном запуске программы читаем список пользователей из файла, далее снова п.2

# 5*. Логируйте каждый запуск программы отдельной функцией log.
# Время запуска пишем в log.txt

# 6**. Удаление конкретного пользователя.

import sys, os, datetime


# 5.
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

def print_students():
    print()
    for num, (name, last_name, age) in enumerate(students):
        print("{num}. {last_name} {name}".format(name=name, last_name = last_name, num = num))

# 6.
def del_student():
    global students
    index = input("\nEnter number of student you want to delete\n.To return to main menu press 'b")
    if index.lower() == "b":
        return 0
    else:
        index = int(index)

    removed = students.pop(index)
    print("Student {} {} was removed.\n".format(removed[1], removed[0]))

# 1
def menu_function(option=None):
    if not option:
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
    elif option.lower() == "d":
        del_student()
    elif option.lower() == "p":
        print_students()
    else:
        print("\nWrong option selected. Tru again.")

log()

menu = """
Select option:
q - quid
a - add student
d - delete student
p - print list of all students
"""

students = []
filename = 'students.txt'

# 4.
if os.path.isfile(filename):
    for line in open(filename, 'r'):
        students.append(line.strip().split())

# 2
while True:
    menu_function()
