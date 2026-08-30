import random
import sys
diff1 = 100 
diff2 = 150 
diff3 = 300
diff4 = 500
diff5 = 666
diff1a = 15 
diff2a = 10 
diff3a = 10
diff4a = 9
diff5a = 8
max_attempts = 0
attemptsall = 0
attemptsallgame = 16 
victory = 0
defeat = 0
games = 0
dev = 0
def stuer():
       if diff == 100 and (number > diff1 or number < 1):
           print("----------")
           print(f"Вводите числа в диапазоне 1-{diff1}")
           print("----------")
           return False
       elif diff == 150 and (number > diff2 or number < 1):
           print("----------")
           print(f"Вводите числа в диапазоне 1-{diff2}")
           print("----------")
           return False
       elif diff == 300 and (number > diff3 or number < 1):
           print("----------")
           print(f"Вводите числа в диапазоне 1-{diff3}")
           print("----------")
           return False
       elif diff == 500 and (number > diff4 or number < 1):
           print("----------")
           print(f"Вводите числа в диапазоне 1-{diff4}")
           print("----------")
           return False
       elif diff == 666 and (number > diff5 or number < 1):
           print("----------")
           print(f"Вводите числа в диапазоне 1-{diff5}")
           print("----------")
           return False
       else:
           return True
while True:
    attempts = 0
    attemptsend = 0
    diffi = 0
    print("----------")
    print("Угадай число!")
    print("----------")
    print("0 - Общая статистика")
    print("1 - Выход")
    print("----------")
    print("---Уровни сложности---")
    print(f"2 - Мирная (1-{diff1}) ({diff1a} попыток)")
    print(f"3 - Лёгкая (1-{diff2}) ({diff2a} попыток)")
    print(f"4 - Средняя (1-{diff3}) ({diff3a} попыток)") 
    print(f"5 - Сложная (1-{diff4}) ({diff4a} попыток)")
    print(f"6 - Адская (1-{diff5}) ({diff5a} попыток)")
    while True:
        try:
            diff = int(input("[МЕНЮ] Введите число: "))
            print("----------")
            if diff == 0:
                print("----------")
                print(f"Всего игр: {games}")
                print(f"Побед: {victory}")
                print(f"Поражений: {defeat}")
                if games > 0:
                    ratio = victory / games 
                    ratio1 = ratio * 100
                    print(f"Процент побед: {ratio1}%")
                else:
                    print("Процент побед: 0")
                if attemptsallgame == 16:
                    print(f"Лучшая игра: 0")
                elif attemptsallgame == 1:
                    print(f"Лучшая игра: {attemptsallgame} попытка")
                elif 2 <= attemptsallgame <= 4:
                    print(f"Лучшая игра: {attemptsallgame} попытки")
                elif attemptsallgame > 4:
                    print(f"Лучшая игра: {attemptsallgame} попыток")
                print(f"Всего попыток: {attemptsall}")
                print("----------")
                continue
            elif diff == 1:
                sys.exit()
            elif diff == 2:
                diff = diff1
                max_attempts = diff1a
                games +=1
                diffi += 1
                break
            elif diff == 3:
                diff = diff2
                max_attempts = diff2a
                games +=1
                diffi += 2
                break
            elif diff == 4:
                diff = diff3
                max_attempts = diff3a
                games +=1
                diffi += 3
                break
            elif diff == 5:
                diff = diff4
                max_attempts = diff4a
                games +=1
                diffi += 4
                break
            elif diff == 6:
                diff = diff5
                max_attempts = diff5a
                games +=1
                diffi += 5
                break
            elif diff == 1682:
                print("[ВНИМАНИЕ] Эта функция нужна исключительно для тестирования.")
                print("Она напрямую влияет на игровой процесс, старайтесь не использовать")
                print("этот режим без острой необходимости, он не рассчитан для эксплуатации пользователем.")
                print("Режим разработчика: Активировано.")
                dev = 1
            else:
                print("Неизвестное значение")
        except ValueError:
            print("----------")
            print("Вводите только цифры. Код ошибки: ValueError.")
            print("----------")
    secret = random.randint(1, diff)
    while True:
        try:
            number = int(input("Введите число: "))
            if stuer():
                attempts += 1
                attemptsall += 1
                if diffi == 1:
                    attemptsend = diff1a - attempts
                elif diffi == 2:
                    attemptsend = diff2a - attempts
                elif diffi == 3:
                    attemptsend = diff3a - attempts
                elif diffi == 4:
                    attemptsend = diff4a - attempts
                elif diffi == 5:
                    attemptsend = diff5a - attempts
            elif dev >= 1 and number == 1682:
                print(f"Cекретное число: {secret}")
                continue
            else:
                continue
            if number > secret:
                    print("----------")
                    print("Меньше!")
                    print(f"Осталось: {attemptsend} попыток")
                    print("----------")
            elif number < secret:
                    print("----------") 
                    print("Больше!")
                    print(f"Осталось: {attemptsend} попыток")
                    print("----------")
            elif number == secret:
                    print("Угадал!")    
                    print(f"Попыток: {attempts}")
                    victory += 1
                    if attempts <= attemptsallgame:
                        attemptsallgame = attempts
                        break
                    else:
                        break
            if attempts == max_attempts:
                print(f"Попытки закончились! Загаданное число: {secret}.")
                defeat += 1
                break
        except ValueError:
            print("----------")
            print("Вводите только цифры. Код ошибки: ValueError.")
            print("----------")
    while True:
        cont = 0
        try:
            print("Вы хотите сыграть ещё раз?")
            print("1 - да")
            print("2 - нет")
            cont = int(input("Введите число: "))
            if cont == 2:
                sys.exit()
            elif cont == 1:
                break
            else:
                print("----------")
                print("Вводите числа в диапазоне 1-2")
                print("----------")
                continue
        except ValueError:
            print("----------")
            print("Вводите только цифры. Код ошибки: ValueError.")
            print("----------") 
            