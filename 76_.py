'''Escribir una cadena que permita transformar una lista en una cadena de caracteres
separados por el caracter pasado como parámetro'''

def lista_a_cadena(lista, separador):
    cadena = separador.join(map(str, lista))
    return cadena

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5]
caracter_separador = "-"
cadena_resultante = lista_a_cadena(mi_lista, caracter_separador)
print(cadena_resultante)
