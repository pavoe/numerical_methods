def Tuzinowski_Pawel_mnoz_mac(A,B):
    # wymiar macierzy zwracanej to (wiersze macierzy A)x(kolumny macierzy B) 
    wA = len(A)     # wiersze A
    kB = len(B[0])  # kolumny B
    kA = len(A[0])  # kolumny A, potrzebne do przechodzenia podczas mnożenia (zmienna k)
    # inicjalizacja macierzy
    C = [ [ 0 for y in range(wA) ] for x in range(kB) ]
    for indW in (0,wA-1,1):    # uzupełniam macierz zwracaną
        for indK in (0,kB-1,1):
            C[indW][indK] = 0
            for k in range(0,kA):
                C[indW][indK] += A[indW][k] * B[k][indK]
    return C


A1 = [[2,3],
      [1,5]]
B1 = [[1,7],
      [3,2]]
C1 = Tuzinowski_Pawel_mnoz_mac(A1, B1)
print(C1)

A2 = [[1,4,6],
      [7,-1,-5],
      [10,0,1]]
B2 = [[2,2,8],
      [0,-4,-10],
      [5,5,-1]]
C2 = Tuzinowski_Pawel_mnoz_mac(A2, B2)
print(C2)


A3 = [[1,5,7],
      [0,-3,4]]
B3 = [[0,1],
      [10,15],
      [-7,3]]
C3 = Tuzinowski_Pawel_mnoz_mac(A3, B3)
print(C3)
