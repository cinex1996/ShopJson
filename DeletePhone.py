import json
from json import JSONDecodeError


def delete():
    isTrue = False
    FileFound="shop.json"
    try:
        with open(FileFound,"r", encoding="utf-8") as file:
            people = json.load(file)
    except JSONDecodeError:
        print("Plik jest uszkodzony")
    NameDelete = input("Podaj nazwę telefonu który chcesz usunąć")
    for row in people:
        if row["Name Phone"] == NameDelete:
            people.remove(row)
        else:
            print("Nie posiadamy takiego modelu telefonu")
    with open(FileFound,"w",encoding="utf-8") as file:
        json.dump(people,file,indent=4,ensure_ascii=False)
    print("Zapisano pomyślnie wszystko")