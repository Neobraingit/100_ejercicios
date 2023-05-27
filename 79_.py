'''Verificar si una cadena es un número o no, devolviendo Tre o False según el caso'''

def es_numero(cadena):
    return cadena.isdigit()

# Ejemplo de uso
cadena1 = "12345"
cadena2 = "abc123"

print(es_numero(cadena1))  # Devuelve True
print(es_numero(cadena2))  # Devuelve False
