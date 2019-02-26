"""
    Salida de un rectangulo de 4*4 = 36
    La entrada debera ser las dimensiones del rectangulo, ya sea renglon * columna
    La salida de manera general son la cantidad de configuraciones con recangulos de 2*1 | 1*2 dentro de un rectangulo
    definido por el usuario
"""
#Sergio Téllez Ojeda
#Inteligencia artificial 
soluciones = 0
def esSolucion():
    global soluciones
    soluciones += 1

def movimiento(numMov):
    if numMov > m*n/2:
        esSolucion()
    else:
        r = 0
        c = 0
        while r < m and a[r][c] != 0:
            c += 1
            if c == n:
                c = 0
                r += 1
        if r < m:
            if c + 1 < n and a[r][c + 1] == 0:
                a[r][c], a[r][c + 1] = numMov, numMov
                movimiento(numMov + 1)
                a[r][c], a[r][c + 1] = 0, 0
            if r + 1 < m and a[r + 1][c] == 0:
                a[r][c], a[r + 1][c] = numMov, numMov
                movimiento(numMov + 1)
                a[r][c], a[r + 1][c] = 0, 0
                
m = int(input("Renglones: "))
n = int(input("Columnas: "))

soluciones = 0
a = [[0 for i in range(n)] for i in range(m)]
movimiento(1)

print("Soluciones:", soluciones)