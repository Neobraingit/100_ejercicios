'''Escribir una función que tenga como parámetro la ruta de un directorio y nos devuelva la cantidad de archivos que hay dentro'''
import os

def contar_archivos(ruta_directorio):
    # Obtener la lista de archivos en el directorio
    lista_archivos = os.listdir(ruta_directorio)
    
    # Contar la cantidad de archivos
    cantidad_archivos = len(lista_archivos)
    
    return cantidad_archivos

contar_archivos('/home/Marcos/Documentos')
