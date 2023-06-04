# Escribir el número más grande obtenido palindrómico

def obtener_mayor_palindromo():
    mayor_palindromo = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            producto = i * j
            if str(producto) == str(producto)[::-1] and producto > mayor_palindromo:
                mayor_palindromo = producto
    return mayor_palindromo

# Ejemplo de uso
numero_palindromo = obtener_mayor_palindromo()
print(numero_palindromo)
