import os
import shutil
import datetime

changing_dir = ''


def get_list():
    result = os.listdir()
    result = [f for f in result if os.path.isdir(f)]
    print(result)


def create_file(name, text=False):
    global changing_dir
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_foler(name):
    global changing_dir
    try:
        os.mkdir(name)
    except FileExistsError:
        print('A folder with that name already exists!')


def delete_file(name):
    global changing_dir
    os.rmdir(name) if os.path.isdir(name) else os.remove(name)
    return


def copy_file(name, new_name):
    global changing_dir
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('A folder with that name already exists!')
    else:
        shutil.copy(name, new_name)


def log_file(message=False):
    global changing_dir
    date_time = datetime.datetime.now()
    session_info = f'{date_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(session_info + '\n')


def change_dir():
    global changing_dir
    print('Current directory: \n {}'.format(os.getcwd()))
    changing_dir = input('Enter new directory: ')
    os.chdir(changing_dir)
    print('Changed directory to: \n {}'.format(changing_dir))


def i_need_help():
    print("-" * 100)
    print('The following functions are accessible in this file manager: ')
    print()
    print(
        '"list_folders"                - gets a list of folders in which can be found in this file' + "'" + 's directory')
    print('"create_file" filename        - creates a file. Specify its extension and give that file a name!')
    print(
        '"create_folder" foldername    - creates a folder. Give that file a name (every one should have a name right?)')
    print('"delete" foldername//filename - deletes a file or a folder (only if you do not like that folder/file)')
    print(
        '"copy" finename newname       - copies a file or a folder. Do that from time to time so folder would not feel lonely.')
    print('"change_path"               - changes some paths. Unfortunately it does not work :( ')
    print('"game"                      - a little game of fun. Enjoy.')
    print("-" * 100)



if __name__ == '__main__':
    create_file('newf.txt')
    create_foler('new folder1')
    get_list()
    delete_file('newf.txt')
    copy_file('new folder1', 'new folder3')
    log_file()
    i_need_help()
