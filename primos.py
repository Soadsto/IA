def primo(num):
    if num < 2:     #si es menos que 2 no es primo
        return False
    for i in range(2, num):  #un rango desde el dos hasta el numero que nosotros elijamos
        if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
            return False
    return True    #Es primo

def primos(num):
    nums = []
    for i in range(num):
        if primo(i):
            nums.append(i)
    return nums

#Donde pedimos y guardamos N
def leer():
    while True:
        try:
            num = int(input("Dame N: ")) #Pedimos N.
            if num <= 0:
                raise ValueError
            break
        except:
            print("Dato invalido")
    return num

def leerK():
    while True:
        try:
            k = int(input("Dame K: ")) #Pedimos K
            if k <= 0:
                raise ValueError
            break
        except:
            print("Dato invalido")
    return k