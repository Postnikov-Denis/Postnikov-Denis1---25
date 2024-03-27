import random

def zad21():
    words = []
    result = ""
    N = input("Введите кол-во слов: ")
    for i in range(N + 1):
        word = input("Введите слово: ")
        words.append(word)
    for word in words:
        result += word + " "
    print(result)
    return

print(zad21())


def zad22():
    words = []
    result = ""

    while True:
        word = input("Введите слово: ")
        if word == "stop":
            break
        words.append(word)

    for word in words:
        result += word + " "

    print(result)
    return


#print(zad22())


def zad23():
    word = input("Введите слово: ")

    for letter in word:
        if letter == "ф":
            print("Ого! Это редкое слово!")
            break
    else:
        print("Эх, это не очень редкое слово...")
    return


#print(zad23())


def zad24():
    answers = 0
    errors = 0

    while errors < 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_result = num1 + num2

        user_answer = input(f"{num1} + {num2} = ")

        if user_answer.isdigit() and int(user_answer) == correct_result:
            print("Правильно!")
            answers += 1
        else:
            print("Ответ неверный")
            errors += 1

    print(f"Игра окончена. Правильных ответов: {answers}")
    return


#print(zad24())