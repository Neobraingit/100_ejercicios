# Escribir una programa que permita mezclar los items de una lista
import random

def mezclar_lista(lista):
    random.shuffle(lista)
    return lista

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5]
lista_mezclada = mezclar_lista(mi_lista)
print(lista_mezclada)


