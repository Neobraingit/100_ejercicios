'''Escribimos una función que tenga como parámetro un fichero y un texto y
nos devuelva ese texto escrito en el fichero'''

def escribir(fichero, texto):
    with open('fichero.txt', 'w') as f:
        f.write('Hello world')
        
escribir('fichero.txt', 'Hola mundo')
        
