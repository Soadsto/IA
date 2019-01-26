import primos as reader
prims = None
kg = 0
soluciones = []

def es_solucion(a, k, n):
    #Cantidad de sumandos deseados por el usuario, K es la cantidad de sumandos de la solucion
    global kg 
    return sum(a) == n and k == kg #si la suma es igual a n y los sumandos son los deseados


def show_solution(a):
    global soluciones
    a.sort()
    a = list(a)
    if a in soluciones: 
        return
    print(a)    
    soluciones.append(a)

def crear_candidatos(a, n, cand):
    global prims
    posibilidades = prims
    suma = sum(a)
    for elem in posibilidades:
        if not elem in a:
            cand.append(elem)
            
def backtrack(a, k, n):
    if es_solucion(a, k, n):
        show_solution(a)
    else:
        cand = [] #aqui se guardan los candidatos
        crear_candidatos(a, n, cand)
        k = k + 1
        for c in cand:
            a.append(c)
            if sum(a) <= n:
                backtrack(a, k, n)
            a.pop()

def main():
    global prims, kg, soluciones
    num = reader.leer() #EL N que vamos a ocupar
    kg = reader.leerK() #La cantidad de sumandos a usar
    prims = reader.primos(num) #Los primos dentro del rango de 2 a N
    prims.reverse()
    backtrack([], 0, num)

    print("Hay un total de " + str(len(soluciones)) + " soluciones.")

main()