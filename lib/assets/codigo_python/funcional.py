import time,sys,os
from imports_imagenes import * #del codigo imports_imagenes.py

##donde va la cantidad de movimiento (Girar o zoom) ?cliente o server?

#####-------CLIENTE (INDICA QUE ACCION REALIZAR)-----------------------
if __name__ == "__main__":
	for coso in sys.argv:
		print coso
	print "fin"
	print os.getcwd()

	name_image = sys.argv[1]#raw_input("Nombre de imagen GIF: ")
	folder = sys.argv[2]

	inicializar(name_image,folder)

	while(True):
		#ver lo de primero mover derecha o izq
		opcion = raw_input("Girar: \n1 Derecha \n2 Izquierda \nZoom:\n3 Zoom in \n4 Zoom out\n5 Rotar\n7 Centrar\n8 Agregar texto\n0 Reset\n")

		start_time = time.time()
		texto_proyeccion = ""
		cantidad = 0
	    #asignar cantidad de mov
		if opcion == '1': # movimiento girar derecha
		    cantidad = 0.1

		elif opcion == '2': #movimiento girar izquierda
		    cantidad = 0.1

		elif opcion == '3': #hacer zoom
		    cantidad = 0.1

		elif opcion == '4': #quitar zoom
		    cantidad = 0.1

		#para opcion rotar solo enviar opcion "5" (incluye antihorario-horario--mismo mov)

		#para opcion 7 solo enviar '7' o centrar

		elif opcion == '8':
			texto_proyeccion = raw_input("Ingrese texto: ")

		hacer(opcion,cantidad,texto_proyeccion) ##mucho mas simplificado (todo lo configura el server) texto_proyeccion = "" para vacio

		print "Demoro %f segundos en total"%(time.time() - start_time)
