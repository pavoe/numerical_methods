# Napisac funkcje rozwiazywania rownan nieliniowych metoda bisekcji.
# Uwagi:
# * szukamy rozwiazania w przedziale [a,b] - w tym przedziale musi byc 1 miejsce zerowe f.
# * badana funkcje mozna zadeklarowac w ramach procedury lub przekazywac jej postac na wejsciu

def bisekcja(a, b, eps):
    c = (a + b) / 2
    # if (signChange(func(c)-eps, func(c)+eps)):
    #     return c
    # if (signChange(a,c)):
    #     bisekcja(a,c,eps)
    # else:
    #     bisekcja(c,b,eps)
    while (not(signChange(func(c-eps), func(c+eps)))):  # dopoki punktu nie ma w obrzezach
           if (signChange(a,c)):
               b = c         # bisekcja(a,c,eps)
           else:
               a = c         # bisekcja(c,b,eps)
           c = (a + b) / 2
    return c
    


def func(x):
    return (x+2)*(x-3)*(x-5)


def signChange(a,b):
    if ((func(a) < 0 and func(b) > 0) or (func(a) > 0 and func(b) < 0)):
        return True
    else:
        return False


a = 2.05
b = 3.45
eps = 0.3
print(bisekcja(a,b,eps))


a = -2.9
b = -1.2
eps = 0.2
print(bisekcja(a,b,eps))