import copy


def Tuzinowski_Pawel_suma_mac(A, B):
    C = copy.deepcopy(A)    # ponieważ macierz wyjsciowa jest wymiaru macierzy wejsciowych
    maxY = len(C) - 1
    maxX = len(C[0]) - 1
    for indY in (0, maxY, 1):
        for indX in (0, maxX, 1):
            C[indY][indX] = A[indY][indX] + B[indY][indX]
    return C        

    

A1 = [[7,1],
     [4,7]]
B1 = [[4,2],
     [5,6]]

A2 = [[3,2,4],
     [1,2,3],
     [7,7,6]]
B2 = [[2,2,2],
     [4,5,1],
     [0,-1,0]]


D = Tuzinowski_Pawel_suma_mac(A1, B1)
D2 = Tuzinowski_Pawel_suma_mac(A2, B2)


print(D)
print(D2)
