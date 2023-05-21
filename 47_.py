'''Escribir una función que compruebe si una frase tiene por lo menos una letra en mayúsculas'''

def tiene_mayusculas(frase):
    return any(letra.isupper() for letra in frase)

# Ejemplo de uso
frase_1 = "Esta es una Frase de ejemplo"
frase_2 = "esta es otra frase sin mayúsculas"

print(tiene_mayusculas(frase_1))  # True
print(tiene_mayusculas(frase_2))  # False
