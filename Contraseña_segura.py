
import random
import string

def generar_contraseña(longitud):
    if longitud < 4:  # Se recomienda un mínimo de 4 para incluir todos los tipos de caracteres
        raise ValueError("La longitud debe ser de al menos 4 caracteres.")
    
    # Definir el conjunto de caracteres posibles
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Asegurar que la contraseña tenga al menos un carácter de cada tipo
    contraseña = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Completar con caracteres aleatorios hasta alcanzar la longitud deseada
    contraseña += random.choices(caracteres, k=longitud - 4)
    
    # Mezclar los caracteres para mayor seguridad
    random.shuffle(contraseña)
    
    return ''.join(contraseña)

# Ejemplo de uso
longitud = 12  # Cambiar según sea necesario
contraseña = generar_contraseña(longitud)
print("Contraseña generada:", contraseña)
