'''Escribir una función con tres parámetros(n, a, numUmbral) que permita encontrar los números de 0 hasta el umbral dado
que son divisibles por n pero no por a'''

def encontrar_numeros_divisibles(n, a, num_umbral):
    numeros_encontrados = []
    for num in range(num_umbral + 1):
        if num % n == 0 and num % a != 0:
            numeros_encontrados.append(num)
    return numeros_encontrados

resultado = encontrar_numeros_divisibles(3, 2, 20)
print(resultado)
