#def Tuzinowski_Pawel_silnia2(x):   # rekurencyjnie
#    if x == 1:
#        return 1
#    return x * Tuzinowski_Pawel_silnia2(x - 1)

def Tuzinowski_Pawel_silnia(x):
    result = 1
    for x in range(x, 1, -1):
        result = result * x
    return result


a = 3
b = 5
c = 10  
d = 0

print(a, "!  =  ", Tuzinowski_Pawel_silnia(a))
print(b, "!  =  ", Tuzinowski_Pawel_silnia(b))
print(c, "!  =  ", Tuzinowski_Pawel_silnia(c))
print(d, "!  =  ", Tuzinowski_Pawel_silnia(d))