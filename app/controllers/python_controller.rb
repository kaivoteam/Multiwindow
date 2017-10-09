class PythonController < ApplicationController
  def new
  	#nombre de la imagen obtenida del catalogo
    nombre_imagen = "corazon"
  	pwd= Rails.root.to_s
  	imagenes_folder = pwd+"/lib/assets/codigo_python/imagenes/"

    # Ubuntu
    require 'os'

    #En win
    if OS.windows?  #=> true or false
      job1 = Process.spawn("python lib/assets/codigo_python/leer_leapmotion.py "+nombre_imagen+" 1 "+imagenes_folder)
      job2 = Process.spawn("python lib/assets/codigo_python/checkeo_imagen.py "+pwd+" "+nombre_imagen+" 1 "+imagenes_folder)
      job3 = Process.spawn("python lib/assets/codigo_python/vista_imagen.py "+pwd)
    else
    	job1 = fork do
    		exec("python lib/assets/codigo_python/leer_leapmotion.py "+nombre_imagen+" 1 "+imagenes_folder) #genera imagenes
    	 #para ejecutar es necesario "nombre de imagen + carpeta de imagenes + giro gif"
      end

      job2 = fork do 
        exec("python lib/assets/codigo_python/checkeo_imagen.py "+pwd+" "+nombre_imagen+" 1 "+imagenes_folder) #actualiza imagenes en una ventana
        #necesito argumentos de job1 y job2
      end

      job3 = fork do 
        exec("python lib/assets/codigo_python/vista_imagen.py "+pwd) #actualiza imagenes en una ventana
      end
    end

  	#Process.detach(job1)
    #Process.detach(job2)
    #Process.detach(job3)

	#result = `python lib/assets/codigo_python/funcional.py corazon `+imagenes_folder+'`'
	#render :text => result
	#print "paso"
  end

  def create
  end
end
