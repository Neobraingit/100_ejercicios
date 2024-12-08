import argparse
from termcolor import colored

parser = argparse.ArgumentParser(description='Programa que muestra los n numeros primos')
parser.add_argument('-n', '--numero', type=int, required=True, help='Dime un número')

args = parser.parse_args ()

def numeros_primos():
    for i in range(0, args.numero):
        if i % 2 == 0:
            print (colored(f'[+] {i} es un número par', 'green'))
        else:
            print (colored(f'[!] {i} No es par', 'yellow'))
            
numeros_primos()