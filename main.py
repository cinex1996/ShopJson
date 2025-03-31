import sys
from DisplayInformation import display
from AddPhone import addPhone
from EditShop import EditShop
from DeletePhone import delete
def main():
    while True:
        print("Witamy w naszym sklepie online!")
        print("""1.Wyświetl informacje
        2.Dodaj telefon
        3.Edytuj telefon
        4.Usuwanie telefonu
        5.Wyjście z programu""")
        Choice = int(input("Wybież opcje: \n"))
        if Choice == 1:
            display()
        elif Choice == 2:
            addPhone()
        elif Choice == 3:
            EditShop()
        elif Choice == 4:
            delete()
        elif Choice == 5:
            sys.exit()
if __name__ == "__main__":
    main()