# Crear una lista  de números pares del 1 al 10

lista_par = []

for i in range (1, 11):
    if i % 2 == 0:
        lista_par.append(i)
print (lista_par)