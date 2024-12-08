
import argparse
from termcolor import colored

parser = argparse.ArgumentParser(description='Tabla de multiplicar')
parser.add_argument('-n', '--numero', type=int, required=True,help='Dime un número')

args = parser.parse_args()

for i in range (10, 0, -1):
   resultado =  i * args.numero
   print (colored(f'{args.numero} x {i} = {resultado}', 'yellow'))