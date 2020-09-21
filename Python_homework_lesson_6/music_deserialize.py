# 2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них
# информацию. И получить объект: словарь из предыдущего задания.
import json, pickle

with open('group.json', 'r', encoding='utf-8') as f:
    result = json.load(f)

print(result)
print(type(result))

with open('group.pickle', 'rb') as f:
    music = pickle.load(f)

print(music)
print(type(music))