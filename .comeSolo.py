#Sergio Téllez Ojeda 
#Inteligencia Artifial
soluciones = 0
finales = [0 for i in range(15)] #Aqui contamos donde termina cada solucion

def nuevo(aux):
    nueva = []
    for i in range(len(aux)):
        nueva.append(aux[i])
    return nueva

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

def contar(tablero):
    global finales
    for i in range(len(tablero)):
        if tablero[i] == True:
            finales[i] += 1
            return

def movimiento(tablero, i):
    global soluciones
    r, c = renglon(i), columna(i)                        
    if c-2 >= 0: #Hacia la izquierda
        if tablero[posicion(r, c-1)] and tablero[posicion(r, c-2)]: #Si la casilla inmediata esta ocupada, verifica la siguiente
            tablero[i], tablero[posicion(r, c-1)], tablero[posicion(r, c-2)] = True, False, False            
            if tablero.count(True) == 1:
                soluciones += 1
                contar(tablero)
            else:
                for i in range(len(tablero)):
                    if not tablero[i]:
                        movimiento(nuevo(tablero), i)
            tablero[i], tablero[posicion(r, c-1)], tablero[posicion(r, c-2)] = False, True, True            
    if r-2 >= 0 and c-2 >= 0: #Diagonal hacia arriba y a la izquierda
        if tablero[posicion(r-1, c-1)] and  tablero[posicion(r-2, c-2)]: #Si la casilla inmediata esta ocupada, verifica la siguiente
            tablero[i], tablero[posicion(r-1, c-1)], tablero[posicion(r-2, c-2)] = True, False, False
            if mov == 13:
                soluciones += 1
                contar(tablero)
            else:
                for i in range(len(tablero)):
                    if not tablero[i]:
                        movimiento(nuevo(tablero), i, mov+1)
            tablero[i], tablero[posicion(r-1, c-1)], tablero[posicion(r-2, c-2)] = False, True, True
    if r-2 >= 0: #Diagonal hacia arriba y a la derecha
        if tablero[posicion(r-1, c)] and tablero[posicion(r-2, c)]: #Si la casilla inmediata esta ocupada, verifica
            tablero[i], tablero[posicion(r-1, c)], tablero[posicion(r-2, c)] = True, False, False
            if mov == 13:
                soluciones += 1
                contar(tablero)
            else:
                for i in range(len(tablero)):
                    if not tablero[i]:
                        movimiento(nuevo(tablero), i, mov+1)
            tablero[i], tablero[posicion(r-1, c)], tablero[posicion(r-2, c)] = False, True, True
    if c+2 <= 4: #Hacia la derecha
        if tablero[posicion(r, c+1)] and tablero[posicion(r, c+2)]: #Si la casilla inmediata esta ocupada, verifica la siguiente                
            tablero[i], tablero[posicion(r, c+1)], tablero[posicion(r, c+2)] = True, False, False
            if mov == 13:
                soluciones += 1
                contar(tablero)
            else:
                for i in range(len(tablero)):
                    if not tablero[i]:
                        movimiento(nuevo(tablero), i, mov+1)
            tablero[i], tablero[posicion(r, c+1)], tablero[posicion(r, c+2)] = False, True, True
    if r+2 <= 4 and c+2 <= 4: #Diagonal hacia abajo y a la derecha
        if tablero[posicion(r+1, c+1)] and tablero[posicion(r+2, c+2)]: #Si la casilla inmediata esta ocupada, verifica la siguiente
            tablero[i], tablero[posicion(r+1, c+1)], tablero[posicion(r+2, c+2)] = True, False, False
            if mov == 13:
                soluciones += 1
                contar(tablero)
            else:
                for i in range(len(tablero)):
                    if not tablero[i]:
                        movimiento(nuevo(tablero), i, mov+1)
            tablero[i], tablero[posicion(r+1, c+1)], tablero[posicion(r+2, c+2)] = False, True, True
    if r+1 <= 4 and r+2 <= 4: #Diagonal hacia abajo y a la izquierda
        if tablero[posicion(r+1, c)] and tablero[posicion(r+2, c)]: #Si la casilla inmediata esta ocupada, verifica la siguiente
            tablero[i], tablero[posicion(r+1, c)], tablero[posicion(r+2, c)] = True, False, False        
            if mov == 13:
                soluciones += 1
                contar(tablero)
            else:
                for i in range(len(tablero)):
                    if not tablero[i]: #Si encuentra una posicion vacia, llamas recursivamente al metodo
                        movimiento(nuevo(tablero), i, mov+1)
            tablero[i], tablero[posicion(r+1, c)], tablero[posicion(r+2, c)] = False, True, True

def leer():
    while True:
        try:
            size = int(input("Del 0 al 14 ¿Cuál casilla está vacia? "))
            if size < 0 or size > 14:
                print("No existe dicha posicion")
                continue
            return size
        except ValueError:
            print("Dato invalido. Escribe de nuevo")

def comeSolo():
    global soluciones, finales
    n =  leer()
    tablero = [True for i in range(15)] #Aqui acomodamos las posiciones del tablero de arriba hacia abajo
    tablero[n] = False
    movimiento(nuevo(tablero), n)
    print("Soluciones: ", soluciones)   
    for i in range(len(finales)):
        print("Posicion[",renglon(i),",", columna(i),"] = ", finales[i])

comeSolo()