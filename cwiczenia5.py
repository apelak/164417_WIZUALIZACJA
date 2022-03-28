# zad1

a = [1 - x for x in range(10)]
print(a)

b = [4 ** x for x in range(8)]
print(b)

c = [x for x in b if x % 2 == 0]
print(c)

# zad2

import random as rand

lista1 = [rand.randint(0, 100) for x in range(10)]
print(lista1)
nowa_lista = [x for x in lista1 if x % 2 == 0]
print(nowa_lista)

# zad3

do_kupienia = {"mąka": "kg",
               "cieciorka": "kg",
               "banan": "szt",
               "beer": "hektolitry",
               "wódeczka": "litry",
               "fajki": "szt"}

nowa_lista_zakupow = [x for x, y in do_kupienia.items() if y == "szt"]
print(nowa_lista_zakupow)


# zad4

def prostokatny(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return "jest prostokatny"
    return "nie jest prostokatny"


a, b, c = 3, 4, 5
print(prostokatny(a, b, c))


# zad5

def pole_trapezu(a=2, b=3, h=4):
    return (a + b) * h / 2


print(pole_trapezu())


# zad6

def iloczyn(a1=1, q=4, n=10):
    wynik = a1
    for x in range(1, n + 1):
        wynik *= q
    return wynik


print(iloczyn())


# zad7

def iloczyn2(*liczby, q):
    if len(liczby) == 0:
        return 0
    else:
        iloczyn_liczb = liczby[0]
        for a in liczby:
            iloczyn_liczb *= q
        return iloczyn_liczb


print(iloczyn2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, q=4))

#zad8

def lista_zakupow(**lista):
    zlicz = 0
    for y in lista:
        zlicz += lista[y]
    return len(lista), zlicz

print(lista_zakupow(maka=15, gumowy_penis=100, bananki=15))


#zad9
import ciagi.arytmetyczne as ar
import ciagi.geometryczne as geo

print(ar.n_ty_wyraz(1, 4, 2))
print(geo.suma_wyrazow(5, 1, 8))
