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

def iloczyn(a1=1, q=4, n=10):
    wynik = a1
    kolejny_wyraz = a1
    for x in range(n):
        kolejny_wyraz*=q
        wynik*=kolejny_wyraz
    return wynik
print(iloczyn())

#Zadanie 7

