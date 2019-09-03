import os


def make_dirs(quantity):
    for i in range(1, quantity+1):
        name = os.path.join(os.getcwd(), f'dir_{i}')
        if not os.path.exists(name):
            os.mkdir(name)
            print(f'Директория "{name}" создана')
        else:
            print(f'Директория "{name}" уже существует!')


def del_dirs(quantity):
    for i in range(1, quantity+1):
        name = os.path.join(os.getcwd(), f'dir_{i}')
        if os.path.exists(name):
            print(f'Директория "{name}" существует и будет удалена')
            os.removedirs(name)
            print(f'Директория "{name}" удалена!')
        else:
            print(f'Директории "{name}" не существует.')




