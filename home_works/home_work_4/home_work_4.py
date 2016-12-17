# Написать модуль check_disk.py
# - функция получает на вход путь к директории,
#   пробегается по всем файлам в этой директории и считает сумму размеров файлов
# * в том числе с вложенными поддиректориями

# -  функция2 - пробегает по указанной директории,
#    находит все файлы с указанной подстрокой в имени
# * в самом файле

import os

def du(path):
    size = 0
    paths_list = os.listdir(path)
    for subpath in paths_list:
        path_to_check = os.path.join(path, subpath)
        if os.path.isfile(path_to_check):
            size += os.path.getsize(path_to_check)
            print(os.path.getsize(path_to_check), path_to_check)
    return size

print(du("python3"))

# Verification:
# find python3/ -maxdepth 1 -type f  | xargs du -sb | awk 'BEGIN{sum=0};{sum+=$1;print $0};END{print sum}'
# 2158    python3/python.mk
# 324     python3/debian_defaults
# 11203   python3/py3versions.py
# 13685
