print("Выберите нужную вам функцию, напишите первое число выбранную функцию и второе число через пробел")
print("Сложение '+'")
print("Вычитание '-'")
print("Умножение '*'")
print("Деление ':'")
print("Целочисленное деление '::'")
print("Взятие остатка ':?'")
print("Возведение в степень '<>', второе число степень")
print("Квадратный корень числа '_\/---', второе число не обязательно")
print("Переводить из любой системы счисления в десятичную '!', второе число не обязательно")
print("Анализ числа '!?%', второе число не обязательно")
print("В который входит:")
print("1) Вывод количества разрядов в числе")
print("2) Вывести сколько каких цифр в есть числе (если цифры нет, выводить её не надо)")
print("3) Четное или не четное число")
print("4) Вывод суммы цифр числа")
print("5) проверку является ли число простым, если не простое, то вывести все делители числа")
print("6) проверку ли число полным квадратом (если да, то какого числа)")
print("7) проверить, является ли число полным кубом (если да, то какого числа)")
stroka = input()
number = stroka.split()[1]


def number_is_slojenie():
    print(int(stroka.split()[0]) + int(stroka.split()[2]))


def number_is_wichitanie():
    print(int(stroka.split()[0]) - int(stroka.split()[2]))


def number_is_umnojenie():
    print(int(stroka.split()[0]) * int(stroka.split()[2]))


def number_is_delenie():
    print(int(stroka.split()[0]) / int(stroka.split()[2]))


def number_is_delenieeee():
    print(int(stroka.split()[0]) // int(stroka.split()[2]))


def number_is_ostatok():
    print(int(stroka.split()[0]) % int(stroka.split()[2]))


def number_is_stepen():
    print(int(stroka.split()[0]) ** int(stroka.split()[2]))


def number_is_koren():
    print(int(stroka.split()[0]) ** 0.5)


def number_is_int():
    print(int(int(stroka.split()[0])))


def number_is_analiz():
    print(len(stroka.split()[0]))           #первое действие
    list1 = []
    for i in range(10):
        count = 0
        for j in stroka.split()[0]:
            if i == int(j):
                count += 1
        list1.append((i, count))
    print(list1)                            #второе действие
    if int(stroka.split()[0]) % 2 == 0:
        print("Четное")
    else:
        print("Нечетное")                   #третье действие
    count1 = 0
    for b in stroka.split()[0]:
        count1 += int(b)
    print(count1)                           #четвертое действие
    list2 = []
    for g in range(1, int(stroka.split()[0]) + 1):
        if int(stroka.split()[0]) % g == 0:
            list2.append(g)
    print(list2)                            #пятое действие
    if int(stroka.split()[0]) ** 0.5 % 1 != 0:
        print("НЕТ")
    else:
        print(int(stroka.split()[0]) ** 0.5)#шестое действие
    if int(stroka.split()[0]) ** (1./3.) % 1 != 0:
        print("НЕТ")
    else:
        print(int(stroka.split()[0]) ** (1./3.))#седьмое действие


if number == "+":
    number_is_slojenie()
elif number == "-":
    number_is_wichitanie()
elif number == "*":
    number_is_umnojenie()
elif number == ":":
    number_is_delenie()
elif number == "::":
    number_is_delenieeee()
elif number == "":
    number_is_ostatok()
elif number == ":?":
    number_is_ostatok()
elif number == "<>":
    number_is_stepen()
elif number == "_\/---":
    number_is_koren()
elif number == "!":
    number_is_int()
elif number == "!?%":
    number_is_analiz()
