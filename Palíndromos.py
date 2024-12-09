
import argparse
from termcolor import colored

parser =argparse.ArgumentParser(description='Programa para ver si dos palabras son palíndromos')
parser.add_argument('-p1', '--palabra1', type=str, required=True, help='Dime la primera palabra')
parser.add_argument('-p2', '--palabra2', type=str, required=True, help='Dime la segunda palabra')

args = parser.parse_args()

def comprobar_palíndromos():
    if sorted(args.palabra1) == sorted(args.palabra2):
        print ('Son Palíndromos..')
    else:
        print ('No son palíndromos...')
        
comprobar_palíndromos()