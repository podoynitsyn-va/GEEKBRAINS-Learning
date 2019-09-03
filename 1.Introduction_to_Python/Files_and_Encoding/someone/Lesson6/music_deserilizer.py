# 2  Создать модуль music_deserialize.py.
# В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
# И получить объект: словарь из предыдущего задания.

import json
import pickle

with open('group.json', 'r') as f:
    json_data = json.load(f)
    print(json_data)

print(type(json_data))

print()

with open('group.pickle', 'rb') as f:
    pickle_data = pickle.load(f)
    print(pickle_data)

print(type(pickle_data))
