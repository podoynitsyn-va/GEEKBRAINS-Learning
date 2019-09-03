import json
import pickle


def deserialize_json():
    with open('group.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def deserialize_pickle():
    with open('group.pickle', 'rb') as file:
        return pickle.load(file)


print(deserialize_json())
print(deserialize_pickle())
