'''Imprimir solo los números impares del 10 y el 20.
Hacer dos versiones con for y while'''

for i in range (11, 20, 2):
    print (i)
    
print ('----------------------------------------')

numero = 10
while numero <= 20:
    if numero % 2 != 0:
        print (numero)
    numero += 1
    