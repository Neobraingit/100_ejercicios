'''Encuentra el Número Oculto
Crea un programa donde el usuario tenga que encontrar un número oculto.
Requisitos:

Genera un número aleatorio entre 1 y 20.
Pide al usuario que adivine el número.
Indica si su intento es "muy bajo" o "muy alto" hasta que lo acierte.
Lleva un conteo de los intentos y muéstralo al final.'''
import random

numero_oculto = random.randint(1, 100)

while True:
    numero = int(input('Dime el número secreto: '))
    if numero == numero_oculto:
        print ('Has ganado ')
        break
    elif numero < numero_oculto:
        print ('Más alto..')
    elif numero > numero_oculto:
        print ('Más bajo...')
    else:
        print ('[!] Numero incorrecto')
