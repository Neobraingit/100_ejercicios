
def dibujar_piramide(n):
    for i in range(1, n + 1):
        # Espacios a la izquierda para centrar los *
        espacios = ' ' * (n - i)
        # Caracteres * de la pirámide
        estrellas = '*' * (2 * i - 1)
        # Imprimir una fila de la pirámide
        print(espacios + estrellas)

# Solicitar un número entero al usuario
try:
    numero = int(input("Introduce un número entero para la altura de la pirámide: "))
    if numero > 0:
        dibujar_piramide(numero)
    else:
        print("El número debe ser mayor que 0.")
except ValueError:
    print("Entrada inválida. Debes introducir un número entero.")
