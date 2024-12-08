

import re

# Texto proporcionado
texto = input('Dime una frase: ')

texto_sin_puntuacion = texto.lower()

# Separar en palabras
palabras = texto_sin_puntuacion.split()

# Contar palabras únicas
palabras_unicas = set(palabras)
numero_palabras_unicas = len(palabras_unicas)

print (numero_palabras_unicas)




