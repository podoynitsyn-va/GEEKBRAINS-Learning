import pickle
import json


my_favorite_music_group = {
    'name': 'AC/DC',
    'tracks': ['Back in Black', 'The Razors Edge', 'Highway to Hell', 'Touch too Much', 'Thunderstruck'],
    'albums': [{'name': 'The Razors Edge', 'year': 1990},
               {'name': 'Back in Black', 'year': 1980},
               {'name': 'Highway to Hell', 'year': 1979}]
}

with open('group.pickle', 'wb') as file_pickle:
    pickle.dump(my_favorite_music_group, file_pickle)
    file_pickle.close()

print(f'Объект my_favorite_music_group записан в байты в файл {file_pickle.name}')

with open('group.json', 'w', encoding='utf-8') as file_json:
    json.dump(my_favorite_music_group, file_json)
    file_json.close()

print(f'Объект my_favorite_music_group записан в json в файл {file_json.name}')

