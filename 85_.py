'''Escribir una función que tenga como parámetro una lista y un elemento. Buscar ese elemento en la lista'''

def buscar(lista, elemento):
    # Recorremos la lista
    for i in lista:
        # Buscamos el elemento en la lista
        if elemento in lista:
         print (elemento)
            
lista = [1, 2, 3, 4, 5]
buscar(lista, 2)