'''Escribir una función llamada eliminarEsp que tome una frase como parámetro y la devuelva sin espacios'''

def eliminarEsp(frase):
    resultado = frase.replace(' ', ' ')
    return resultado

frase = "Hola, ¿cómo estás?"
frase_sin_espacios = eliminarEsp(frase)
print(frase_sin_espacios)

    
    