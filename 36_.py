# Crea una función que sume la totalidad de las cifras de un número

def sum_numero(num):
    cifra = 0
    for i in str(num): # La pasamos a string para poder recorrerla
        cifra += int(i) # Lo pasamos a int para poder sumarlo
        
    print (cifra)
    
sum_numero(2222333)
