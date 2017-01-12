# 1. Простейшие арифметические операции
# 
# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".
# 
# 2. Високосный год
# 
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
# 
# 3. Квадрат
# 
# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
# 
# 4. Времена года
# 
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
# 
# 5. Банковский вклад
# 
# Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
# 
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

def arithmetic(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2
    else: return "Unknow operation"

print("\nArithmetic")
print(arithmetic(4.2, 2, "/"))

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0 ) \
        or year % 400 == 0:
        return True
    else:
        return False

print("\nis_year_leap")
print(is_year_leap(1600))

def square(size):
    perimeter = size * 4
    content = size ** 2
    diagonal = ((size ** 2) * 2) ** (1/2)
    return (perimeter, content, diagonal)

print(square(5))

def season(month):
    seasons = [
        'Winter',
        'Spring',
        'Summer',
        'Autumn',
           ]
    return seasons[(month) // 3 % 4]

print("\nSeasons")
for i in range(1,13):
    print(i, season(i))

def bank(a, years):
    if years >= 1:
        years -= 1
        return bank(a + a * 0.1, years)
    else:
        return a

print("\nBank")
for i in range(5):
    print(i,bank(10, i))
