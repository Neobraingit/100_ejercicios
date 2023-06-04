'''Sumar todos lo dígitos de una cifra'''

def sumar_digitos(numero):
    suma = 0
    str_numero = str(numero)
    for digito in str_numero:
        suma += int(digito)
    return suma

# Ejemplo de uso
numero = 12345
resultado = sumar_digitos(numero)
print(resultado)

