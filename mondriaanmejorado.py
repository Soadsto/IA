soluciones = 0
def es_solucion(numMov):
    return numMov > m*n/2

def crearCandidatos(a, numMov, cand):

    if c + 1 < n and a[r][c + 1] == 0:
        a[r][c], a[r][c + 1] = numMov, numMov
        backtrack(numMov + 1)
        a[r][c], a[r][c + 1] = 0, 0
    if r + 1 < m and a[r + 1][c] == 0:
        a[r][c], a[r + 1][c] = numMov, numMov
        backtrack(numMov + 1)
        a[r][c], a[r + 1][c] = 0, 0
            
def backtrack(a, ,):
    if es_solucion(numMov):
        global soluciones
        print(a)
        soluciones += 1
    else:
        cand = []
        

m = int(input("Renglones: "))
n = int(input("Columnas: "))
matirz = [[0 for i in range(n)] for i in range(m)]
backtrack([], 0)    