# Napisac algorytm metody zlotego podzialu (optymalizacja):
# Deklaracja funkcji: def Nazwisko_Imie_zloty_podzial(a,b,eps)
# Uwagi:
#  a, b - granice poszukiwania minimum funkcji
#  eps - dokladnosc obliczen

import math

p = (math.sqrt(5)-1)/2

def zloty_podzial(a,b,eps):
    xL = b - p * (b - a)
    xR = a + p * (b - a)
    while ((b - a) > eps):
        if (func(xL) > func(xR)):
            a = xL
        else:
            b = xR
        xL = b - p * (b - a)
        xR = a + p * (b - a)
    return xR

def func(x):
    #return (x-2)*(x+3)*(x-4)
    return (x+2)*(x-1)*(x+6)




# testy




# dla (x-2)*(x+3)*(x-4)

# a = 2.1
# b = 3.85
# eps = 0.00001
# print(zloty_podzial(a,b,eps))



# dla (x+2)*(x-1)*(x+6)

a = -2
b = 0.7
eps = 0.00001
print(zloty_podzial(a,b,eps))