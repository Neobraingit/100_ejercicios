# Secuencia de Fibonacci

def fibonacci(n):
    sequence = [0, 1]  # Inicializamos la secuencia con los primeros dos números (0 y 1)

    # Generamos los siguientes números de la secuencia hasta el número n
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]  # Sumamos los dos últimos números de la secuencia
        sequence.append(next_number)  # Agregamos el siguiente número a la secuencia

    return sequence

# Ejemplo de uso
n = 10  # Número de elementos de la secuencia que deseamos generar
result = fibonacci(n)
print(result)
