'''Escribir una función que demuestre si un número es palíndromo'''

def es_palindromo(numero):
    numero = str(numero)
    return numero == numero[::-1]

# Ejemplo de uso
numero1 = 12321
numero2 = 12345

print(es_palindromo(numero1))  # Devuelve True
print(es_palindromo(numero2))  # Devuelve False
