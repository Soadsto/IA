soluciones = 0
def es_solucion(numMov):
    return numMov > m*n/2

def crearCandidatos(a, numMov, cand):
    
                
def backtrack(a, numMov):
    
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