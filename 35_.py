'''Escribir una función que pida una lista y un elemento y verifique si el elelemento está en dicha lista'''

def verified(dato1, dato2):
    if dato2 in dato1:
        return True
    else:
        return False
    
print (verified([2, 3, 4, 5], 9))