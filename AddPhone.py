import json
import os.path


def addPhone():
    namePhone = input("Podaj nazwę telefonu")
    price = int(input("Podaj cenę telefonu"))
    JsonFile = {
            "Name Phone":namePhone,
            "Price":price
        }
    if os.path.exists("shop.json"):
        try:
            with open("shop.json","r",encoding="utf-8") as file:
               ShopPhone = json.load(file)
        except json.JSONDecodeError:
            print("Plik jest uszkodzony")
            ShopPhone = []
    else:
        ShopPhone = []
    ShopPhone.append(JsonFile)
    with open("shop.json","w",encoding="utf-8") as file:
        json.dump(ShopPhone, file, indent=4, ensure_ascii=False)