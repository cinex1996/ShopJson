import json
import os.path
from json import JSONDecodeError


def display():
    fileName = "shop.json"
    if not os.path.exists(fileName):
        print("Nie istnieje taki plik")
        return
    else:
        with open(fileName,"r", encoding="UTF-8") as file:
            try:
                people = json.load(file)
                print(json.dumps(people, indent=4, ensure_ascii=False))
            except JSONDecodeError:
                print("Taki plik nie istnieje")
            except FileNotFoundError:
                print("Taki plik nie istnieje")
