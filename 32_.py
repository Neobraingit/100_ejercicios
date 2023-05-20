'''Crear la variable L y asignarle esta lista [3, 6, 9, 12, 15, 18, 21, 24] después crear otra variable que contenga los números
de L divididos por 3.
Mostrar esa segunda variable por consola'''

L = [3, 6, 9, 12, 15, 18, 21, 24]

# Crear otra variable con los números de L divididos por 3
L2 = [i/ 3 for i in L]

# Mostrar la segunda variable por consola
print(L2)
