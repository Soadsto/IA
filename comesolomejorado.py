#Funcion para obtener el renglon dada la posicion
soluciones = 0

def imprime(lista):
    print(lista[0])
    print(*lista[1:3], sep='\t')
    print(*lista[3:6], sep='\t')
    print(*lista[6:10], sep='\t')
    print(*lista[10:], sep='\t')

def renglon(posicion):
    if posicion == 0: return 0
    if posicion < 3: return 1
    if posicion < 6: return 2
    if posicion < 10: return 3
    return 4 
#Funcion para obtener la columna dada la posicion
def columna(posicion):
    if posicion == 0: return 0
    if posicion < 3: return (posicion-1) % 2
    if posicion < 6: return (posicion-3) % 3
    if posicion < 10: return (posicion-6) % 4
    return (posicion-10) % 5

def posicion(r, c):
    if c > r: return -1
    return int(r*(r + 1)/2 + c)

def es_solucion(entrada):
    print('Faltan ', entrada.count(True))
    return entrada.count(True) < 4

def crearCandidatos(a, entrada):
    final, medio = [], []
    p = a[-1] #Posicion del ultimo moviento
    i, j = renglon(p), columna(p)
    # print('Posicion: ',p)
    # imprime(entrada)
    if j - 2 >= 0: # mov 5
        m, f = posicion(i, j-1), posicion(i, j-2)
        if entrada[m] and entrada[f]:
            if f >= 0:
                final.append(f)
                medio.append(m)
            #*********************************************
    if i - 2 >= 0 and j - 2 >= 0: #mov 3
        m, f = posicion(i-1, j-1), posicion(i-2, j-2)
        if entrada[m] and entrada[f]:
            if f >= 0:
                final.append(f)
                medio.append(m)
            #*********************************************
    if i - 2 >= 0: #mov 2
        m, f = posicion(i-1, j), posicion(i-2, j)
        if entrada[m] and entrada[f]:
            if f >= 0:
                final.append(f)
                medio.append(m)
            # *********************************************
    if j + 2 <= 4: #mov 6
        m, f = posicion(i, j+1), posicion(i, j+2)
        if entrada[m] and entrada[f]:
            if f >= 0:
                final.append(f)
                medio.append(m)
            #*********************************************
    if i + 2 <= 4 and j + 2 <= 4: #mov 4
        m, f = posicion(i+1, j+1), posicion(i+2, j+2)
        if entrada[m] and entrada[f]:
            if f >= 0:
                final.append(f)
                medio.append(m)
            #*********************************************
    if i + 2 <= 4: #mov 1 
        m, f = posicion(i+1, j), posicion(i+2, j)
        if entrada[m] and entrada[f]: 
            if f >= 0:
                final.append(f)
                medio.append(m)
    # print(final, '8========D', medio)
    # print('-----------------------------------')
    # input()
    return final, medio

def backtrack(a, k, entrada):
    if es_solucion(entrada):
        global soluciones
        soluciones += 1
        print(a)
    else:
        final, medio = crearCandidatos(a, entrada)
        k += 1
        for i, f in enumerate(final):
            new_input = list(entrada)
            new_input[a[-1]] = True
            new_input[f] = False
            new_input[medio[i]] = False
            a.append(f)
            backtrack(a, k, new_input)
            a.pop()

def comesolo():
    n = int(input("Ingresa la posicion del 0 al 14: "))
    tablero = [True for i in range(15)] #Aqui acomodamos las posiciones del tablero de arriba hacia abajo
    tablero[n] = False
    backtrack([n], 0, tablero)
    global soluciones
    print(soluciones)

comesolo()