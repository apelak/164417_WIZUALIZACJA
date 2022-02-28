import math

# Zadanie 1
a1 = 4
a2 = 5
print(a1, a2)
b1 = 4.3
b2 = 2.1
print(b1, b2)
c1 = "wizualizacja"
c2 = "danych"
print(c1+" "+c2)
d1 = 2j
d2 = 2 + 3.8j
print(d1, d2)
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

a = 2
a += 2
print(a)
b = 3
b -= 1
print(b)
c = 3
c *= 2
print(c)
d = 4
d /=2
print(d)
e = 2
e **= 3
print(e)
f = 7
f %= 3
print(f)
del a, b, c, d, e, f

#Zadanie 4

print(math.e**10)

print(pow(math.log(5 + (math.sin(8)) ** 2, math.e), 1/6))

print(math.floor(3.55))

print(math.ceil(4.80))

#Zadanie 5

imie = "ARKADIUSZ"
nazwisko = "PELAK"
print(imie.capitalize(), nazwisko.capitalize())

#Zadanie 6

slowa = "la la la"
print(slowa.count("la"))

#Zadanie 7

string = "Wizualizacja Danych"
print(string[1], "\n", string[-1])
del string

#Zadanie 8

print(slowa.split(" "))

#Zadanie 9

string = "Lubie pociagi"
float =  3.14
hex = hex(28)
print('{0:s} {1:f} {2:s}'.format(string, float, hex))
print(type(hex))

s = "nie no ta\n"
f = 98.652
h = "0xF0"

print(s + "jeszcze %(to)f" % {'to': f})
print("albo nawet {0:.3f}".format(f))
print(int(h, 16))