'''Crea un programa que genere un nombre de superhéroe único.
Requisitos:

Solicita al usuario su color favorito y un animal que le guste.
Combina estas palabras con una característica aleatoria, como "Increíble", "Misterioso", "Volador", etc.
Devuelve un nombre como: "El Increíble Tigre Azul" o "La Voladora Pantera Roja".'''

import random

color = input('Dime tu color favorito: ')
animal = input('Dime tu animal favorito: ')
características_aleatorias = ['voladora', 'rápido', 'grande', 'pequeño']

print (f'El {random.choice(características_aleatorias)} {animal} {color}')