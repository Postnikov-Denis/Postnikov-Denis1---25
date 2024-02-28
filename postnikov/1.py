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
print(zad2())