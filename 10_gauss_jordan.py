# Napisac funkcje do algorytmu eliminacji Gaussa-Jordana bez wyboru elementu podstawowego.
# A - macierz wspolczynnikow ukladu rownan
# b - wektor wyrazow wolnych

def gauss_jordan(A,b):
    n = len(b)                  # macierz kwadratowa n x n
    for i in range(n):          # od 1 do n <=> od 0 do n-1 <--- odejmowany wiersz
        for j in range(n):      # od 1 do n <=> od 0 do n-1 <--- od ktorego odejmuje
            if (j==i):          # nie dopuszczamy do odejmowania tego samego wiersza od siebie
                continue
            m = A[j][i] / A[i][i]   # mnoznik m_ji, niezalezny od k
            for k in range(i,n):    # od i do n <=> od [i] do [n-1] <--- kolejne wspolczynniki
                A[j][k] = A[j][k] - m * A[i][k]
            b[j] = b[j] - m * b[i]  # odejmuje rowniez odpowiednie wiersze wektora b
    # w ten sposob macierz A stanie sie macierza diagonalna
    # pamietac nalezy jednak, ze na diagonali sa to wciaz jakies wspolczynniki
    # koncze wiec obliczenia, aby zwrocic wektor x
    x = [0 for a in range(n)]
    for a in range(n):
        x[a] = b[a] * (1/A[a][a])
    return x



A = [[2,-3,-1],
     [-4,10,5],
     [8,-4,4]]
b = [9,-29,12]
print(gauss_jordan(A,b))


A = [[2,1,4],
     [6,6,14],
     [4,14,19]]
b = [1,8,25]
print(gauss_jordan(A,b))

A = [[3,2],
     [4,-1]]
b = [-8,-7]
print(gauss_jordan(A,b))

A = [[8,1,2],
     [5,-3,-7],
     [0,-5,7]]
b = [16,-22,11]
print(gauss_jordan(A,b))