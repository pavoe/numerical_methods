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



U = [[3,-4,3],
     [0,2,3],
     [0,0,-2]]
b = [23,2,-4]
print(ukladU(U,b))


U = [[2,-3,-1],
     [0,4,3],
     [0,0,2]]
b = [9,-11,-2]
print(ukladU(U,b))


U = [[2,0,(10/3)],
     [0,3,2],
     [0,0,3]]
b = [-(2/3),5,3]
print(ukladU(U,b))