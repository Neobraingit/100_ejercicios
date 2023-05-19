''' Solicita al usuario su edad y almacénalo en una variable. Hay que verificar si es mayor o menor  de edad.
Si el usuario es mayor o igual que 18 imprimir "Eres mayor de edad" si no, "Eres menor de edad'''

edad = int(input('Dime tu edad: '))
if edad >= 18:
    print ('Eres mayor de edad¡¡')
elif edad < 18:
    print ('Eres menor de edad¡¡')