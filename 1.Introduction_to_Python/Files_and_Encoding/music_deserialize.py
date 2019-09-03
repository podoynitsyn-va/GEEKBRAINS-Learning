import pickle
import json


with open('group.pickle', 'rb') as file_pickle:
    music_group_pickle = pickle.load(file_pickle)
    file_pickle.close()

print('Словарь, загруженный из group.pickle:')
print(music_group_pickle)

with open('group.json', 'rb') as file_json:
    music_group_json = json.load(file_json)
    file_json.close()

print('Словарь, загруженный из group.json:')
print(music_group_json)

