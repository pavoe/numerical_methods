# całka z sin(x) w zakresie [0,pi]
# metoda średniej całkowej - naiwne Monte-Carlo

import math, random


def monte_carlo(a,b):
    n = 10000
    suma = 0
    for i in range(n):
        x = random.random()     # losuje z przedzialu [0,1]
        z = a + (b - a) * x     # z to wylosowany punkt z dziedziny funkcji calkowanej
        suma += func(z)         # sumuje wartosci funkcji dla rownomiernie losowanych punktow z
    # oszacowana calka to srednia z tych powyzszych wszystkich wartosci dla losowanych punktow
    # pomnozona przez dlugosc przedzialu calkowania [prostokat]
    return ((b - a) / n) * suma

def func(x):
    return math.sin(x)

# dla y = sin(x)
a = 0
b = math.pi
integral = monte_carlo(a,b)
print(integral)



# metoda pod inna funkcje
def monte_carlo2(a,b):
    n = 10000
    suma = 0
    for i in range(n):
        x = random.random()     # losuje z przedzialu [0,1]
        z = a + (b - a) * x     # z to wylosowany punkt z dziedziny funkcji calkowanej
        suma += func2(z)        # sumuje wartosci funkcji dla rownomiernie losowanych punktow z
    # oszacowana calka to srednia z tych powyzszych wszystkich wartosci dla losowanych punktow
    # pomnozona przez dlugosc przedzialu calkowania [prostokat]
    return ((b - a) / n) * suma

def func2(x):
    return x*x*x + 2*x*x + 6

# dla y = x^3 + 2x^2 + 6
a = 0
b = 1
integral = monte_carlo2(a,b)
print(integral)