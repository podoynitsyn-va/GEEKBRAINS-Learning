import sys
from game_num import game
from core import get_list, create_foler, create_file, delete_file, copy_file, log_file, i_need_help, change_dir

log_file('Session start')

command = sys.argv[1] if len(sys.argv) > 1 else i_need_help()

if command == 'list_folders':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
        text = sys.argv[3]
        create_file(name, text)
    except IndexError:
        name = sys.argv[2]
        create_file(name)
elif command == 'create_folder':
    name = sys.argv[2]
    create_foler(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
        delete_file(name)
    except FileNotFoundError:
        print('No such file in directory! What are you, stupid?!')
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
        copy_file(name, new_name)
    except IndexError:
        print('You gave that name to a folder already! Try another one. Take your time, no rush..')
elif command == 'help':
    i_need_help()
elif command == 'change_path':
    # path_name = sys.argv[2]
    change_dir()
elif command == 'game':
    game()


log_file('Session end')
