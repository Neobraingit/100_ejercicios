'''Crea una función que elimine los duplicados de una lista y la devuelva en otra ordenada ascendentemente'''

def dupli(lista):
    result = []
    for i in lista:
        if i not in result:
            result.append(i)
    print (result)
    
dupli([2, 2, 2, 3, 4, 5])