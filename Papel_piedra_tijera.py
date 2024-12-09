
import random

opciones = ['Papel', 'Tijera', 'Piedra']

while True:
    tirada_jugador_1 = random.choice(opciones)
    print (tirada_jugador_1)
    tirada_jugador_2 = random.choice(opciones)
    print (tirada_jugador_2)
    
    if tirada_jugador_1 == 'Piedra' and tirada_jugador_2 == 'Papel':
        print ('Jugador 1 ha ganado¡')
    elif tirada_jugador_1 == 'Tijera'and tirada_jugador_2 == 'Papel':
        print ('Jugador 1 ha ganado¡¡')
    else:
        print ('Jugador 2 ha ganado ¡¡')
        break
        