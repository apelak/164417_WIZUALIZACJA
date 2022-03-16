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

