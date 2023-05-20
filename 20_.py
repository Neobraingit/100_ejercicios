# Escribir un programa que muestre los valores de las claves 'manzana' y 'banana' que corresponden con 3 y 7

datos = {'manzana': 3, 'banana': 7}

clave_manzana = 'manzana'
clave_banana = 'banana'

valor_manzana = datos.get(clave_manzana)
valor_banana = datos.get(clave_banana)

print(f"El valor correspondiente a '{clave_manzana}' es: {valor_manzana}")
print(f"El valor correspondiente a '{clave_banana}' es: {valor_banana}")
