lista=[3,5,8,10,15]
print (type(lista))
print(lista)
lista.append(5)
print(lista)
print(lista [0])
# print(lista.index(10))
for element in lista:
    print(element)
print(len(lista))
for i in range(len(lista)):
    print(f"Element o indexie {i} ma wartość {lista[i]}")

# lista.append("kawa")
# print(lista)
lista2=[5,6]
lista.extend(lista2)
print(lista)

parzyste_liczby=[]
for element in lista:
    if element % 2 == 0:
        parzyste_liczby.append(element)
print(f"Parzyste liczby to: {parzyste_liczby}")

# napis="Tralalla"
# for element in napis:
#     print(element)

liczba = 7
if liczba in lista:
    print(f"Liczba {liczba} znajduje się w liście {lista}")
else:
    print(f"Liczba {liczba} nie znajduje się w liście {lista}")

slowo = "elementarz"
# SAMOGLOSKI=["a","e","i","o","u","y"]
SAMOGLOSKI = "aeiouy"
samogloski = []
for litera in slowo:
    if litera in SAMOGLOSKI:
        samogloski.append(litera)
print(f"Samogłoski w slowie {slowo} to {samogloski}")
