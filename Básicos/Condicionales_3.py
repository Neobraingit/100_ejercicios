
from termcolor import colored

# Averiguar si estás aprobado (60+)

nota = float(input('Introduce la nota: '))

if nota >= 60:
    print (colored('Estás aprobad@', 'red'))
else:
    print (colored('No has aprobad@', 'blue'))