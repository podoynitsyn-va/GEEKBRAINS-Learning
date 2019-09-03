#ДЗ. Тема 6. Работа с файлами
#1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
#my_favourite_group = {
#‘name’: ‘Г.М.О.’,
#‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
#‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
#{‘name’: ‘Шапито’,‘year’: 2014}]}

#С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
#2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle,
# прочитать из них информацию. И получить объект: словарь из предыдущего задания.

import json
import pickle

import json
import pickle



with open('group.pickle','rb') as f:
    my_favourite_group=pickle.load(f)
    f.close()

print('pickle :', type(my_favourite_group),my_favourite_group)


with open('group.json','r') as f:
    my_favourite_group = json.load(f)
    f.close()

print('JSON   :',type(my_favourite_group),my_favourite_group)
