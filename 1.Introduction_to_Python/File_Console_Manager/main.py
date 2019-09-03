import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, print_log, reset_log, change_directory
from Guess_the_Number import game

command = sys.argv[1]

if command == 'list':
    try:
        get_list(sys.argv[2])
    except IndexError:
        get_list()

elif command == 'create_file':
    try:
        name = sys.argv[2]
        try:
            text = sys.argv[3]
            create_file(name, text)
        except IndexError:
            create_file(name)
    except IndexError:
        print('Необходимо ввести имя файла!')

elif command == 'create_folder':
    try:
        name = sys.argv[2]
        create_folder(name)
    except IndexError:
        print('Необходимо ввести имя папки!')

elif command == 'delete_file':
    try:
        name = sys.argv[2]
        delete_file(name)
    except IndexError:
        print('Необходимо ввести имя файла или папки!')
    except FileNotFoundError:
        print('Объект с таким именем отсутствует')

elif command == 'copy_file':
    try:
        file_from = sys.argv[2]
        file_to = sys.argv[3]
        copy_file(file_from, file_to)
    except IndexError:
        print('Необходимо ввести имя копируемого файла, затем имя файла, в который копируем!')
    except NameError:
        print('Копируемый файл с таким именем не найден!')
    except FileNotFoundError:
        print('Копируемый файл с таким именем не найден!')

elif command == 'print_log':
    try:
        print_log()
    except FileNotFoundError:
        print('Файл журнала не найден')

elif command == 'reset_log':
    try:
        reset_log()
    except FileNotFoundError:
        print('Файл журнала не найден')

elif command == 'change_dir':
    try:
        directory = sys.argv[2]
        change_directory(directory)
    except IndexError:
        print('Введите корректный путь!')

elif command == 'game':
    game()

elif command == 'help':
    print('list - получение списка файлов и папок в директории ')
    print('     (list all - все содержимое, list files - только файлы, list folders - только папки)')
    print('create_file name - создание файла name')
    print('create_folder name - создание папки name')
    print('delete_file name - удаление файла или папки name')
    print('copy_file name1 name2 - копирование файла name1 в файл name2')
    print('print_log - отображение содержимого файла журнала')
    print('reset_log - очистка файла журнала')
    print('change_dir - изменение текущей рабочей директории')
    print('game - сыграть с компьютером в игру "Угадай число"')
else:
    print('Введите корректную команду (список команд - команда help)')



