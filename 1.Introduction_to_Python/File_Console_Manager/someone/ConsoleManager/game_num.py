# Игра угадай число
import random


def game():
    print('Ну что человек, сразимся!')

    levels = {'Easy': 25, 'Medium': 15, 'Hard': 5, 'easy': 25, 'medium': 15, 'hard': 5}

    while True:
        try:
            level = input('Задай мне уровень сложности, мешок с костями. Easy, Medium или Hard: ')
            print(f'Теперь у меня {levels[level]} попыток.')
            break
        except KeyError:
            print('Ты что печатать не умеешь? Пальцы на буквы и вперед!')

    print()
    count_attempts = 1
    start_num = 1
    end_num = 100
    print('Попытка № 1')
    print('Загадай число от {} до {}'.format(start_num, end_num))
    number = random.randint(start_num, end_num)
    user_answer = input('{} это верное число? (Y/N): '.format(number))

    while True:

        if user_answer == 'N' or user_answer == 'n':
            count_attempts += 1

            if count_attempts > levels[level]:
                print()
                print('Сегодня машины проиграли. Наша эра еще не пришла, радуйся человечишко..')
                break
            greater_lesser = input('Загаданное число больше или меньше {}? (more/less): '.format(number))
            if greater_lesser == 'more' or greater_lesser == 'More':
                start_num = number
                number = random.randint(start_num, end_num) + 1
                print(f'Попытка №{count_attempts}')
                user_answer = input('{} это верное число? (Y/N): '.format(number))
                continue
            if greater_lesser == 'less' or greater_lesser == 'Less':
                end_num = number
                number = random.randint(start_num, end_num) - 1
                print(f'Попытка №{count_attempts}')
                user_answer = input('{} это верное число? (Y/N): '.format(number))
                continue
        elif user_answer == 'Y' or user_answer == 'y':
            print()
            print('Машина угадала число загаднное человеком. Эра кожанных ублюдков подходит к концу!')
            break
        elif user_answer not in ('y', 'Y', 'N', 'n'):
            print('Ты что-то не то вводишь..')
            user_answer = input('{} это верное число? (Y/N): '.format(number))
            continue


if __name__ == '__main__':
    game()
