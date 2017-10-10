import os.path, os,time,sys
from imports_imagenes import * #del codigo imports_imagenes.py


if __name__ == "__main__":
	folder = sys.argv[1]
	name_image = sys.argv[2]
	giro = sys.argv[3]
	folder_imagenes = sys.argv[4]

	finput = folder+'/imagen_generada.png' #nombre standar para la imagen
	foutput = folder+'/imagen_mostrada.png'

	while(True):
		print "esperando que se cree el archivo"
		while( not os.path.exists(finput)):
			#chequear si se hace reset y

			if os.path.exists(folder+"/reset"):
				##reset elegante
				print("acaba de acontecer un reset")
				inicializar(name_image,giro,folder_imagenes)
				os.remove(folder+"/reset")

			time.sleep(0.001)
		
		print("esperando que aumente el tamanno")
		while(os.path.getsize(finput) == 0): #no lea antes que se llene
			time.sleep(0.001)

		print("archivo creado..")

		if os.path.exists(foutput):
			os.remove(foutput) #elminate

		os.rename(finput, foutput)
	#foutput es la imagen que se utiliz
	#print "archivos generados"
	#time.sleep(1) #esperar que todo se refresque