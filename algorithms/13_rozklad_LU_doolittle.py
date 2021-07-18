# Funkcja tworzaca rozklad LU macierzy za pomoca metody Doolittle'a.

def rozklad_LU_doolittle(A):
    n = len(A[0])
    L = [[0 for each in range(n)] for each in range(n)]     # inicjalizacja L
    for i in range(n):
        L[i][i] = 1
    U = [[0 for each in range(n)] for each in range(n)]     # inicjalizacja U
    for i in range(n):          # pierwszy wiersz - latwe do przypisania wartosci U
        U[0][i] = A[0][i]
    for k in range(n):          # kolumny
        for w in range(1,n):    # wiersze - z pominieciem juz obliczonego 1. wiersza
            sum = 0
            if (w > k):         # gdy w > k, uzupelniam macierz L, nie U
                for x in range(k):
                    sum += L[w][x] * U[x][k]
                L[w][k] = (A[w][k] - sum) / U[k][k]
            else:
                for x in range(k):
                    sum += L[w][x] * U[x][k]
                U[w][k] = A[w][k] - sum
    return L,U


A = [[3,2,3],
     [-9,-4,-6],
     [12,12,14]]

print(rozklad_LU_doolittle(A))


A = [[1,1,4],
     [2,0,10],
     [3,-7,24]]

print(rozklad_LU_doolittle(A))