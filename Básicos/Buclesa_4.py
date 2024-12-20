
from termcolor import colored
import random

numero = random.randint(0, 101)

while True:
    opcion = int(input('Introduce el número: '))

    if opcion > numero:
        print (colored('Más bajo', 'red'))
    elif opcion < numero:
        print (colored('Más alto', 'yellow'))
    elif opcion == numero:
        print (colored('Has ganado¡¡¡', 'light_blue'))
        break
    
    