

frase = input('Dime una frase para contar sus palabras: ')
contador = 0

for i in frase.split():
    contador += 1
print (f'La frase tiene {contador} palabras.')
    