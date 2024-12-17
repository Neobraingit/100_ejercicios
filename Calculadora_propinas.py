'''Crea un programa que calcule cuánto debería dejar cada persona de propina en un restaurante.
Requisitos:

Pregunta al usuario por el total de la cuenta.
Pregunta cuántas personas van a dividir la cuenta.
Pregunta qué porcentaje de propina desean dejar (por ejemplo, 10%, 15%, 20%).
Devuelve cuánto debe pagar cada persona, incluyendo su parte proporcional de la propina.'''


total_cuenta = float(input('¿Cuánto es el total de la cuenta? '))
total_personas = int(input('¿Cuántas personas somos a repartir? '))
porcentaje_propina = float(input('¿Cuál es el porcentaje de la propina a dejar? '))

def calculadora_propinas():
    resultado = (total_cuenta / total_personas) 
    propina = resultado % porcentaje_propina
    
    print (f'Tenemos que pagar cada uno: {propina + resultado} €.')


calculadora_propinas()
