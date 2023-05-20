'''Crear una función que sume todos los valores de una lista'''

def suma_lista(lista):
    for i in lista:
     print ('La suma de la lista es de: ',sum(lista))
     break
        
suma_lista([2, 4, 6])