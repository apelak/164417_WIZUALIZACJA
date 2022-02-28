# Zadanie 1
a1 = 4
a2 = 5
print(a1," ",a2)
b1 = 4.3
b2 = 2.1
print(b1," ",b2)
c1 = "wizualizacja"
c2 = "danych"
print(c1+" "+c2)
d1 = 2j
d2 = 2 + 3.8j
print(d1," ",d2)

#Zadanie 2
a = input(float("Podaj 1 liczbe: "))
b = input(float("Podaj 2 liczbę: "))
c = input("1.Dodawanie 2.Odejmowanie 3.Mnożenie 4.Dzielenie 5.Potęgownie")
def dodawanie():
    print(a+b)
def odejmowanie():
    print(a-b)
def mnozenie():
    print(a*b)
def dzielenie():
    print(a/b)
def potegowanie():
    print(a+b)

switcher = {
    1:'dodawanie',
    2:'odejmowanie',
    3:'mnozenie',
    4:'dzielenie',
    5:'potegowanie',

}


