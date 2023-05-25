'''Escribir una función que tenga como parámetro un diccionario y devuelva la clave que tenga mayor número de valor'''

def clave_con_maximo_valor(diccionario):
    max_valor = None
    max_clave = None
    
    for clave, valor in diccionario.items():
        if max_valor is None or valor > max_valor:
            max_valor = valor
            max_clave = clave
    
    return max_clave
