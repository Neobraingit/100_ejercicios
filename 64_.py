'''Escribir una función que tome como parámetro la ruta de un archivo y verifica si el archivo tiene un número.
Devolverá True si lo tiene y False si no'''

import re
def numero (ruta):
     with open('fichero.txt', 'r') as archivo:
            contenido = archivo.read()
            resultado = re.search(r'\d', contenido)
            if resultado:
                return True
            else:
                return False
            
            
print (numero ('fichero.txt'))