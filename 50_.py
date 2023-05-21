''' Escribe una función que concatene dos diccionarios'''
def concatenar_diccionarios(dic1, dic2):
    dic_concatenado = dict(dic1)
    dic_concatenado.update(dic2)
    return dic_concatenado



diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'c': 3, 'd': 4}
diccionario_concatenado = concatenar_diccionarios(diccionario1, diccionario2)
print(diccionario_concatenado)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
