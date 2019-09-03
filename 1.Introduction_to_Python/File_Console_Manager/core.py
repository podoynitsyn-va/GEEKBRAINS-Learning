import os
import shutil
import datetime
import random


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as new_file:
        if text:
            new_file.write(text)
    save_info(f'file {name} is created')


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Данная папка уже существует!')
    save_info(f'folder {name} is created')


def get_list(type_list='all'):
    result = os.listdir()
    if type_list == 'folders':
        result = [x for x in result if os.path.isdir(x)]
    elif type_list == 'files':
        result = [x for x in result if not os.path.isdir(x)]
    for i in result:
        print(i)
    save_info(f'get list')


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
        save_info(f'folder {name} is deleted')
    else:
        os.remove(name)
        save_info(f'file {name} is deleted')


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Данная папка уже существует')
        save_info(f'copy folder {name} to folder {new_name}')
    else:
        shutil.copy(name, new_name)
        save_info(f'copy file {name} to file {new_name}')


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time}: {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')
    f.close()


def reset_log():
    with open('log.txt', 'w') as f:
        f.write('')
    f.close()


def print_log():
    with open('log.txt', 'r') as f:
        for line in f:
            print(line)
    f.close()


def change_directory(name):
    if os.path.isdir(name):
        os.chdir(name)
        print(os.getcwd())


if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some text')
    create_folder('new_folder')
    get_list()
    get_list(True)
    delete_file('text.dat')
    delete_file('new_folder')
    # create_file('text.dat', 'some text')
    # copy_file('text.dat', 'new_text.dat')
    reset_log()
