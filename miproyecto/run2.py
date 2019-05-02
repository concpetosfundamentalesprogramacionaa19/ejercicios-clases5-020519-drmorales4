"""
	file: run2.py
	autor: drmorales4
"""

from misvariables import *

# uso de condicional simple

nota = input ("Ingrese la nota 1: ")

nota2 = input("Ingrese la nota 2: ")

nota = int(nota)
nota2 = int(nota2)

if nota >= 18:
	print("%s, con una nota de: %d" % (mensaje, nota))
else:
	print("%s, con una nota de: %d" % (mensaje2, nota))

if nota2 >= 18:
	print("%s, con una nota de: %d" % (mensaje, nota2))
else:
	print("%s, con una nota de: %d" % (mensaje2, nota2))