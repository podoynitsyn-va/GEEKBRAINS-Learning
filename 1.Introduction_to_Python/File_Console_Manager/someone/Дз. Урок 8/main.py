import sys
from core import create_file, create_folder, directory, delete_file, copy_file, save_info, change_dir, game

command = sys.argv[1]
save_info('Старт')
if command == 'list':
    if sys.argv[2] == 'folders':
        directory(True)
    else:
        directory()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название папки')
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
        delete_file(name)
    except OSError:
        print('Невозможно удалить папку с файлами')
    except IndexError:
        print('Отсутствует название файла или папки')
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('Отсутствует название файла или папки')
    else:
        copy_file(name, new_name)
elif command == 'change':
    try:
        new_dir = sys.argv[2]
        change_dir(new_dir)
    except IndexError:
        print('Отсутствует название папки')
elif command == 'game':
    game()

elif command == 'help':
    print('list - текущая директория. Чтобы отобразить только папки, введите параметр folders \n'
          'create_file - созвдание файла.\n'
          'create_folder - создание папки.\n'
          'delete - удаление папки или файла.\n'
          'copy - копирование папки или файла.\n'
          'change - смена текущей рабочей директории.\n'
          'game - запускает игру "Загадай число".\n')

save_info('Конец')
