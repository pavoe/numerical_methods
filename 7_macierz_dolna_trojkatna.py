def ukladL(L,b):   # gdzie L - macierz dolna trojkatna, b - wektor wyrazow wolnych
    x = [0 for a in range(len(b))]      # rozwiazanie - wektor x
    for i in range(0,len(b)):
        y = b[i]    # odpowiadajacy wyraz wolny, ktory bedzie za chwile zmienny
        for j in range(0,i):
            # eliminacja wspolczynnikow macierzy ze znanymi x, aby dostac sie
            # za chwile do nieznanego x 
            y -= L[i][j] * x[j] 
        x[i] = y / L[i][i]
    return x


L = [[1,0,0],
     [2,3,0],
     [1,-1,2]]
b = [-1,2,3]

print(ukladL(L,b))


L = [[-2,0,0],
     [1,3,0],
     [4,2,2]]
b = [2,5,2]

print(ukladL(L,b))


L = [[-2,0],
     [1,1]]
b = [2,5]

print(ukladL(L,b))