
from termcolor import colored

# Comparar tres números

numero_1 = int(input('Introduce el primer número: '))
numero_2 = int(input('introduce el segundo número: '))
numero_3 = int(input('Introduce el tercer número: '))

if numero_1 >= numero_2 and numero_1 >= numero_3:
    print (colored('Es mayor que los otros dos', 'red'))
elif numero_2 > numero_1 and numero_1 > numero_3:
    print (colored('Es mayor el número dos', 'yellow'))
elif numero_3 > numero_1 and numero_3 > numero_2:
    print (colored('El número tres es el mayor', 'blue'))