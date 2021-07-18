# Napisac algorytm kwadratury prostokatow:
# Deklaracja funkcji: def Nazwisko_Imie_prostokaty(a,b,n)
# Uwagi:
#  a, b - granice calkowania
#  n - liczba wezlow (w takim razie liczba prostokatow = n − 1)


def prostokaty(a,b,n):
    podstawa = (b - a) / (n - 1)     # x_(i+1) - x_i  <-- podstawa prostokata
    t = a
    suma = func(t) * podstawa
    for i in range(1,n):    # od 1 do n-1 (pierwszy prostokat jest juz w sumie)
        t += podstawa
        suma += func(t)
    return suma * podstawa


def func(x):
    return x*x + 5*x + 6


# testy


print(prostokaty(-2,0,100000))

print(prostokaty(4,20,100000))