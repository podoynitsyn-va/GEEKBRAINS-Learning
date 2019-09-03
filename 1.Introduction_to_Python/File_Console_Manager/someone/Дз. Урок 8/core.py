import os
import shutil
import datetime
import random
import sys


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8')as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка с таким именем уже существует')


def directory(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        try:
            os.remove(name)
        except FileNotFoundError:
            print('Файла с таким именем не существует')


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Папка с таким именем уже существует')
        except FileNotFoundError:
            print('Файла с таким именем не существует')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def change_dir(new_dir):
    try:
        new_path = os.path.join(os.getcwd(), f'{new_dir}')
        os.chdir(new_path)
    except FileNotFoundError:
        print('Смена директории не удалась. Папка не найдена')
    finally:
        print(f'Текущая директория: {os.getcwd()}')


def game():
    count_1 = 1
    count_2 = 100
    global is_winner
    is_winner = False
    print(
        'Правила игры: Вы загадываете число от 1 до 100. Компьютер старается его отгадать. '
        'Для подсказок компьютеру используйте символы <, > и =')
    try:
        while not is_winner:
            comp_number = random.randint(count_1, count_2)
            print(f'Число компьютера: {comp_number}')
            user_simbol = input(
                'Введите подсказку для компьютера: ')
            if user_simbol == '=':
                is_winner = True
                print('Конец игры. Компьютер угадал Ваше число')
                break
            elif user_simbol == '<':
                count_2 = comp_number - 1
            elif user_simbol == '>':
                count_1 = comp_number + 1
            else:
                print('Недопустимый символ. Введите <, > или =')
    except ValueError:
        print('Игра окончена. Вы указали неверный диапазон чисел для компьютера.')


if __name__ == '__main__':
    change_dir('1')
    print(sys.path)