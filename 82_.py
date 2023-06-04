'''Escribir una función que demuestre si un número entero es un circular primo'''

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def es_circular_primo(numero):
    str_numero = str(numero)
    for _ in range(len(str_numero)):
        if not es_primo(int(str_numero)):
            return False
        str_numero = str_numero[1:] + str_numero[0]
    return True

# Ejemplo de uso
numero1 = 197
numero2 = 23
numero3 = 37

print(es_circular_primo(numero1))  # Devuelve True
print(es_circular_primo(numero2))  # Devuelve True
print(es_circular_primo(numero3))  # Devuelve False
