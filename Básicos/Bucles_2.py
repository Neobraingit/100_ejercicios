

# Tabla de multiplicar

from termcolor import colored

numero_a_multiplicar = int(input('Introduce el número: '))

for i in range(1, 11):
        resultado = numero_a_multiplicar * i
        print (f'{numero_a_multiplicar} x {i} = {resultado}')