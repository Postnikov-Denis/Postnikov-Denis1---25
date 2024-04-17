def zad1():
    a = input("Введите пароль: ")
    a1 = input("Повторно введите пароль: ")
    if a == a1:
        print("Пароль принят")
    else:
        print("Пароль не принят")
    return


def zad2():
    a = int(input("Введите номер места: "))
    if a % 2 == 0 and a<=36:
        print("верхнее в купе")
    elif a % 2 != 0 and a<= 36:
        print("нижнее в купе")
    elif a % 2 == 0 and a >= 37:
        print("боковое верхнее")
    elif a % 2 != 0 and a >= 37:
        print("боковое нижнее")
    return

def zad3():
    a = int(input("Введите год: "))
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print("Год високосный")
    else:
        print("Год не является високосным")
    return

#print(zad3())


def zad4():
    color1 = input("Введите название первого основного цвета: ")
    color2 = input("Введите название второго основного цвета: ")
    stock = ["красный", "синий", "желтый"]
    if color1 not in stock or color2 not in stock:
        print("Ошибка: введенные цвета не являются основными.")
    else:
        if color1 == "красный" and color2 == "синий":
            secondary_color = "фиолетовый"
        elif color1 == "красный" and color2 == "желтый":
            secondary_color = "оранжевый"
        elif color1 == "синий" and color2 == "желтый":
            secondary_color = "зеленый"
        else:
            print("Ошибка: введенные цвета не могут быть смешаны.")

    print("Вторичный цвет:", secondary_color)
    return

#print(zad4())