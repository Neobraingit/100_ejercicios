''' Escribe una funcion que tenga como parámetro un número entero y muestre todos los divisores de ese número'''

def mostrar_divisores(numero):
    print(f"Divisores de {numero}:")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)

mostrar_divisores(12)