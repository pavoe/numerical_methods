import math

# a - liczba pierwiastkowana, x - x0, eps - precyzuje przybliżenie
def heron(a,x,eps):  
    test = 1000
    while (test > eps):
        old_x = x
        x = 0.5 * (x + a/x)
        test = math.fabs(x-old_x)
    return x


eps = 0.001

a = 100
print( heron(a, a/2, eps) )

a = 50
print( heron(a, a/2, eps) )

a = 4
print( heron(a, a/2, eps) )

a = 15
print( heron(a, a/2, eps) )

a = 16
print( heron(a, a/2, eps) )