soluciones = 0

def show_solution(a):
    global soluciones
    soluciones += 1

def es_solucion(k, n):
    return k == n

def crear_candidatos(a, k, n, cand):
    c = 0
    for i in range(n):
        legal = True
        for j in range(k):
            if abs(k-j) == abs (i-a[j]): #AMENAZA EN DIAGONAL
                legal = False
            if (i == a[j]):              #AMENAZA EN COLUMNA
                legal = False
        if legal:
            cand.append(i)
            c += 1

def backtrack(a, k, n):
    if es_solucion(k, n):
        show_solution(a)
    else:
        cand = [] #aqui se guardan los candidatos
        crear_candidatos(a, k, n, cand)
        k = k + 1
        for c in cand:
            a.append(c)            
            backtrack(a, k, n)
            a.pop()

def nQueens():
    global soluciones
    backtrack([], 0, 10)
    print("10 = n , Soluciones: ", soluciones)

nQueens()