
import random
from termcolor import colored

numero = random.randint(1, 100)

while True:
    opción = int(input('Dime el número: '))
    if opción == numero:
        print (colored('¡Has ganado!', 'red'))
    elif opción > numero:
        print ('Más bajo...')
    elif opción < numero:
        print ('Mas alto...')
    else: 
        print ('Número inválido')