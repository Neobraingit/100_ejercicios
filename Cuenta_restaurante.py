from termcolor import colored

monto_cuenta = float(input('Dime cuanto te debo: '))

número_comensales = float(input('Dime el número de comensales: '))

popina = 15

tocante = (monto_cuenta * 15) / número_comensales

print (colored(f'Tocamos a {tocante} € cada uno.', 'yellow'))