import math

# Zadanie 1
a1 = 4
a2 = 5
print(a1, " ", a2)
b1 = 4.3
b2 = 2.1
print(b1, " ", b2)
c1 = "wizualizacja"
c2 = "danych"
print(c1+" "+c2)
d1 = 2j
d2 = 2 + 3.8j
print(d1, " ", d2)
del a1, a2, b1, b2, c1, c2, d1, d2
# Zadanie 2
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
print("1.Dodawanie 2.Odejmowanie 3.Mnożenie 4.Dzielenie 5.Potęgownie: ")
c = int(input())
if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
    print(a*b)
elif c == 4:
    print(a/b)
elif c == 5:
    print(pow(a, b))
else:
    print("nieprawidlowa wartosc")
del a, b, c
# Zadanie 3










