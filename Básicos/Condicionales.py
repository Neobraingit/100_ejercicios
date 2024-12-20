
from termcolor import colored
'''Par e impar'''

numero = int(input('Introduce el número: '))

if numero % 2 == 0:
    print (colored('Es número par', 'red'))
else:
    print (colored('Es número impar', 'green'))