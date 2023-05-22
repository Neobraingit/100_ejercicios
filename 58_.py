'''Escribe una función que tenga como parámetros una lista y devuelva y devuelva una lista de tuplas
donde cada tupla corresponda con el número de apariciones de la tupla'''

def contar_apariciones(lista):
    contador = {}
    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    
    resultado = []
    for elemento, apariciones in contador.items():
        resultado.append((elemento, apariciones))
    
    return resultado


mi_lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
resultado = contar_apariciones(mi_lista)
print(resultado)

