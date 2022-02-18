entries = []
from datetime import date

def dodaj():
    nowy_wpis = input("Dodaj wpis: ")
    data_wpisu = date.today()
    d1 = data_wpisu.strftime("%d/%m/%Y")
    wpis = (nowy_wpis, d1)
    entries.append(wpis)


def czytaj():
    for wpisy in entries:
        print(wpisy)


while True:
    warunek = int(input("1 - dodaj 2 - czytaj 3 - wyjdź: "))
    if warunek == 1:
        dodaj()
    if warunek == 2:
        czytaj()
    if warunek == 3:
        break

#wypisywać entries oddzielnie i do kazdego datę