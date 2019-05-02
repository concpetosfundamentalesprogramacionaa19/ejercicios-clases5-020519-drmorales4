"""
	file: run3.py
	autor: drmorales4

	nota mayor o igual a 18: sobresaliente
	nota mayor o igual a 16 y menor a 18: muy buena
	nota mayor o igual a 13 y menor a 16: buena
	nota menor a 13: insificiente

"""

from misvariables import *

# condiciones anidadas

nota = input ("Ingrese su Nota: ")

nota = int(nota)

if nota >= 18:
	print ("%s - nota: %d" % ("Sobresaliente", nota))
else:
	if (nota >= 16) and (nota < 18):
		print ("%s - nota: %d" % ("Muy buena", nota))
	else:
		if (nota >= 13) and (nota < 16):
			print ("%s - nota: %d" % ("Buena", nota))
		else:
			print ("%s - nota: %d" % ("Insificiente", nota))

