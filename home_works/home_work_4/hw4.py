# Написать модуль check_disk.py
# - функция получает на вход путь к директории,
#   пробегается по всем файлам в этой директории и считает сумму размеров файлов
# * в том числе с вложенными поддиректориями

# -  функция2 - пробегает по указанной директории,
#    находит все файлы с указанной подстрокой в имени
# * в самом файле

from check_disk import du, grep
# from check_disk import grep

print("Test of dir functino:")
# to test dir python3 was copied from /usr/share/
dir = 'python3'
print( "Dir {dir} size is - {size}".format(dir=dir, size=du(dir, recursive=False)))
print()
print("Dir {dir} size is - {size}".format(dir=dir, size=du(dir)))

print("\nTest of grep functino:")
dir = 'python3'

str = 'Pyt'
print('\nstr =', str)
print(grep(dir, str, ignorecase=True))

str = 'yth'
print('\nstr =', str)
print(grep(dir, str, ignorecase=True, recursive=True))
