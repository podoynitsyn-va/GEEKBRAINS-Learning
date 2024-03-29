# Тема 3. Практикум "Угадай число"

# ======================================================================================================================
# В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги.
# Компьютер начинает его отгадывать предлагая игроку варианты чисел. Если компьютер угадал число,
# игрок выбирает “победа”. Если компьютер назвал число меньше загаданного, игрок должен выбрать
# “загаданное число больше”. Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”.
# Игра продолжается до тех пор пока компьютер не отгадает число.
# Примечание: Знаки “=”, “>” и “<” пользователь вводит с клавиатуры для общения с компьютером.
#-----------------------------------------------------------------------------------------------------------------------
# Компьютер предлагает число посередине интервала, постепенно сужая границы  в зависимости от ответов пользователя

start = 1
stop = 100
answer = None
win = False
while win == False:
    print(f'Сейчас я попытаюсь угадать загаданное тобой число от {start} до {stop}!')
    number = (start + stop) // 2
    print(f'Я думаю, что это число {number}')
    answer = input()
    if answer == '<':
        stop = number - 1
    elif answer == '>':
        start = number + 1
    elif answer == '=':
        win = True
    else:
        print('Введи "<" если загаданное число меньше, ">" если больше и "=" если я угадал!')
        print('Итак:')
    if start == stop:
        print(f'Это число {start}')
        win = True
    elif start > stop:
        print('Ловите жулика!!!')
        print('Ты жульничаешь! Я выиграл!')
        break
else:
    print('Я так и знал!')
