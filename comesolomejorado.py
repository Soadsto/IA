#Funcion para obtener el renglon dada la posicion
def renglon(posicion):
    r = 0
    while (r+1)*(r+2)/2 < posicion:
        r += 1
    return r

#Funcion para obtener la columna dada la posicion
def columna(posicion):
    r = 0
    while (r+1)*(r+2)/2 < posicion: 
        r += 1
    return int(posicion-r*(r+1)/2) 

def posicion(renglon, columna):
    return int(renglon*(renglon + 1)/2 + columna)

def es_solucion(k):
    return k == 13

def crearCandidatos(a, input, cand):
    p = a[-1] #Posicion del ultimo moviento
    i, j = renglon(p), columna(p)
    if j - 2 >= 0: # mov 5
        if input[posicion(i, j-1)] and input[posicion(i, j-2)]:
            cand.append(posicion(i, j-2))
    if i - 2 >= 0 and j - 2 >= 0: #mov 3
        if input[posicion(i-1, j-i)] and input[posicion(i-2, j-2)]:
            cand.append(posicion(i-2, j-2))
    if i - 2 >= 0: #mov 2
        if input[posicion(i-1, j)] and input[posicion(i-2, j)]:
            cand.append(posicion(i-2, j))
    if j + 2 <= 4: #mov 6
        if input[posicion(i, j+1)] and input[posicion(i, j+2)]:
            cand.append(posicion(i, j+2))
    if i + 2 <= 4 and j + 2 <= 4: #mov 4
        if input[posicion(i+1, j+1)] and input[posicion(i+2, j+2)]:
            cand.append(posicion(i+2, j+2))
    if i + 2 <= 4: #mov 1 
        if input[posicion(i+1, j)] and input[posicion(i+2, j)]: 
            cand.append(posicion(i+2, j))            

def backtrack(a, k, input):
    if es_solucion(k):
        print (a)
    else:
        cand = []
        crearCandidatos(a, input, cand)
        k += 1
        for c in cand:
            a.append(c)
            input[c] = False
            backtrack(a, k, input)
            input[c] = True
            a.pop()

def comesolo():
    n = int(input("Ingresa la posicion del 0 al 14: "))
    tablero = [True for i in range(15)] #Aqui acomodamos las posiciones del tablero de arriba hacia abajo
    tablero[n] = False
    backtrack([n], 0, tablero)

comesolo()