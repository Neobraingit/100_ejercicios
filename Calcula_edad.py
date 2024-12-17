


from datetime import datetime

# Pedir al usuario su fecha de nacimiento
fecha_nacimiento_str = input("Por favor, ingresa tu fecha de nacimiento (formato día/mes/año): ")

# Convertir la cadena de texto a un objeto datetime
try:
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
    
    # Obtener la fecha de hoy
    fecha_actual = datetime.now()
    
    # Calcular la edad
    edad = fecha_actual.year - fecha_nacimiento.year
    
    # Ajustar si el cumpleaños aún no ha ocurrido este año
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

    # Mostrar la edad calculada
    print(f"Tienes {edad} años.")
except ValueError:
    print("El formato de fecha ingresado no es válido. Intenta nuevamente usando día/mes/año.")
