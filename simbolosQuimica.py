simbolos = [
            "Ac", "Al", "Am", "Sb", "Ar", "As", "At", "Ba", 
            "Bk", "Be", "Bi", "Bh", "B", "Br", "Cd", "Ca",
            "Cf", "C", "Ce", "Cs", "Cl", "Cr", "Co", "Cu",
            "Cm", "Ds", "Db", "Dy", "Es", "Er", "Eu", "Fm", 
            "F", "Fr", "Gd", "Ga", "Ge", "Au", "Hf", "Hs", 
            "He", "Ho", "H", "In", "I", "Ir", "Fe", "Kr",
            "La", "Lr", "Pb", "Li", "Lu", "Mg", "Mn", "Mt",
            "Md", "Hg", "Mo", "Nd", "Ne", "Np", "Ni", "Nb",
            "N", "No", "Os", "O", "Pd", "P", "Pt", "Pu", "Po",
            "K", "Pr", "Pm", "Pa", "Ra", "Rn", "Re", "Rh", "Rg",
            "Rb", "Ru", "Rf", "Sm", "Sc", "Sg", "Se", "Si",
            "Ag", "Na", "Sr", "S", "Ta", "Tc", "Te", "Tb", "Tl",
            "Th", "Tm", "Sn", "Ti", "W", "U", "V", "Xe", "Y", "Zn"
        ]   
soluciones = 0

def esSolucion(cadena):
    return len(cadena) == 0

def showSolucion(a):
    global soluciones
    for elem in a:
        print(elem.capitalize(), end = ' ')
    print()
    soluciones = soluciones + 1

def crearCandidatos(cadena, cand):
    global simbolos
    posibilidades = simbolos
    for elem in posibilidades:
        if cadena.find(elem) == 0:
            cand.append(elem)
    
def bactrack(a, cadena):
    if esSolucion(cadena):
        showSolucion(a)
    else:
        cand = []
        crearCandidatos(cadena, cand)
        for c in cand:
            a.append(c)
            i = cadena.find(c)
            bactrack(a, cadena[:i] + cadena[i + len(c):])
            a.pop()

def main():
    global soluciones
    for i, elem in enumerate(simbolos):
        simbolos[i] = elem.casefold()
        
    # print(simbolos)
    cadena =  input("Ingresa una cadena: ")
    bactrack([], cadena)
    print("Hay un total de ", soluciones, " soluciones.")
    
main()