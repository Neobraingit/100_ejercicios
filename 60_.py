'''Escribir una función que tome como parámetros dos enteros y calcule el máximo común divisor 
utilizando el algoritmo de Euclides'''

def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

mcd = calcular_mcd(24, 36)
print(mcd)  # Salida: 12
