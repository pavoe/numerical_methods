# Funkcja przeksztalcajaca macierz symetryczna w macierz L
# (ktora mozna odbic i latwo otrzymac macierz U dla rozkladu LU).

from math import sqrt

def rozklad_cholesky(A):
    n = len(A[0])
    L = [[0 for each in range(n)] for each in range(n)]     # inicjalizacja L
    for k in range(n):
        for w in range(k,n):
            sum = 0
            if(w == k):     # diagonala
                for x in range(k):
                    sum += L[w][x] * L[w][x]
                L[w][w] = sqrt((A[w][w] - sum))
            else:           # pod diagonala
                for x in range(k):
                    sum += L[w][x] * L[k][x]
                L[w][k] = (A[w][k] - sum) / L[k][k]
    return L



A = [[4,-6,8],
     [-6,10,-10],
     [8,-10,29]]

print(rozklad_cholesky(A))