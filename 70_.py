'''Escribir una función que pase como parámetro una lista de caracteres y una longitud de contraseña
y genere una contraseña aleatoria que contenga esos caracteres y la longitud de la contraseaña'''
import random

def generar_contrasena(caracteres, longitud):
    contrasena = ""
    for _ in range(longitud):
        contrasena += random.choice(caracteres)
    return contrasena

caracteres_permitidos = ['a', 'b', 'c', '1', '2', '3', '@', '#', '$']
longitud_contrasena = 8

contrasena_generada = generar_contrasena(caracteres_permitidos, longitud_contrasena)
print(contrasena_generada)
