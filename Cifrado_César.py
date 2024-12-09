def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        # Verificar si el carácter es una letra
        if caracter.isalpha():
            # Determinar si es mayúscula o minúscula
            inicio = ord('A') if caracter.isupper() else ord('a')
            # Calcular el carácter cifrado
            nuevo_caracter = chr((ord(caracter) - inicio + desplazamiento) % 26 + inicio)
            resultado += nuevo_caracter
        else:
            # Si no es letra, dejarlo sin cambios
            resultado += caracter
    return resultado

# Ejemplo de uso
texto_original = "Hola Mundo!"
desplazamiento = 3

# Cifrar el texto
texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
print("Texto cifrado:", texto_cifrado)

# Descifrar el texto
texto_descifrado
