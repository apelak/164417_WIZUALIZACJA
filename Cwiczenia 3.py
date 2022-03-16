import math
# lista = []
# for element in sekwencja:
#     if warunek_na_element:
#         lista.append(akcja_na_element)
# lista = [akcja_na_element for element in sekwencja if warunek_na_element]

# a = [pow(x, 2) for x in range(10)]
# print(a)
#
# b = [pow(3, x) for x in range(6)]
# print(b)
#
# c = [x for x in a if x % 2 != 0]
# print(c)


# lista = []
# for a in [1,2,3]:
#     for b in [4,5,6]:
#         lista.append((a, b))
# print(lista)
# lista2 = [(a, b) for a in [1, 2, 3] for b in [4, 5, 6]]
# print(lista2)

# slownik = {'PZU': 'Państwowy Zakład Ubezpieczeń',
#            'ZUS': 'Zakład Ubezpieczeń Społecznych',
#            'PKO': 'Państwowa Kasa Oszczędności'}
# slownikOdwrocony = {}
# for key, value in slownik.items():
#     slownikOdwrocony[value] = key
# print(slownik)
# print(slownikOdwrocony)
# slownik2 = {value: key for key, value in slownikOdwrocony.items()}
# print(slownik2)

# 3oo304l
# funkcje
# def nazwa_funkcji(arg pozycyjne, domyślne = wartość, *argument, **argument):
# instrunkcje
# return


# def row_kwadratowe(a, b, c):
#     delta = b**2 - 4 * a * c
#     if delta < 0:
#         print("Brak rozwiazan")
#         return -1
#     elif delta == 0:
#         print("jedno rozwiazanie: ")
#         x = (-b)/(2*a)
#         return x
#     else:
#         print("dwa rozwiazania")
#         x1 = ((-b) - m.sqrt(delta))/(2 * a)
#         x2 = ((-b) + m.sqrt(delta))/(2 * a)
#         return x1, x2
#
#
# print(row_kwadratowe(6, 1, 3))
# print(row_kwadratowe(1, 2, 1))
# print(row_kwadratowe(1, 4, 1))

# def parzystosc(a):
#     if a % 2 == 0:
#         return "parzysta", a
#     return "nieparzysta", a
#
#
# print(parzystosc(4))
# print(parzystosc(5))

# def dlugosc_odcinka(x1=0, y1=0, x2=1, y2=1):
#     return math.sqrt((x2-x1)**2-(y2-y1)**2)
#
# #argumenty domyslne
# print(dlugosc_odcinka())
# #agrumenty pozycyjne
# print(dlugosc_odcinka(4, 5, 6, 9))
# #dwa pierwsze argumenty pozycyjne, kolejne dwa wpisywane wartosci
# print(dlugosc_odcinka(1, 1, y2=8, x2=0))
# #wartosc przypisywana do danego argumentu
# print(dlugosc_odcinka(y2=3, x1=5, y1=6, x2=0))
# #dwa pierwsze argumenty jako domyslne, kolejne dwa z nowa wartoscia
# print(dlugosc_odcinka(y2=1, x2=6))

def co_lubie(** rzeczy):
    for cos in rzeczy:
        print("lubie")
        print(cos)
        print("co lubie")
        print(rzeczy[cos])


co_lubie(gry=['planszowe', 'komputerowe'])


