import json
import pickle

my_favourite_group = {
    'name': 'Vacuum',
    'tracks': ['I Breath', 'Power', 'Satyricon'],
    'albums': [{'name': 'Seance at the Chaebol', 'year': 1998},
               {'name': 'The Plutonium Cathedral', 'year': 1997},
               {'name': 'Your Whole Life Is Leading Up to This', 'year': 2004}]
}


def serialize_json(obj):
    with open('group.json', 'w', encoding='utf-8') as file:
        print(json.dumps(obj))
        json.dump(obj, file)


def serialize_pickle(obj):
    with open('group.pickle', 'wb') as file:
        print(pickle.dumps(obj))
        pickle.dump(obj, file)


serialize_json(my_favourite_group)
serialize_pickle(my_favourite_group)
