def zad41():
    n = int(input("Введите число: "))
    if n % 3 == 0:
        return("число делится на 3")
    else:
        return("число НЕ делится на 3")

#print(zad41())

def zad42():
    try:
        a = float(input("Введите число: "))
        res = 100 / a
        return res
    except ZeroDivisionError:
        return "Ошибка: деления на ноль!"
    except ValueError:
        return "ошибка: пожалуйста, введите число."

#print(zad42())

def zad43():
    date = input("Введите дату")
    day, month, year = map(int, date.split("."))
    if day * month == int(str(year)[-2:]):
        return True
    else:
        return False

#print(zad43())

def zad44():
    n = input("Введите номер билета: ")
    hl = len(n) // 2
    fh = sum(map(int, n[:hl]))
    sh = sum(map(int, n[hl:]))
    if fh == sh:
        return True
    else:
        return False

#print(zad44())