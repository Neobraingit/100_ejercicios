'''Crear una lista con los valores 1,2,3,4,5,6,7,8,9,0 y después crear otra lista que contenga
un elemento de cada tres de la lista anterior. En este caso debemo obtener: 1, 4, 7, 0'''

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lista_cada_tres = lista_original[0::3]  # Obtiene elementos de cada tres posiciones, comenzando desde la posición 0

print(lista_cada_tres)
