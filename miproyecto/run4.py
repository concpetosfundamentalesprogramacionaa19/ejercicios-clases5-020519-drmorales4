"""
	file: run4.py
	autor: drmorales4

	
	deseamos obtener el costo de una carrera universitaria
	el valor promedio de cada ciclo es de 1200 $
	el valor promedio del seguro educativo por ciclo es de 100 $
	si la edad del estudiante es <= 20, caso contrario sera de $ 150
	si el estudiante tiene una modalidad a distancia el numero de ciclos a seguir es de 10
	caso contrario debera seguir 8 ciclos
	- obtener la proyeccion del costo de la carrera de un estudiante

"""


from misvariables import *

# 

edad = input ("Por favor Ingrese su edad: ") # se ingresa la edad

edad = int(edad)

costo = 1200 	# costo promedio de la matricula
seguro_1 = 100	# seguro si el estudiante es menor o igual a 20 años
seguro_2 = 150		# seguro si el estudiante es mayor a 20 años
ciclo_distancia = 10		# numero de ciclos si es modalidad a distancia
ciclo_presencial = 8		# numero de ciclos si es modalidad presencial

modalidad = input ("Ingrese su modalidad (Distancia o Presencial): ")	# ingresar la modalidad presencial o distacia


if (modalidad == "Distancia") and (edad <= 20):
	costo_final = costo * ciclo_distancia + seguro_1 * ciclo_distancia
	print ("%s %d " % ("\nEl costo de toda la carrera e: ", costo_final))
else:
	if (modalidad == "Distancia") and (edad > 20):
		costo_final = costo * ciclo_distancia + seguro_2 * ciclo_distancia
		print ("%s %d " % ("\nEl costo de toda la carrera e: ", costo_final))
	else:
		if (modalidad == "Presencial") and (edad <= 20):
			costo_final = costo * ciclo_presencial + seguro_1 * ciclo_presencial
			print ("%s %d " % ("\nEl costo de toda la carrera e: ", costo_final))
		else:
			if (modalidad == "Presencial") and (edad > 20):
				costo_final = costo * ciclo_presencial + seguro_2 * ciclo_presencial
				print ("%s %d " % ("\nEl costo de toda la carrera e: ", costo_final))





