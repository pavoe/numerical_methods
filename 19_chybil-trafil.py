import random, math

# całka z sin(x) w zakresie [0,pi]
# metoda Monte Carlo 'chybil-trafil' (hit-or-miss)
# x losujemy w [0,pi], y losujemy w [0,1]
# ponizsza metoda dziala poprawnie tylko dla funkcji przecinajacych sie z osia OX


def chybil_trafil(a,b):
    minF = 0
    maxF = 1
    n = 10000
    k = 0
    for i in range(n):
        x = random.uniform(a,b)        # x losowane z przedzialu calkowania [a,b]
        y = random.uniform(minF,maxF)  # y losowane z przedzialu zmiennosci funkcji [minF,maxF]
        if (func(x) >= 0):
            if ( (y > 0) and (y <= func(x)) ):
                k = k + 1  # trafienie
        else:
            if ( (y < 0) and (y >= func(x)) ):
                k = k - 1  # trafienie (k zmniejszam, bo calka dla ujemnych wartosci jest ujemna)
    return k / n * (b - a) * (maxF - minF)

            
def func(x):
    return math.sin(x)


a = 0
b = math.pi
integral = chybil_trafil(a,b)
print(integral)


# dla y = sin(x) w zakresie [0,2*pi]

def chybil_trafil2(a,b):
    minF = -1
    maxF = 1
    n = 10000
    k = 0
    for i in range(n):
        x = random.uniform(a,b)        # x losowane z przedzialu calkowania [a,b]
        y = random.uniform(minF,maxF)  # y losowane z przedzialu zmiennosci funkcji [minF,maxF]
        if (func(x) >= 0):
            if ( (y > 0) and (y <= func(x)) ):
                k = k + 1  # trafienie
        else:
            if ( (y < 0) and (y >= func(x)) ):
                k = k - 1  # trafienie (k zmniejszam, bo calka dla ujemnych wartosci jest ujemna)
    return k / n * (b - a) * (maxF - minF)


a = 0
b = 2 * math.pi
integral = chybil_trafil2(a,b)
print(integral)