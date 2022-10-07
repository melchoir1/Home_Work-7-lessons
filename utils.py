import json

def load_students():
    with open("./students.json", "r") as students:
        return json.load(students) #читаем файл

def load_professions():
    with open("./professions.json", "r") as professions:
        return json.load(professions) #читаем файл

