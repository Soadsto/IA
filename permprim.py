import primos as reader
prims = None
kg = 0
soluciones = []

def es_solucion(a, k, n):
    #Cantidad de sumandos deseados por el usuario, K es la cantidad de sumandos de la solucion
    global kg 
    return 0 == n and k == kg #si la suma es igual a n y los sumandos son los deseados


def show_solution(a):
    global soluciones
    #print("PROCESANDO a:", a)
    x = list(a)
    x.sort()
    #print("x = ", x)
    if x in soluciones: 
        return
    print("Found it: ",x)    
    soluciones.append(x)

def crear_candidatos(a, n, cand):
    global prims
    posibilidades = prims
    for elem in posibilidades:
        if n - elem >= 0:
            cand.append(elem)
    #print("Candidatos: ", cand)
    #input()
            
def backtrack(a, k, n):
    #print("n:", n)
    if es_solucion(a, k, n):
        show_solution(a)
    else:
        cand = [] #aqui se guardan los candidatos
        crear_candidatos(a, n, cand)
        k = k + 1
        for c in cand:
            a.append(c)
            if k <= kg:
                backtrack(a, k, n-c)
            a.pop()

def main():
    global prims, kg, soluciones
    num = reader.leer() #EL N que vamos a ocupar
    kg = reader.leerK() #La cantidad de sumandos a usar
    prims = reader.primos(num) #Los primos dentro del rango de 2 a N
    print(prims)
    prims.reverse()
    backtrack([], 0, num)

    print("Hay un total de " + str(len(soluciones)) + " soluciones.")

main()