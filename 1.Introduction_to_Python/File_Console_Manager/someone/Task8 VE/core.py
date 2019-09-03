import os, shutil, datetime, random

def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')

def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)

def delete_file(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except FileNotFoundError:
        print("Данный объект отсутствует в рабочей папке") #Добавил еще один тип ошибки

def copy_file(name, new_name):
    try:
        if os.path.isdir(name):
            try:
                shutil.copytree(name, new_name)
            except FileExistsError:
                print('Такая папка уже есть')
        else:
            shutil.copy(name, new_name)
    except FileNotFoundError:
        print("Копируемый объект отсутствует в рабочей папке") #Добавил еще один тип ошибки

def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt','a', encoding='utf-8') as f:
        f.write(result + '\n')

# Решение второго задания
def dir_change(path):
    try:
        os.chdir("{}".format(path))
    except FileNotFoundError:
        print("Данной директории не существует")
    else:
        print("Текущая рабочая директория: {}".format(os.getcwd()))

# Решение третьего задания
def game():
    number = random.randint(1, 100)
    user_number = "0"
    count = 0
    max_count = "number"
    while max_count.isdigit() == False or int(max_count) <= 0:
        max_count = input("Введите максимальное количество попыток: ")
    while number != int(user_number):
        count += 1
        if count > int(max_count):
            print('Вы проиграли')
            break
        print(f'Попытка № {count}')
        user_number = input('Введите число: ')
        while user_number.isdigit() == False:
            user_number = input('Введите число: ')
        if number < int(user_number):
            print('Ваше число больше загаданного')
        elif number > int(user_number):
            print('Ваше число меньше загаданного')
        else:
            print('Победа')

