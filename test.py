import random

a = random.randint(6, 14)
b = random.randint(18, 24)
print(f"ваше число: {a}")
c = input("еще?(y/n): ")
if c == 'n':
    no = print(f"ваше число {a}")
elif c == 'y':
    yes = random.randint(6, 14)
    a1 = yes + a
    print(f"ваше число: {a1}")
    if a1 > 21 > b:
        print(f"вы проиграли, я выиграл мое число было {b}")
    elif a1 < 21 > b:
        if a1 > b:
            print(f'you {b}')
        elif a1 < b:
            print(f'вы проиграли, я выиграл мое число было {b}')
    elif a1 == 21 > b:
        print(f"ты выиграл,я проиграл! мое число было: {b}")
    elif a1 > 21 < b:
        print(f" мы оба проебали!мое было: {b}")
    elif a1 > 21 == b:
        print(f'вы проиграли, я выиграл мое число было {b}')
    elif a1 < 21 < b:
        print(f'ты выиграл,я проиграл! мое число было: {b}')
    elif a1 < 21 == b:
        print(f'вы проиграли, я выиграл мое число было {b}')
    elif a1 == 21 < b:
        print(f'ты выиграл,я проиграл! мое число было: {b}')
    elif a1 == 21 == b:
        print('НИЧЬЯ')