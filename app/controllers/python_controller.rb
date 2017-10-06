class PythonController < ApplicationController
  def new
  	#nombre de la imagen obtenida del catalogo
    nombre_imagen = "corazon"
  	pwd= Rails.root.to_s
  	imagenes_folder = pwd+"/lib/assets/codigo_python/imagenes/"

  	job1 = fork do
  		exec("python lib/assets/codigo_python/integracion.py "+nombre_imagen+" 1 "+imagenes_folder) #genera imagenes
  	 #para ejecutar es necesario "nombre de imagen + carpeta de imagenes + giro gif"
    end

    print "HOLA MUNDO-----------------------"

    job2 = fork do 
      exec("python lib/assets/codigo_python/checkeo_imagen.py "+pwd) #actualiza imagenes en una ventana
    end

  	Process.detach(job1)
    Process.detach(job2)

	#result = `python lib/assets/codigo_python/funcional.py corazon `+imagenes_folder+'`'
	#render :text => result
	#print "paso"
  end

  def create
  end
end
