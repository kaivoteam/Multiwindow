import os.path, os,time,sys
from PIL import Image,ImageTk #para abrir la imagen

try:
    import Tkinter as tk # this is for python2
except:
    import tkinter as tk # this is for python3

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

class Application(tk.Tk): # I buried this in a class. I prefer that for tk
    def __init__(self):
    	try:
        	super().__init__() # call Tk.__init__
        except:
        	tk.Tk.__init__(self)

        self.CYCLEDELAY = 1 # 3 second per cycle

        # create and place the label once.
        self.image_label = tk.Label(self)
        self.image_label.place(x=0,y=0)

        # call our function
        self.changeImage()

    def changeImage(self):
		"""Change the image on a delay"""
		#dirlist = os.listdir('Ejemplo/')
		global folder

		finput = folder+'/imagen_generada.png' #nombre standar para la imagen
		foutput = folder+'/imagen_mostrada.png'

		while not os.path.exists(finput):
			print "esperando que se cree el archivo"
			time.sleep(0.01)

		while os.path.getsize(finput) == 0: #no lea antes que se llene
			print "esperando que aumente el tamanno"
			time.sleep(0.01)

		print "archivo creado.."
		time.sleep(1)

		if os.path.exists(foutput):
			os.remove(foutput) #elminate

		os.rename(finput, foutput)
		#foutput es la imagen que se utilizara

		image = Image.open(foutput)
		# you had a funky method of getting a random member here. I cleaned it up

		i_width, i_height = image.size

		#self.geometry("{}x{}".format(i_width,i_height))
		# change root's geometry using string formatting (preferred)

		#self.image_label.configure(width=i_width, height=i_height)
		# change the label's geometry using string formatting

		self.tkpi = ImageTk.PhotoImage(image)
		self.image_label.configure(image=self.tkpi)
		# configure the label to use the PhotoImage

		self.after(self.CYCLEDELAY,self.changeImage)
		# loop!

if __name__ == "__main__":
	folder = sys.argv[1]

	root = Application()
	grande = FullScreenApp(root)
	root.mainloop()