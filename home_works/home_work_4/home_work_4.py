# Написать модуль check_disk.py
# - функция получает на вход путь к директории,
#   пробегается по всем файлам в этой директории и считает сумму размеров файлов
# * в том числе с вложенными поддиректориями

# -  функция2 - пробегает по указанной директории,
#    находит все файлы с указанной подстрокой в имени
# * в самом файле

import os

def du(path, recursive=True):
    size = 4096 # dir size itself
    paths_list = os.listdir(path)
    for subpath in paths_list:
        path_to_check = os.path.join(path, subpath)
        if not os.path.isdir(path_to_check):
            size += os.path.getsize((path_to_check))
        elif os.path.isdir(path_to_check):
            if recursive:
                size += du(path_to_check, recursive=True)

    return size

# to test dir python3 was copied from /usr/share/
dir = 'python3'
print("Dir {dir} size is - {size}".format(dir=dir, size=du(dir, recursive=False)))
print()
print("Dir {dir} size is - {size}".format(dir=dir, size=du(dir)))

def grep(dir, str, recursive=False, ignorecase=False):
    paths_list = os.listdir(dir)
    for subpath in paths_list:
        if ignorecase:
            name_to_check = subpath.lower()
            str = str.lower()
        else:
            name_to_check = subpath

        full_path = os.path.join(dir, subpath)
        if str in name_to_check:
            print("Filename matches template:", full_path)
        if os.path.isdir(full_path):
            if recursive:
                grep(full_path, str, recursive, ignorecase)

    return 0

dir = 'python3'

str = 'Pyt'
print('\nstr =', str)
print(grep(dir, str, ignorecase=True))

str = 'yth'
print('\nstr =', str)
print(grep(dir, str, ignorecase=True, recursive=True))
