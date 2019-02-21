s = 0
soluciones = [[0],[0,0],[0,0,0],[0,0,0,0],[0,0,0,0,0]]
def nuevo(mat):
    nueva = []
    for i in range(len(mat)):
        nueva.append(mat[i][:])
    return nueva

def buscar(matriz):
    global soluciones
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                soluciones[i][j] += 1
                break

def funcion(matriz, punto):
    x = punto[0]
    y = punto[1]
    aux = nuevo(matriz)
    global s 
    if x-2 >= 0 and y-2 >= 0:
        if matriz[x-2][y-2] == 1 and matriz[x-1][y-1] == 1:
            matriz[x][y] = 1
            matriz[x-1][y-1] = 0
            matriz[x-2][y-2] = 0
            suma = 0
            for i in range(len(matriz)):
                suma += sum(matriz[i])
            if suma == 1:
                s += 1
                buscar(matriz)
            else:
                for i in range(len(matriz)):
                    for j in range(len(matriz[i])):
                        if matriz[i][j] == 0:
                            punto[0] = i
                            punto[1] = j
                            funcion(nuevo(matriz),punto[:])
            matriz = nuevo(aux)
    if x-2 >=0 and y < len(matriz[x-2]):
        if matriz[x-2][y] == 1 and matriz[x-1][y] == 1:
            matriz[x][y] = 1
            matriz[x-1][y] = 0
            matriz[x-2][y] = 0
            suma = 0
            for i in range(len(matriz)):
                suma += sum(matriz[i])
            if suma==1:
                s += 1
                buscar(matriz)
            else:
                for i in range(len(matriz)):
                    for j in range(len(matriz[i])):
                        if(matriz[i][j] == 0):
                            punto[0] = i
                            punto[1] = j
                            funcion(nuevo(matriz),punto[:])
            matriz = nuevo(aux)
    if x+2 < len(matriz):
        if matriz[x+2][y] == 1 and matriz[x+1][y] == 1:
            matriz[x][y] = 1
            matriz[x+1][y] = 0
            matriz[x+2][y] = 0
            suma = 0
            for i in range(len(matriz)):
                suma += sum(matriz[i])
            if suma==1:
                s += 1
                buscar(matriz)
            else:
                for i in range(len(matriz)):
                    for j in range(len(matriz[i])):
                        if(matriz[i][j] == 0):
                            punto[0] = i
                            punto[1] = j
                            funcion(nuevo(matriz),punto[:])
            matriz = nuevo(aux)
    if x+2 < len(matriz) and y+2 < len(matriz[x+2]):
        if matriz[x+2][y+2] == 1 and matriz[x+1][y+1] == 1:    
            matriz[x][y] = 1
            matriz[x+1][y+1] = 0
            matriz[x+2][y+2] = 0
            suma = 0
            for i in range(len(matriz)):
                suma += sum(matriz[i])
            if suma==1:
                s += 1
                buscar(matriz)
            else:
                for i in range(len(matriz)):
                    for j in range(len(matriz[i])):
                        if(matriz[i][j] == 0):
                            punto[0] = i
                            punto[1] = j
                            funcion(nuevo(matriz),punto[:])
            matriz = nuevo(aux)
    if y-2 >= 0:
        if matriz[x][y-2] == 1 and matriz[x][y-1] == 1:  
            matriz[x][y] = 1
            matriz[x][y-1] = 0
            matriz[x][y-2] = 0
            suma = 0
            for i in range(len(matriz)):
                suma += sum(matriz[i])
            if suma==1:
                s += 1
                buscar(matriz)            
            else:
                for i in range(len(matriz)):
                    for j in range(len(matriz[i])):
                        if(matriz[i][j] == 0):
                            punto[0] = i
                            punto[1] = j
                            funcion(nuevo(matriz),punto[:])
            matriz = nuevo(aux)
    if y+2 < len(matriz[x]):
        if matriz[x][y+2] == 1 and matriz[x][y+1] == 1:    
            matriz[x][y] = 1
            matriz[x][y+1] = 0
            matriz[x][y+2] = 0
            suma = 0
            for i in range(len(matriz)):
                suma += sum(matriz[i])
            if suma==1:
                s += 1
                buscar(matriz)
            else:
                for i in range(len(matriz)):
                    for j in range(len(matriz[i])):
                        if(matriz[i][j] == 0):
                            punto[0] = i
                            punto[1] = j
                            funcion(nuevo(matriz),punto[:])
            matriz = nuevo(aux)
    
def main():
    coordenada = []
    coordenada.append(int(input("Renglon: "))-1)
    coordenada.append(int(input("Columna: "))-1)
    mat = []
    for i in range(5):
        fila = []
        for j in range(i+1):
            if i == coordenada[0] and j == coordenada[1]:
                fila.append(0)
            else:
                fila.append(1)
        mat.append(fila)    
    funcion(nuevo(mat),coordenada[:])
    global s
    global soluciones
    print("Se encontraron: "+ str(s) + " soluciones" )
    for i in range(len(soluciones)):
        for j in range(len(soluciones[i])):
            print("Posicion [" + str(i+1) + "," + str(j+1) +"] = " + str(soluciones[i][j]) )
main()