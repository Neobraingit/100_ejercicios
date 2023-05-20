'''Crear la variable L con la lista [-6, 5, -3, -1, 2, 8, -3, 6] luego crear una nueva lista con
los números que son mayores que cero'''

L = [-6, 5, -3, -1, 2, 8, -3, 6]
L2 = []

for i in L:
    if i > 0:
        L2.append(i)
    
    
print (L2)

