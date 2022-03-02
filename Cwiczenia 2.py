# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))
#
# if a == b:
#     print("liczby sa rowne", a)
# elif a > b:
#     print("a =", a, "jest wieksze od b =", b)
# else:
#     print("b =", b, "jest wieksza od a =", a)

# a = input("Wpisz pierwsza liczbe: ")
# b = input("Wpisz druga liczbe: ")
# c = input("Wpisz trzecia liczbe: ")
# d = input("Wpisz czwarta liczbe: ")
#
# if (a > b) & (c > d):
#     print("a jest wieksze od b i c jest wieksze od d")
# else:
#     print("liczba a jest mniejsza o b lub c jest mniejsze od d")

# for x in range(0, 6, 1):
#     print(x+1)

# for x in lista:
#     print(x)
# else:
#     print("Zostaly wyswietlone wszystkie elementy listy")
# x = 0
# while x <= 10:
#     if x == 6:
#         break
#     print(x)
#     x += 1
# lista = [1, 4, 5, 2, 5, 1, 2, 3, 5]
# liczba = int(input("Podaj liczbe: "))
# licznik = 0
# while licznik < len(lista):
#     if liczba - lista[licznik] == 0:
#         print("liczba " + str(liczba) + " - " + str(lista[licznik]) + " = 0")
#         break
#     else:
#         licznik += 1
# else:
#     print("nie ma takiej liczby")

# lista1 = [1, 4, 5, 2, 5, 1, 2, 3, 5]
# lista2 = [2, 5, 4, 6, 5]
# lista3 = []
# for a in lista1:
#     for b in lista2:
#         wynik = a + b
#         lista3.append(wynik)
#     print(lista3)

# a = input("wczytaj pierwsza liczbe: ")
# b = input("wczytaj druga liczbe: ")
# try:
#     a = int(a)
#     b = int(b)
#     wynik = a / b
#     print(wynik)
# except ZeroDivisionError:
#     print("nie mozna dzielic przez 0")
# except ValueError:
#     print("nie wczytano liczby calkowitej")

# lista = ['a', 5, 5.5, [1, 2, 3]]
# slownik = {klucz:wartosc}
# {1:20, 'a':'b', 2:5}

# lista1 = [1, 4, 5, 2, 5, 1, 2, 3, 5]
# slownik = {1: 20, 'a': 'b', 2: 5}
# print(slownik['a'])
# del slownik['a']
# print(slownik)
# del lista1[2]
# lista1.sort()
# print(lista1)
# slownik.pop(2)
# print(slownik)
# lista1.remove(4)
# print(lista1)
# lista1.reverse()
# print(lista1)
# slownik['k'] = 's'
# print(slownik)
# print(lista1.index(1))
