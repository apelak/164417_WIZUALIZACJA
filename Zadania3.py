#Zadanie 1
a = [1-x for x in range(10)]
print(a)

b = [4**x for x in range(8)]
print(b)

c =[x for x in b if x % 2 == 0]
print(c)

#Zadanie 2
import random as r
d = [r.randint(0, 100) for x in range(10)]
print(d)
e = [x for x in d if x % 2 == 0]
print(e)

#Zadanie 3
slownik = {'mąka': 'kg',
           'czosnek': 'szt',
           'sól': 'kg',
           'chleb': 'szt'}
nowa = [key for key, value in slownik.items() if value == 'szt']
print(nowa)

#Zadanie 4

def czy_prostokatny(a, b, c):
    if a**2+b**2==c**2:
        print("Jest prostokatny")
        return 1
    else:
        print("Nie jest prostokatny")
        return 0

print(czy_prostokatny(3, 4, 5))

#Zadanie 5

def pole_trapezu(a=4, b=5, h=3):
    return (a+b)*h/2

print(pole_trapezu())

#Zadanie 6

def iloczyn(a=1, b=4, ile=10):
    if a == 0:
        return 0
    else:
        ciag = []
        for x in range(ile):
            ciag.append(a*(b**x))
        print(ciag)
        iloczyn = 1
        for x in ciag:
            iloczyn *=x
    return iloczyn
print(iloczyn())

#Zadanie 7

def iloczyn2(*ciag):
    if len(ciag) == 0:
        return 0
    else:
        iloczyn = 1
        for x in ciag:
            iloczyn *= x
    return iloczyn
print(iloczyn2())

#zadanie 8

def zakupy(** pl):
    print("Wszystkich produktów jest", len(pl.keys()))
    return sum(pl.values())


print(zakupy(jaja=40, bułka=50, mleko=30))

#Zadanie 9

from ciągi import *

print(ciągi_arytmetyczne.n_wyraz(1, 1, 100))
print(ciągi_geometryczne.n_wyraz(1, 5, 4))