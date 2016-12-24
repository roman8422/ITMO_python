# Создаем поезд на функциях
# Создается пустой поезд с помощью функций, значения возвращаются с помощью return или print
# Декоратор уголь, декоратор дерево, декоратор камень, все должно лежать в вагоне
#
#* написать декоратор, который куда-то складирует количество запусков функции, разные функции должны считаться по отдельности

def put_content(vagon, content):
    list_vagon = vagon.split('\n')
    container = list_vagon[1]
    container = list(container)
    content = list(content)
    space_to_fill = len(container) - 3 # отнимаем пробел и | спереди и | сзади вагона

    if len(content) >= space_to_fill: # если строка не влезает в вагон - обрезаем
        content = content[:space_to_fill]
        content = container[:2] + content + container[-1:]
    else: # если строка влезает в вагон, нужны ли пробелы для выравнивания
        num_of_spaces = space_to_fill - len(content)
        num_of_spaces_at_the_beginning = num_of_spaces // 2 # сколько нужно пробелов в начале вагона
        num_of_spaces_at_the_end = num_of_spaces % 2 + num_of_spaces_at_the_beginning # сколько нужно пробелов в конце вагона

        beginning_of_the_container = [' ' for i in range(num_of_spaces_at_the_beginning)]
        end_of_the_container = [' ' for i in range(num_of_spaces_at_the_end)]

        content = container[:2] + beginning_of_the_container + content + end_of_the_container + container[-1:]

    content = "".join(content)
    list_vagon[1] = content
    vagon = "\n".join(list_vagon)

    return vagon

def add_coal(func):
    def new_func():
        return put_content(func(), "coal")
    return new_func


def add_oil(func):
    def new_func():
        return put_content(func(), "oil")
    return new_func

def add_kerosene(func):
    def new_func():
        return put_content(func(), "kerosene")
    return new_func

def add_phosphate(func):
    def new_func():
        return put_content(func(), "phosphate")
    return new_func


def teplovoz():
    return("""\
     ______
   _()_||__||
  (         |
 /-OO----OO"" """)


def vagon():
    return("""\
  ________
 |        |
 "OO----OO" """)


print(teplovoz())
print(add_coal(vagon)())
print(add_oil(vagon)())
print(add_kerosene(vagon)())
print(add_phosphate(vagon)())
