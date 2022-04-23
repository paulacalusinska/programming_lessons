# haslo = "kawiarnia"
import random
slowa = open("words_for_hangman.txt").readlines()
haslo = random.choice(slowa)
haslo = haslo.strip()
print("Zgadnij słowo. Masz 10 prób.")

rozwiazanie = []
for element in haslo:
    rozwiazanie.append('_')

proba = 0
while True:
    print(rozwiazanie)


    litera = input("Podaj literę: ")
    proba = proba+1
    for i in range(len(haslo)):
        if litera == haslo[i]:
            rozwiazanie[i] = litera

    if "_" not in rozwiazanie:
        print(f"Brawo! Zgadłeś w {proba} próbie! Słowo to: {rozwiazanie}")
        break

    if proba == 10:
        print("Koniec! Wykorzystałeś wszystkie próby :(")
        break

