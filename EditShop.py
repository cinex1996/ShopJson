import json
import os.path
from json import JSONDecodeError


def EditShop():
    isTrue = False
    try:
        with open("shop.json","r") as file:
            shop = json.load(file)
    except JSONDecodeError:
        print("Źle sczytany plik z bazy danych")
    print("""Co ty chcesz zedytować
    1.Zmień nazwę
    2.Zmień cenę""")
    try:
        choice = int(input("Podaj swój wybór"))
    except ValueError:
        print("Wartość musi być liczbą")
        return
    if choice == 1:
        OldNamePhone = input("Podaj nazwe telefonu który ty szukasz do edycji")
        if os.path.exists("shop.json"):
            for namePhone in shop:
                   if namePhone["Name Phone"] == OldNamePhone:
                       print("Znaleziono Telefon")
                       NewNamePhone = input("Podaj nazwę nowego telefonu")
                       namePhone["Name Phone"] = NewNamePhone
                       break
                   else:
                        print("Nie znaleziono telefonu")
                        break
    elif choice == 2:
        OldNamePhone = input("Podaj nazwę swojego telefonu ")
        if os.path.exists("shop.json"):
            for namePhone in shop:
                if namePhone["Name Phone"] == OldNamePhone:
                    print("Znaleziono telefon")
                    NewPrice = int(input("Podaj nową cenę tego telefonu"))
                    namePhone["Price"] = NewPrice
                    isTrue = True
                    break
        if not isTrue:
            print("Nie posiadamy tekiego telefonu")
    else:
        print("Zły wybór")
        return
    with open("shop.json","w") as file:
        json.dump(shop, file, indent=4,ensure_ascii=False)

