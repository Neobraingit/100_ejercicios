'''Escribir una función que tome como parámetro una frase y que filtre las palabras que son menores que el valor mínimo.
Luego devolver la frase sin las palabras filtradas'''

def filtrar_palabras(frase, longitud_minima):
    palabras = frase.split()  # Dividir la frase en palabras
    palabras_filtradas = [palabra for palabra in palabras if len(palabra) >= longitud_minima]
    frase_filtrada = ' '.join(palabras_filtradas)  # Unir las palabras filtradas en una nueva frase
    return frase_filtrada

frase_original = "Esta es una frase de ejemplo para filtrar palabras según su longitud."
longitud_minima = 3
frase_filtrada = filtrar_palabras(frase_original, longitud_minima)
print(frase_filtrada)



