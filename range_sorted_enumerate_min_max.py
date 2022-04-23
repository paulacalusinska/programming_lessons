A = [1,2,3,4,5,6,7,8,9,100,34,35]

def wypisz_parzyste(lista):
    parzyste = []
    for e in lista:
        if e % 2 == 0:
            parzyste.append(e)
    return parzyste

print(wypisz_parzyste(A))

def wypisz_parzyste2(lista):
    return[e for e in lista if e % 2 == 0]
print(wypisz_parzyste2(A))

B = [1,1,1,2,2,2]
print(B)
C = [n/2 for n in B]
print(C)
D = [n for n in B if n == 1]
print(D)


def najwieksza_liczba(lista):
    if len(lista) == 0:
        return None
    i_max = 0
    max = lista[i_max]
    for i, e in enumerate(lista):
        if e > max:
            max = e
            i_max = i
    return max, i_max
print(najwieksza_liczba(A))

E = [5, -4, 6, -80, 45, 100, -3, 4]

def dodatnie_ujemne(lista):
    dodatnie = []
    ujemne = []
    for e in lista:
        if e >= 0:
            dodatnie.append(e)
        else:
            ujemne.append(e)
    return dodatnie, ujemne
print(dodatnie_ujemne(E))

F = [-3,1,2,3,4,5,6,7]
def kwadraty_liczb(lista):
    return sorted([e**2 for e in lista])
    # lista_kwadraty_liczb = []
    # for e in lista:
    #     lista_kwadraty_liczb.append(e**2)
    # return lista_kwadraty_liczb

print(kwadraty_liczb(F))

def czy_liczba_pierwsza(liczba):
    dzielniki = 0
    for dzielnik in range(1, liczba + 1):
        if liczba % dzielnik == 0:
            dzielniki += 1
            if dzielniki == 3:
                break
    if dzielniki == 2:
        return True
    else:
        return False
print(czy_liczba_pierwsza(12))



# abcdef
# bcdefa
# cdefab

def wypisz_parzyste(k, n):
    parzyste = []
    for e in range (n, n+k*2):
        if e % 2 == 0:
            parzyste.append(e)
    return parzyste
print(wypisz_parzyste(3, 11))