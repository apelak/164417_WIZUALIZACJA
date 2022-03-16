# lista = []
# for element in sekwencja:
#     if warunek_na_element:
#         lista.append(akcja_na_element)
# lista = [akcja_na_element for element in sekwencja if warunek_na_element]

a = [pow(x, 2) for x in range(10)]
print(a)

b = [pow(3, x) for x in range(6)]
print(b)

c = [x for x in a if x % 2 != 0]
print(c)
