
import time

Lista = ['Rojo', 'Ambar', 'Verde']

print ('Dime qué color ves en el semáforo: ')

color = input()
while True:
    if color == 'Rojo':
        print ('Detente unos segundos...')
        time.sleep (5)
        break
    elif color == 'Ambar':
        print ('Acelera¡¡¡')
        break
    elif color == 'Verde':
        print ('Continua')
        break
        
    
