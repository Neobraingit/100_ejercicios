
import argparse

parser = argparse.ArgumentParser(description='Contador de vocales')
parser.add_argument('-f', '--frase', type=str, required=True,help='Dime una frase')

args = parser.parse_args()

vocales = 'aeiou'

def contar_vocales():
    contador = 0
    for i in args.frase:
        if i in vocales:
            contador += 1
    print (f'La frase tiene {contador} vocales')

contar_vocales()