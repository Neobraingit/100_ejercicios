'''Escribir una función que tome como parámetros la hora de inicia y la hora de final
calcular la cantidad de días y horas entre ellos'''


from datetime import datetime, timedelta

def calcular_dias_horas(hora_inicio, hora_fin):
    formato_hora = "%H:%M"  # Formato de hora

    # Obtener objetos de tiempo para la hora de inicio y finalización
    inicio = datetime.strptime(hora_inicio, formato_hora)
    fin = datetime.strptime(hora_fin, formato_hora)

    # Calcular la diferencia de tiempo
    diferencia = fin - inicio

    # Calcular la cantidad de días y horas
    dias = diferencia.days
    horas = diferencia.seconds // 3600

    return dias, horas

hora_inicio = "09:30"
hora_fin = "17:45"

dias, horas = calcular_dias_horas(hora_inicio, hora_fin)
print(f"Cantidad de días: {dias}")
print(f"Cantidad de horas: {horas}")
