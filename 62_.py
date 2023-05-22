'''Escribir una función que tome como argumento la ruta de un fichero y una palabra.
La función debe mostrar cuantas veces aparece la palabra en el fichero'''

def ocurrencias(ruta, palabra):
    archivo = open('fichero.txt','r')
    lectura = archivo.read()
    contador = lectura.lower().count(palabra.lower())
    for palabra in archivo:
         contador += 1
    print (f'La palabra {palabra} aparece {contador} veces en el fichero')
    

ocurrencias('fichero.txt', 'Esto')