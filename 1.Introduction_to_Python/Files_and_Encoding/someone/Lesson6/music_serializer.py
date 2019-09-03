# 1: Создать модуль music_serialize.py.
# В этом модуле определить словарь для вашей любимой музыкальной группы.
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно.
# В файле group.json указать кодировку utf-8.

import json
import pickle

my_favourtie_band = {
    'name': 'Metallica',
    'tracks': ['Cyanide', 'Fuel'],
    'albums': [{'name': 'Death Magnetic', 'year': 2008},
               {'name': 'Fuel', 'year': 1986}]
}

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourtie_band, f)

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourtie_band, f)
