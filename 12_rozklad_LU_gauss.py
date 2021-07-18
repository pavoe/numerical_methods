# Funkcja tworzaca rozklad LU macierzy za pomoca eliminacji Gaussa.

def rozklad_LU_gauss(A):
    n = len(A[0])
    L = [[0 for each in range(n)] for each in range(n)]  # inicjalizacja L
    for i in range(n):
        L[i][i] = 1
    U = A   # inicjalizacja U, bedzie ona przeksztalcana z macierzy A do koncowej macierzy U
    # uzupelniam macierze L i U jednoczesnie
    for i in range(n-1):   # od 1 do n-1 <=> od 0 do n-2 <--- odejmowany wiersz
        for j in range(i+1, n): # od i+1 do n <=> od [i+1] do [n-1] <--- od ktorego wiersza odejmujemy
            m = U[j][i] / U[i][i]   # mnoznik m_ji, niezalezny od k
            L[j][i] = m
            for k in range(i, n):   # od i do n <=> od [i] do [n-1] <--- kolejne wspolczynniki
                U[j][k] = U[j][k] - m * U[i][k]
    return L,U




A = [[3,2,3],
     [-9,-4,-6],
     [12,12,14]]

print(rozklad_LU_gauss(A))


A = [[1,1,4],
     [2,0,10],
     [3,-7,24]]

print(rozklad_LU_gauss(A))