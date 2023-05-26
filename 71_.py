'''Escribir una función que tenga como parámetro un número x y devuelva
trigonométrica'''

import math

def calcular_trigonometrica(x):
    # Convertir el ángulo a radianes
    radianes = math.radians(x)

    # Calcular el valor de las funciones trigonométricas
    seno = math.sin(radianes)
    coseno = math.cos(radianes)
    tangente = math.tan(radianes)

    # Devolver el resultado como una tupla
    return seno, coseno, tangente


angulo = 45
resultado = calcular_trigonometrica(angulo)
print(f"Seno: {resultado[0]}")
print(f"Coseno: {resultado[1]}")
print(f"Tangente: {resultado[2]}")


