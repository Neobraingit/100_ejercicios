
import time
import datetime

# Bucle infinito para el reloj
while True:
    # Obtener la hora actual
    ahora = datetime.datetime.now()
    
    # Extraer horas, minutos y segundos
    horas = ahora.hour
    minutos = ahora.minute
    segundos = ahora.second

    # Mostrar la hora en formato HH:MM:SS
    print(f"{horas:02}:{minutos:02}:{segundos:02}", end="\r")  # "\r" sobrescribe la línea actual

    # Esperar un segundo antes de actualizar
    time.sleep(1)
