
import time
from termcolor import colored

Lista = ['Rojo', 'Ambar', 'Verde']

print ('Dime qué color ves en el semáforo: ')

color = input()
while True:
    if color == 'Rojo':
        print (colored('Detente unos segundos...','red'))
        time.sleep (5)
        break
    elif color == 'Ambar':
        print (colored('Acelera¡¡¡', 'yellow'))
        break
    elif color == 'Verde':
        print (colored('Continua', 'green'))
        break
        
    
