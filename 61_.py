'''Escribir una función que tome como parámetro la ruta completa de un fichero y devuelva su contenido'''

def lectura_fichero(ruta):
    fichero = open('fichero.txt')
    print (fichero.read())
    
lectura_fichero('fichero.txt')