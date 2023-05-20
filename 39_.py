'''Crea un función que tenga como parámetros clave, valor, diccionario y permita introducir esa clave y valor al diccionario.
Luego mostrar ese diccionario'''

def agregar_elemento(clave, valor, diccionario):
    diccionario[clave] = valor
    return diccionario

# Ejemplo de uso
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print("Diccionario original:", mi_diccionario)

clave = input("Ingrese la clave: ")
valor = input("Ingrese el valor: ")

mi_diccionario = agregar_elemento(clave, valor, mi_diccionario)
print("Diccionario actualizado:", mi_diccionario)
