'''Escribir una función que tome como argumento la ruta de un fichero y un caracter
La función debe borrar del fichero el caracter'''

def borrar_caracter_en_archivo(ruta_archivo, caracter):
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    with open(ruta_archivo, 'w') as archivo:
        for linea in lineas:
            nueva_linea = linea.replace(caracter, '')
            archivo.write(nueva_linea)

ruta = 'fichero.txt'
caracter_a_borrar = 'a'

borrar_caracter_en_archivo(ruta, caracter_a_borrar)
