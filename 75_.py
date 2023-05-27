'''Un número n es par si n1 es impar, y viceversa
escribir dos funciones recursivas'''

def es_par(n):
    if n < 10:
        return (n % 10) % 2 == 1
    return es_impar(n // 10)

def es_impar(n):
    if n < 10:
        return (n % 10) % 2 == 0
    return es_par(n // 10)
