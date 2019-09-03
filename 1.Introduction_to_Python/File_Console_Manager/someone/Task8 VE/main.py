import sys
from core import get_list, create_file, create_folder, delete_file, copy_file, save_info, dir_change, game

save_info("Старт")

command = sys.argv[1]

if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print("Отсутствует название файла")
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print("Отсутствует название папки")
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print("Отсутствует название удаляемого объекта")
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
    except IndexError:
        print("Отсутствует название копируемого объекта")
    else:
        try:
            new_name = sys.argv[3]
        except IndexError:
            print("Отсутствует название нового объекта")
        else:
            copy_file(name, new_name)
elif command == 'change_directory': # Решение второго задания
    try:
        directory = sys.argv[2]
    except IndexError:
        print("Отсутствует адрес новой рабочей директории")
    else:
        dir_change(directory)
elif command == 'game': # Решение третьего задания
    game()
elif command == 'help':
    print('list - список файлов и папок')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удаление файла или папки')
    print('copy - копирование файла или папки')
    print('change_directory - изменение рабочей директории')
    print('game - запуск игры "Угадай число"')

save_info("Конец")

