'''Escribir una función presenciaVocal que tome como parámetro una frase y verifique si tiene una vocal o no.
Devolverá True si hay vocal y False si no la hay'''

def presenciaVocal(frase):
    vocales = ['a', 'e', 'i', 'o', 'u']
    for letra in frase:
        if letra in vocales:
            return True
    return False
    
    
frase1 = 'Mmmmmmmmmmmmmmm'
frase2 = 'Me llamo Carmona'
print (presenciaVocal(frase2))