def permute(a, l, r):
    #A es una lista. 
    #l es 0. Siempre
    #r la longitud de la lista en menos 1 
    if l == r:
        print (a)
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l] #Backtrack

#Driver program to test the above function
cad = "123"
n = len(cad) #Numero de permutaciones
a = list(cad) #List 
permute(a, 0, n-1)