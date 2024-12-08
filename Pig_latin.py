
def to_pig_latin(word):
    """
    Convierte una palabra al formato "Pig Latin".
    
    Args:
        word (str): La palabra que se va a convertir.
    
    Returns:
        str: La palabra en "Pig Latin".
    """
    vowels = "aeiou"
    word = word.lower()  # Asegurarse de trabajar con minúsculas
    
    if word[0] in vowels:
        # Si la palabra comienza con vocal
        return word + "way"
    else:
        # Si la palabra comienza con consonante
        # Encuentra el índice del primer carácter vocálico
        for i, letter in enumerate(word):
            if letter in vowels:
                return word[i:] + word[:i] + "ay"
        # Si no hay vocales (palabras inusuales), simplemente añade "ay" al final
        return word + "ay"

# Ejemplos de uso
print(to_pig_latin("hello"))  # Salida: ellohay
print(to_pig_latin("apple"))  # Salida: appleway
print(to_pig_latin("string"))  # Salida: ingstray
print(to_pig_latin("rhythm"))  # Salida: rhythmay (no tiene vocales)
