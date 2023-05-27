'''Escribir una función que permita reemplazar en una cadena de caracteres la palabra introducida en el 
segundo parámetro '''


def reemplazar_palabra(cadena, palabra_original, palabra_nueva):
        nueva_cadena = cadena.replace(palabra_original, palabra_nueva)
        return nueva_cadena

# Ejemplo de uso
cadena_original = "El perro corre en el parque"
palabra_original = "perro"
palabra_nueva = "gato"
cadena_resultante = reemplazar_palabra(cadena_original, palabra_original, palabra_nueva)
print(cadena_resultante)

    