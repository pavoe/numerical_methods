# Dzielenie wielomianu przez dwumian.
# a - tablica wspolczynnikow dzielonego wielomianu w(x) [a_n*x^n + ... + a1*x + a0]
# c - wartosc w dwumianie, przez ktory dzielimy -> (x-c)
# *   zwracamy tablice b wspolczynnikow wielomianu v(x) bedacego wynikiem dzielenia
#     oraz reszte r   [ W(x) = (x-c)V(x)+r ]
# v(x) = b_n-1 * x^(n-1) + ... + b1*x + b0

def horner2(a,c):
    b = [ 0 for x in range(len(a)-1) ]  # inicjalizacja tablicy b
    b[len(b)-1] = a[len(b)]     # przypisanie ostatniego wspolczynnika
    for i in range(len(a)-2, 0, -1):    # kolejne wspolczynniki
        b[i-1] = a[i] + c * b[i]
    r = a[0] + c * b[0]     # reszta
    return b,r


def wypisz(a):
    calc = str(a[0])
    for i in range(1, len(a), 1):
        calc = calc + " + " + str(a[i]) + " * x^" + str(i)
    return calc


a = [4,2,6,8,-5,1,0,-3]
c = 3
print('W(x) = ' + str(wypisz(a)))
print('/ (x - ' + str(c) + ')')
print('V(x) = ' + str(wypisz(horner2(a,c)[0])) + ' r. ' + str(horner2(a,c)[1]))
print()


a = [-5,10,12]
c = 2
print('W(x) = ' + str(wypisz(a)))
print('/ (x - ' + str(c) + ')')
print('V(x) = ' + str(wypisz(horner2(a,c)[0])) + ' r. ' + str(horner2(a,c)[1]))
print()


a = [1594,-123,781,0,15]
c = 23
print('W(x) = ' + str(wypisz(a)))
print('/ (x - ' + str(c) + ')')
print('V(x) = ' + str(wypisz(horner2(a,c)[0])) + ' r. ' + str(horner2(a,c)[1]))