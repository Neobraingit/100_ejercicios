'''Crear una función que tenga como parámetro una lista y un elemento.
 Mostrar en que índice está dicho elemento'''
 
def encontrar_indice(lista, elemento):
    if elemento in lista:
        indice = lista.index(elemento)
        print(f"El elemento '{elemento}' se encuentra en el índice {indice} de la lista.")
    else:
        print(f"El elemento '{elemento}' no está presente en la lista.")

# Ejemplo de uso
mi_lista = [10, 20, 30, 40, 50]
elemento_buscado = 30
encontrar_indice(mi_lista, elemento_buscado)



     