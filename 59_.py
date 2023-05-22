'''Escribir una función que tome como parámetro tres listas de números enterosy devuelva
una lista en orden ascendente que sea la union de las tres listas sin duplicados'''

def fusion(lista1, lista2, lista3):
    resultado = lista1 + lista2 + lista3 # Unión de las tres listas
    sin_duplicados = list(set(resultado))
    ordenada = resultado.sort()
    print (sin_duplicados)
    
fusion([12, 2, 3], [2, 5, 6], [3, 8, 9])
           
    
    