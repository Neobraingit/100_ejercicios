
import mysql.connector



from mysql.connector import Error

try:
    # Establecer la conexión
    connection = mysql.connector.connect(
        host='localhost',  # Cambia por la dirección de tu servidor
        user='root',  # Tu nombre de usuario
        password='',  # Tu contraseña
        database='Archivos'  # Nombre de la base de datos
    )
    
    if connection.is_connected():
        print("Conexión exitosa a la base de datos")
        
        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()
        
        # Escribir y ejecutar una consulta
        query = "SELECT * FROM Libros"
        cursor.execute(query)
        
        # Obtener resultados
        results = cursor.fetchall()
        for row in results:
            print(row)
        
except Error as e:
    print(f"Error al conectar a MySQL: {e}")

finally:
    # Cerrar la conexión
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión cerrada")

    