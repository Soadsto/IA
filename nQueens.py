soluciones = 0

def es_solucion(k, n):
    return k == n

def crear_candidatos(a, k, n, cand):
    for i in range(n):
        legal = True
        for j in range(k):
            if abs(k - j) == abs (i - a[j]): #AMENAZA EN DIAGONAL
                legal = False
            if (i == a[j]):                  #AMENAZA EN COLUMNA
                legal = False
        if legal:
            cand.append(i)

def backtrack(a, k, n):
    global soluciones
    if es_solucion(k, n):
        soluciones += 1        
    else:
        cand = [] #aqui se guardan los candidatos
        crear_candidatos(a, k, n, cand)
        k = k + 1
        for c in cand:
            a.append(c)            
            backtrack(a, k, n)
            a.pop()
 
def leer():
    while True:
        try:
            size = int(input("Tamaño del tablero = "))
            if size == 1:
                print("Solucion trivial")
            if size <= 3:
                print("No existen soluciones para tableros < 4")
                continue
            return size
        except ValueError:
            print("Dato invalido. Escribe de nuevo")

def nQueens():
    global soluciones
    n =  leer()
    backtrack([], 0, n)
    print("Soluciones: ",soluciones)

nQueens()