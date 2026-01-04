from PIL import Image, ImageTk

#Cambiar PATH
PATH="C:\\Users\\DEV-CR\\Desktop\\ProyectosGIT\\Python_modules\\Challenge_27_EncenderPC\\"

def obtenerImagen(nombre,ancho=300):
    imagen = Image.open(PATH+nombre)
    porcentaje = (ancho / float(imagen.size[0]))
    alto = int((float(imagen.size[1]) * float(porcentaje)))
    imagenModificada=imagen.resize((ancho, alto), Image.Resampling.LANCZOS)
    photoImg=ImageTk.PhotoImage(imagenModificada)

    return photoImg



