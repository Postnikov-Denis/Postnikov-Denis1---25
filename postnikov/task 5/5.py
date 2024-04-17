import random
def zad51():
    s = [1,5,34,74,9]
    a = int( input("Назовите число: "))
    if a in s:
        return("Вы угадали число!")
    else:
        return("Нет такого числа...")

#print(zad51())

def zad52(s):
    s.sort()
    dub = set()
    n = set()
    for x in s:
        if x in n:
            dub.add(x)
        else:
            n.add(x)
    if not dub:
        print("В списке нет повторяющихся элементов")
    else:
        print("Повторяющиеся элементы в списке: ")
        for x in dub:
            print(x)

ss = [random.randint(1,10) for x in range(1, 10)]
#print(zad52(ss))

def zad53():
    dow = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье",]
    weekd = []
    workd = []
    dvih = int(input("Сколько выходных на неделе вы хотите: "))
    if dvih > len(dow):
        print("Слишком много дней")
    for i in range(1, dvih + 1):
        weekd.append(dow[-i])
        for x not in weekd:
            workd.append(x)
    return("Ваши выходные дни: ", weekd, "Ваши рабочие дни: ", workd)

print(zad53())