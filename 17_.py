'''De dos listas, hacer una tercera que contenga los elementos en común de las dos'''

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lista2 = [1, 2, 4, 5, 7, 4, 3, 7, 9]

lista3 = []
for i in lista1:
    if i in lista2:
        lista3.append(i)
        
print (lista3)