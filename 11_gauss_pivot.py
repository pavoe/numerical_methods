# Napisac funkcje do algorytmu eliminacji Gaussa z czesciowym wyborem elementu podstawowego.
# A - macierz wspolczynnikow ukladu rownan
# b - wektor wyrazow wolnych


def gauss_pivot(A,b):
    n = len(b)      # macierz kwadratowa n x n
    for i in range(n-1):   # od 1 do n-1 <=> od 0 do n-2 <--- odejmowany wiersz
        max = i
        for p in range(i+1,n):  # wyszukiwanie najwiekszej co do modulu wartosci w kolumnie
            if(abs(A[p][i]) > abs(A[max][i])):
                max = p
        if (max != i):          # if(true), nastepuje zamiana poszczegolnych wierszy
            for k in range(i,n):
                temp = A[i][k]
                A[i][k] = A[max][k]
                A[max][k] = temp
            temp2 = b[i]    # zamianie ulegaja takze odpowiednie wiersze wektora b
            b[i] = b[max]
            b[max] = temp2
        for j in range(i+1, n): # od i+1 do n <=> od [i+1] do [n-1] <--- od ktorego wiersza odejmujemy
            m = A[j][i] / A[i][i]   # mnoznik m_ji, niezalezny od k
            for k in range(i, n):   # od i do n <=> od [i] do [n-1] <--- kolejne wspolczynniki
                A[j][k] = A[j][k] - m * A[i][k]
            b[j] = b[j] - m * b[i]  # odejmuje rowniez odpowiednie wiersze wektora b
    # w ten sposob macierz A stanie sie macierza gorna trojkatna
    # posluze sie dodatkowym algorytmem
    x = ukladU(A,b)
    return x

    
# algorytm pomocniczy do macierzy gornej trojkatnej
def ukladU(U,b):   # gdzie U - macierz gorna trojkatna, b - wektor wyrazow wolnych
    x = [0 for a in range(len(b))]      # rozwiazanie - wektor x
    for i in range(len(b)-1,-1,-1):
        y = b[i]    # odpowiadajacy wyraz wolny, ktory bedzie za chwile zmienny
        for j in range(len(b)-1,i,-1):
            # eliminacja wspolczynnikow macierzy ze znanymi x, aby dostac sie
            # za chwile do nieznanego x 
            y -= U[i][j] * x[j] 
        x[i] = y / U[i][i]
    return x




A = [[2,-3,-1],
     [-4,10,5],
     [8,-4,4]]
b = [9,-29,12]
print(gauss_pivot(A,b))


A = [[2,1,4],
     [6,6,14],
     [4,14,19]]
b = [1,8,25]
print(gauss_pivot(A,b))

A = [[3,2],
     [4,-1]]
b = [-8,-7]
print(gauss_pivot(A,b))

A = [[8,1,2],
     [5,-3,-7],
     [0,-5,7]]
b = [16,-22,11]
print(gauss_pivot(A,b))