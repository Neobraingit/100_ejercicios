'''Escribir una función que demuestre si los dígitos de una cifra son iguales o no'''

def digitos_iguales(numero):
    str_numero = str(numero)
    primer_digito = str_numero[0]
    return all(digito == primer_digito for digito in str_numero)

# Ejemplo de uso
numero1 = 111111
numero2 = 123456
numero3 = 777777

print(digitos_iguales(numero1))  # Devuelve True
print(digitos_iguales(numero2))  # Devuelve False
print(digitos_iguales(numero3))  # Devuelve True
