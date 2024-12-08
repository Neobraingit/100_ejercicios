

import time
import os

def reloj_en_tiempo_real():
    try:
        while True:
            # Obtener la hora actual
            hora_actual = time.strftime("%H:%M:%S")
            # Limpiar la consola
            os.system('cls' if os.name == 'nt' else 'clear')
            # Mostrar la hora actual
            print("Hora actual:", hora_actual)
            # Pausa de 1 segundo
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nReloj detenido.")

# Ejecutar el reloj
reloj_en_tiempo_real()
