'''Escribir una función que requiere 3 parámetros: una lista, un índice de cálculo y un fin de cálculo. 
La función debe devolver la suma de los números que se encuentren entre los índices'''

def suma_entre_indices(lista, indice_inicio, indice_fin):
    suma = 0

    # Verificar si los índices son válidos
    if indice_inicio >= len(lista) or indice_fin >= len(lista):
        return "Los índices están fuera del rango de la lista."

    # Asegurarse de que el índice de inicio sea menor o igual al índice de fin
    if indice_inicio > indice_fin:
        return "El índice de inicio debe ser menor o igual al índice de fin."

    # Calcular la suma de los números entre los índices
    for i in range(indice_inicio, indice_fin + 1):
        suma += lista[i]

    return suma


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
indice_inicio = 2
indice_fin = 6

resultado = suma_entre_indices(numeros, indice_inicio, indice_fin)
print(resultado)  # Output: 25 (3 + 4 + 5 + 6 + 7)
 