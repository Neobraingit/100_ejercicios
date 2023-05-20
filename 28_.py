# Escribir un programa que permita medir el tiempo de ejecución de un script.

import time

# Inicio del temporizador
inicio = time.time()

# Código que quieres medir
for i in range (1, 11):
    for e in range(1, 11):
        x = i * e
        if e == 8:
          print (i, '*', e, '=', x)

# Fin del temporizador
fin = time.time()

# Cálculo del tiempo transcurrido
tiempo_transcurrido = fin - inicio

# Imprimir el tiempo transcurrido
print("Tiempo transcurrido: ", tiempo_transcurrido, "segundos")
