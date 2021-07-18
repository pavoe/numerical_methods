# Funkcja wyliczania wartosci wielomianu w(x) dla danej wartosci x.
# (za pomocą minimalnej iloci mnożeń i dodawań -> n + n)
# W(x) = a0 + x(a1 + x(a2 + ... + x(a_n-1 + xa_n)))
# a - tablica wspolczynnikow wielomianu w(x) (a0 + a1*x + a2*x^2 + ...)
# x - wartosc, dla ktorej liczymy wartosc wielomianu

def horner(a,x):
    result = a[len(a)-1]
    for i in range(len(a)-2, -1, -1):
        result = result * x + a[i]
    return result


def wypisz(a,x):
    calc = str(a[0])
    for i in range(1, len(a), 1):
        calc = calc + " + " + str(a[i]) + " * (" + str(x) + ")^" + str(i)
    return calc


a = [1,2,3]
x = 2
print(str(wypisz(a,x)) + " = " + str(horner(a,x)))

a = [1,2,3]
x = 0
print(str(wypisz(a,x)) + " = " + str(horner(a,x)))

a = [5,-2,8,0]
x = -2
print(str(wypisz(a,x)) + " = " + str(horner(a,x)))

a = [0,4,-3,-7,10,-12]
x = 1
print(str(wypisz(a,x)) + " = " + str(horner(a,x)))